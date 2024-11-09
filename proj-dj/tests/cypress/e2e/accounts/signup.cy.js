describe('Signup page tests', function () {
  beforeEach(function () {
    cy.visit('/accounts/signup/')
    const UNIQUE_SUFFIX = Date.now();
    this.USERNAME = `test${UNIQUE_SUFFIX}`;
    this.EMAIL = `test${UNIQUE_SUFFIX}@example.com`;
    this.PASSWORD = `Test123#`;
  });

  it('should not sign up since missing username', function () {
    cy.get('#id_email').type(this.EMAIL);

    const date = '12311990'; // MMDDYYYY
    const formattedDate = `${date.slice(4, 8)}-${date.slice(0, 2)}-${date.slice(2, 4)}`; // YYYY-MM-DD
    cy.get('#id_date_of_birth').type(formattedDate);

    cy.get('#id_password1').type(this.PASSWORD);
    cy.get('#id_password2').type(this.PASSWORD);

    // Submit the signup form
    cy.get('#submit_signup').click();

    cy.get('#id_username:invalid')
      .invoke('prop', 'validationMessage')
      .should('eq', 'Please fill out this field.');
  });

  it('should not sign up since missing email', function () {
    cy.get('#id_username').type(this.USERNAME);
    

    const date = '12311990'; // MMDDYYYY
    const formattedDate = `${date.slice(4, 8)}-${date.slice(0, 2)}-${date.slice(2, 4)}`; // YYYY-MM-DD
    cy.get('#id_date_of_birth').type(formattedDate);

    cy.get('#id_password1').type(this.PASSWORD);
    cy.get('#id_password2').type(this.PASSWORD);

    // Submit the signup form
    cy.get('#submit_signup').click();

    cy.get('#id_email:invalid')
      .invoke('prop', 'validationMessage')
      .should('eq', 'Please fill out this field.');
  });

  it('should not sign up since missing date of birth', function () {
    cy.get('#id_username').type(this.USERNAME);

    cy.get('#id_email').type(this.EMAIL);

    cy.get('#id_password1').type(this.PASSWORD);
    cy.get('#id_password2').type(this.PASSWORD);

    // Submit the signup form
    cy.get('#submit_signup').click();

    cy.get('#id_date_of_birth:invalid')
      .invoke('prop', 'validationMessage')
      .should('eq', 'Please fill out this field.');
  });

  it('should not sign up since missing password1', function () {
    cy.get('#id_username').type(this.USERNAME);

    cy.get('#id_email').type(this.EMAIL);

    const date = '12311990'; // MMDDYYYY
    const formattedDate = `${date.slice(4, 8)}-${date.slice(0, 2)}-${date.slice(2, 4)}`; // YYYY-MM-DD
    cy.get('#id_date_of_birth').type(formattedDate);

    cy.get('#id_password2').type(this.PASSWORD);

    // Submit the signup form
    cy.get('#submit_signup').click();

    cy.get('#id_password1:invalid')
      .invoke('prop', 'validationMessage')
      .should('eq', 'Please fill out this field.');
  });

  it('should not sign up since missing password2', function () {
    cy.get('#id_username').type(this.USERNAME);

    cy.get('#id_email').type(this.EMAIL);

    const date = '12311990'; // MMDDYYYY
    const formattedDate = `${date.slice(4, 8)}-${date.slice(0, 2)}-${date.slice(2, 4)}`; // YYYY-MM-DD
    cy.get('#id_date_of_birth').type(formattedDate);

    cy.get('#id_password1').type(this.PASSWORD);

    // Submit the signup form
    cy.get('#submit_signup').click();

    cy.get('#id_password2:invalid')
      .invoke('prop', 'validationMessage')
      .should('eq', 'Please fill out this field.');
  });

  it('should not sign up since username too short', function () {
    const truncatedUsername = this.USERNAME.slice(3, 7);

    cy.get('#id_username').type(truncatedUsername);

    cy.get('#id_email').type(this.EMAIL);

    const date = '12311990'; // MMDDYYYY
    const formattedDate = `${date.slice(4, 8)}-${date.slice(0, 2)}-${date.slice(2, 4)}`; // YYYY-MM-DD
    cy.get('#id_date_of_birth').type(formattedDate);

    cy.get('#id_password1').type(this.PASSWORD);
    cy.get('#id_password2').type(this.PASSWORD);

    // Submit the signup form
    cy.get('#submit_signup').click();
    cy.get('#username_errors').should('have.text', 'Username too short. It must be at least 5 characters.');
  });

  it('should not sign up since username already exist', function () {
    cy.signup(this.USERNAME, this.EMAIL, this.PASSWORD);
    cy.signup(this.USERNAME, this.EMAIL+'.br', this.PASSWORD);
    cy.get('#username_errors').should('have.text', 'Username already exists.');
  });

  it.only('should not sign up since birthday cannot be in the future', function () {
    cy.get('#id_username').type(this.USERNAME);

    cy.get('#id_email').type(this.EMAIL);

    const date = '12312025'; // MMDDYYYY
    const formattedDate = `${date.slice(4, 8)}-${date.slice(0, 2)}-${date.slice(2, 4)}`; // YYYY-MM-DD
    cy.get('#id_date_of_birth').type(formattedDate);

    cy.get('#id_password1').type(this.PASSWORD);
    cy.get('#id_password2').type(this.PASSWORD);

    // Submit the signup form
    cy.get('#submit_signup').click();
    cy.get('#date_of_birth_errors').should('have.text', 'Birthday cannot be in the future.');
  });

  it('should not sign up since password must contain at least 8 characters', function () {
    cy.get('#id_username').type(this.USERNAME);

    cy.get('#id_email').type(this.EMAIL);

    const date = '12311990'; // MMDDYYYY
    const formattedDate = `${date.slice(4, 8)}-${date.slice(0, 2)}-${date.slice(2, 4)}`; // YYYY-MM-DD
    cy.get('#id_date_of_birth').type(formattedDate);
    const truncatedPassword = this.PASSWORD.slice(0, 6);
    cy.get('#id_password1').type(truncatedPassword);
    cy.get('#id_password2').type(truncatedPassword);

    // Submit the signup form
    cy.get('#submit_signup').click();

    cy.get('#password_errors1').should('have.text', 'Password must contain at least 8 characters.');
  });

  it.only(`should not sign up since passwords don't match.`, function () {
    cy.get('#id_username').type(this.USERNAME);

    cy.get('#id_email').type(this.EMAIL);

    const date = '12312019'; // MMDDYYYY
    const formattedDate = `${date.slice(4, 8)}-${date.slice(0, 2)}-${date.slice(2, 4)}`; // YYYY-MM-DD
    cy.get('#id_date_of_birth').type(formattedDate);

    cy.get('#id_password1').type(this.PASSWORD);
    cy.get('#id_password2').type(this.PASSWORD+'1');

    // Submit the signup form
    cy.get('#submit_signup').click();

    cy.get('#password_errors2').should('have.text', `Passwords don't match.`);
  });

  it('should sign up successfully', function () {
    cy.signup(this.USERNAME, this.EMAIL, this.PASSWORD);
    cy.location().should((loc) => {
      expect(loc.pathname).to.eq('/accounts/login/');
    });
  });
});