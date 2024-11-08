describe('Home app tests logged in', () => {
  beforeEach(() => {
    const UNIQUE_SUFIXX = Date.now();

    const USERNAME = `teste${UNIQUE_SUFIXX}`;
    const EMAIL = `teste${UNIQUE_SUFIXX}@example.com`;
    const PASSWORD = `1234567890#Kl`;
    cy.visit('/accounts/signup/');
    cy.get('#id_username').type(USERNAME);
    cy.get('#id_email').type(EMAIL);
    
    // Convert MM/DD/YYYY to YYYY-MM-DD
    const date = '12311990'; // MMDDYYYY
    const formattedDate = `${date.slice(4, 8)}-${date.slice(0, 2)}-${date.slice(2, 4)}`; // Converts to YYYY-MM-DD

    cy.get('#id_date_of_birth').type(formattedDate); // Use the formatted date
    cy.get('#id_password1').type(PASSWORD);
    cy.get('#id_password2').type(PASSWORD);
    cy.get('#submit_signup').click()
    cy.visit('/accounts/login/');
    cy.get('#id_username').type(EMAIL);
    cy.get('#id_password').type(PASSWORD);
    cy.get('#submit_login').click();
  });

  it('should load the login page successfully', () => {
    cy.get('#link-to-login').click();
    cy.location().should((loc) => {
      expect(loc.pathname).to.eq('/accounts/login/');
    });
  });

  it('should load the page signup page successfully', () => {
    cy.get('#link-to-signup').click()
    cy.location().should((loc) => {
      expect(loc.pathname).to.eq('/accounts/signup/');
    });
  });

  it('should load the home page successfully', () => {
    cy.get('#link-to-home').click()
    cy.location().should((loc) => {
      expect(loc.pathname).to.eq('/');
    });
  });

  it('should load the stopwatch page successfully', () => {
    cy.get('#link-to-stopwatch').click()
    cy.location().should((loc) => {
      expect(loc.pathname).to.eq('/times/stopwatch/');
    });
  });
});