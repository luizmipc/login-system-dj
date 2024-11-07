
Cypress.Commands.add('signupUser', (username, email, password) => {
  cy.get('#id_username').type('teste');
  cy.get('#id_email').type('teste@example.com');
  cy.get('#id_date_of_birth').type('12311990');
  cy.get('#id_password1').type('1234567890#Kl');
  cy.get('#id_password2').type('1234567890#Kl');
});