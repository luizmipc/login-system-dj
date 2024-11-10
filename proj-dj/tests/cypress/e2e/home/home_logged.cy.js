describe('Home app tests logged in', function () {
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
  });

  it('should load the login page successfully', () => {
    cy.get('#link-to-login').click();
    cy.location().should((loc) => {
      expect(loc.pathname).to.eq('/');
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

  it('should load the profile detail page successfully', function () {
    cy.get('#link-to-profile').click()
    cy.location().should((loc) => {
      expect(loc.pathname).to.eq(`/accounts/profile/${this.USERNAME}/`)
    });
    cy.get('#id_username').should('have.text', this.USERNAME);
    cy.get('#id_email').should('have.text', this.EMAIL);
    const date = '12311990'; // MMDDYYYY
    const formattedDate = `${date.slice(0, 2)}/${date.slice(2, 4)}/${ date.slice(4, 8)}`; // YYYY-MM-DD
    cy.get('#id_date_of_birth').should('have.text', formattedDate);
  })
});