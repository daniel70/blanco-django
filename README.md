# blanco-django

This is an empty django project that I use as a template for new projects.
I has a simple home page and will use the following packages (it's a work in progress):
- 2fa
- bootstrap
- django-debug-toolbar

It has one app called common that holds the user model.
The user model uses an email address to login (instead of a username).

Features:
- login / logout functionality
- django messages framework

#### TODO:
1) the first migration should install postgres extensions
2) implement 2FA
