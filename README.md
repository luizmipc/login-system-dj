# Login System in Django
The current project is nearly complete, with user CRUD operations and authentication features fully implemented. However, there's still room to enhance the permissions system for better control over page access.

Looking ahead, my next goal is to start a new project focused on integrating social authentication, allowing users to log in using popular platforms like LinkedIn, GitHub, Google, and others.


## Resources
To not track files in git
- https://www.toptal.com/developers/gitignore

## References
To create the Django Custom User Model
- [Django Custom User Model - LearnDjango](https://learndjango.com/tutorials/django-custom-user-model)

- To future validate phonenumbers
- https://github.com/google/libphonenumber

I learned how complex is to normalize the address class.
- https://stackoverflow.com/questions/42923563/normalization-of-an-address-table-advice-needed

To make the footer stay at the bottom
- https://stackoverflow.com/questions/75360163/vertical-align-a-footer-to-the-bottom-of-the-page-bootstrap-5

To make the navbar 
- https://getbootstrap.com/docs/5.3/examples/offcanvas-navbar/

## Current challenge
I want to create a login system where users can belong to different groups, have different fields, and have different permissions.
- To solve:
- Create a Custom User using AbstractBaseUser
* Create groups of users.
- Create permissions for those groups
- Create proxy models that represent the groups of users.
* https://stackoverflow.com/questions/55263412/django-registering-two-different-types-of-users-with-different-fields
* https://stackoverflow.com/questions/65795812/is-it-possible-in-django-to-have-2-different-types-of-users-with-theirs-own-logi
* https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#specifying-a-custom-user-model