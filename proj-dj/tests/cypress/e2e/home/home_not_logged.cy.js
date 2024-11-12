describe('Home app tests not logged in', () => {
  beforeEach(() => {
    cy.visit('');
  });

  it('should load the login page successfully', () => {
    cy.get('#link-to-login').click()
    cy.location().should((loc) => {
      expect(loc.pathname).to.eq('/accounts/login/');
    });
    cy.get('form[name="login"]').should('exist');
  });

  it('should load the page signup page successfully', () => {
    cy.get('#link-to-signup').click()
    cy.location().should((loc) => {
      expect(loc.pathname).to.eq('/accounts/signup/');
    });
    cy.get('form[name="signup"]').should('exist');
  });

  it('should load the home page successfully', () => {
    cy.get('#link-to-home').click()
    cy.location().should((loc) => {
      expect(loc.pathname).to.eq('/');
    });
  });
});