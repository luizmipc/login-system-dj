describe('Update users tests logged in', function () {
  beforeEach(function () {
    const UNIQUE_SUFIXX = Date.now();

    this.USERNAME = `teste${UNIQUE_SUFIXX}`;
    this.EMAIL = `teste${UNIQUE_SUFIXX}@example.com`;
    this.PASSWORD = `1234567890#Kl`;

    cy.signup(this.USERNAME, this.EMAIL, this.PASSWORD);

    cy.visit('/accounts/login/');
    cy.get('#id_username').type(this.EMAIL);
    cy.get('#id_password').type(this.PASSWORD);
    cy.get('#submit_login').click();
    cy.visit(`/accounts/profile/${this.USERNAME}/update/`);
  });

  it('should not update since missing username', function () {
    cy.get('#id_username').clear();
    cy.get('#submit_update').click();
    cy.get('#id_username:invalid')
      .invoke('prop', 'validationMessage')
      .should('eq', 'Please fill out this field.');
  });

  it('should not update since missing email', function () {
    cy.get('#id_email').clear();
    cy.get('#submit_update').click();
    cy.get('#id_email:invalid')
      .invoke('prop', 'validationMessage')
      .should('eq', 'Please fill out this field.');
  });

  it('should not update since missing birthday', function () {
    cy.get('#id_date_of_birth').clear();
    cy.get('#submit_update').click();
    cy.get('#id_date_of_birth:invalid')
      .invoke('prop', 'validationMessage')
      .should('eq', 'Please fill out this field.');
  });

  it('should not update since username too short', function () {
    const truncatedUsername = this.USERNAME.slice(3, 7);
    cy.get('#id_username').clear().type(truncatedUsername);
    cy.get('#submit_update').click();
    cy.get('#username_errors').should('have.text', 'Username too short. It must be at least 5 characters.');
  });

  it.only('should not update since username already exist', function () {
    const UNIQUE_SUFIXX = Date.now();

    let username = `teste${UNIQUE_SUFIXX}`;
    let email = `teste${UNIQUE_SUFIXX}@example.com`;
    let password = `1234567890#Kl`;

    cy.signup(username, email, password);
    cy.get('#submit_logout').click();
    cy.visit('/accounts/login/');
    cy.get('#id_username').type(this.EMAIL);
    cy.get('#id_password').type(this.PASSWORD);
    cy.get('#submit_login').click();
    cy.visit(`/accounts/profile/${this.USERNAME}/update/`);
    cy.get('#id_username').clear().type(username);
    cy.get('#submit_update').click();
    cy.get('#username_errors').should('have.text', 'Username already exists.');
  });

  it.only('should not update since email already exist', function () {
    const UNIQUE_SUFIXX = Date.now();

    let username = `teste${UNIQUE_SUFIXX}`;
    let email = `teste${UNIQUE_SUFIXX}@example.com`;
    let password = `1234567890#Kl`;

    cy.signup(username, email, password);
    cy.get('#submit_logout').click();
    cy.visit('/accounts/login/');
    cy.get('#id_username').type(this.EMAIL);
    cy.get('#id_password').type(this.PASSWORD);
    cy.get('#submit_login').click();
    cy.visit(`/accounts/profile/${this.USERNAME}/update/`);
    cy.get('#id_email').clear().type(email);
    cy.get('#submit_update').click();
    cy.get('#email_errors').should('have.text', 'Email already exists.');
  });

  it('should load the profile details successfully', function () {
    cy.get('#id_username').should('have.value', this.USERNAME);
    cy.get('#id_email').should('have.value', this.EMAIL);
    const date = '12311990'; // MMDDYYYY
    const formattedDate = `${ date.slice(4, 8)}-${date.slice(0, 2)}-${date.slice(2, 4)}`; // YYYY-MM-DD
    cy.get('#id_date_of_birth').should('have.value', formattedDate);
  });

  it('should update username successfully', () => {
    const UNIQUE_SUFIXX = Date.now();

    let newusername = `teste${UNIQUE_SUFIXX}`;
    cy.get('#id_username').clear().type(newusername);
    cy.get('#submit_update').click();
    cy.get('#id_username').should('have.text', newusername);
  });

  it('should update email successfully', () => {
    const UNIQUE_SUFIXX = Date.now();
    let newemail = `teste${UNIQUE_SUFIXX}@example.com`;
    cy.get('#id_email').clear().type(newemail);
    cy.get('#submit_update').click();
    cy.get('#id_email').should('have.text', newemail);
  });

  it('should update birthday successfully', () => {
    const newdate = '06152000'; // MMDDYYYY
    const formattedNewDate = `${ newdate.slice(4, 8)}-${newdate.slice(0, 2)}-${newdate.slice(2, 4)}`;
    cy.get('#id_date_of_birth').clear().type(formattedNewDate);
    cy.get('#submit_update').click();
    const formattedPrintNewDate = `${newdate.slice(0, 2)}/${newdate.slice(2, 4)}/${ newdate.slice(4, 8)}`;
    cy.get('#id_date_of_birth').should('have.text', formattedPrintNewDate);
  });
});