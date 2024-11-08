describe('Login page tests', function () { // Use 'function' keyword here
  beforeEach(function () { // Use 'function' keyword here
    const UNIQUE_SUFFIX = Date.now();
    this.USERNAME = `test${UNIQUE_SUFFIX}`;
    this.EMAIL = `test${UNIQUE_SUFFIX}@example.com`;
    this.PASSWORD = `Test123#`;

    cy.signup(this.USERNAME, this.EMAIL, this.PASSWORD);
    cy.visit('/accounts/login/');
  });

  it('should not login since missing email', function () {
    cy.get('#id_password').type(this.PASSWORD);
    cy.get('#submit_login').click();
    cy.get('#id_username:invalid')
      .invoke('prop', 'validationMessage')
      .should('eq', 'Please fill out this field.');
  });

  it('should not login since missing password', function () {
    cy.get('#id_username').type(this.EMAIL);
    cy.get('#submit_login').click();
    cy.get('#id_password:invalid')
      .invoke('prop', 'validationMessage')
      .should('eq', 'Please fill out this field.');
  });

  it('should not login since wrong email or password', function () {
    cy.get('#id_username').type(this.EMAIL);
    cy.get('#id_password').type(this.PASSWORD + '1');
    cy.get('#submit_login').click();
    cy.get('#password_errors').should('have.text', 'Invalid email or password');
  });

  it('should login successfully', function () { // Use 'function' keyword here
    cy.get('#id_username').type(this.EMAIL);
    cy.get('#id_password').type(this.PASSWORD);
    cy.get('#submit_login').click();
    cy.get('#id_profile_username').should('have.text', this.USERNAME);
  });
});