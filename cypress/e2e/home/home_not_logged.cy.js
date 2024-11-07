describe('Home app tests not logged in', () => {
  beforeEach(() => {
    cy.visit('');
  });

  it('should load the login page', () => {
    cy.get('#link-to-login').click()
    cy.location().should((loc) => {
      expect(loc.pathname).to.eq('/accounts/login/');
    });
  });

  it('should load the page signup page', () => {
    cy.get('#link-to-signup').click()
    cy.location().should((loc) => {
      expect(loc.pathname).to.eq('/accounts/signup/');
    });
  });

  it('should load the home page', () => {
    cy.get('#link-to-home').click()
    cy.location().should((loc) => {
      expect(loc.pathname).to.eq('/');
    });
  });

  it('should load the login page instead of stopwatch', () => {
    cy.get('#link-to-stopwatch').click()
    cy.location().should((loc) => {
      expect(loc.pathname).to.eq('/accounts/login/');
    });
  });
});