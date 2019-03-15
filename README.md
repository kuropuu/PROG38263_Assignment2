# PROG38263 Assignment 2: Pastebin Clone
Coded by Joanne Pham (@kuropuu) & Julie Mai (@juuliemai)

### Requirements
This web application requires:
* Python 3
* Django 2.0+
* Virtualenv
* pip
* Crispy Forms
* SQLite3
* django-upload-validator

### Installation of Add-Ons
Install Crispy Forms by running `pip install django-crispy-forms`.

### Security Features
We implemented the following security features into our web app:
* Web app is served over HTTPS
* Secure authentication and authorization scheme
* Passwords are hashed in the database
* File uploads are validated to only allow .txt files
* Django requires the csrf_token to be defined for all forms to protect 
against CSRF attacks
* XSS protection is enabled by adding autoescape tags on the base.html file, but is also built into Django with the SecurityMiddleware module
* Django provides protection against SQL injection attacks, along with clickjacking

### Note about reset password function
We did not implement a SMTP server since this is only for development purposes. 
We sent the emails to a folder in the project's home directory called "emails." 
If you are trying to reset your password, simply type in the email address 
associated with your account and then open the corresponding file in the "emails" 
directory. Copy and paste the URL into your web browser to reset your password.
