Cypress.Commands.add("signup", (username, email, password) => {
  // Visit the signup page
  cy.visit('/accounts/signup/');
  
  // Fill out the signup form
  cy.get('#id_username').type(username);
  cy.get('#id_email').type(email);

  // Convert MM/DD/YYYY to YYYY-MM-DD format
  const date = '12311990'; // MMDDYYYY
  const formattedDate = `${date.slice(4, 8)}-${date.slice(0, 2)}-${date.slice(2, 4)}`; // YYYY-MM-DD
  cy.get('#id_date_of_birth').type(formattedDate);

  // Fill out password fields
  cy.get('#id_password1').type(password);
  cy.get('#id_password2').type(password);

  // Submit the signup form
  cy.get('#submit_signup').click();
});

Cypress.Commands.add("login", (email, password) => {
  // Visit the login page
  cy.visit('/accounts/login/');
  cy.get('#id_username').type(email);
  cy.get('#id_password').type(password);

  // Submit the login form
  cy.get('#submit_login').click();
});