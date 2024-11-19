# 0x03-user_authentication_service
Create a user validation system mapped to the database. Handles creating users, validating their logins/credentials

## user.py
User class and sqlalchemy mappings

## auth.py
Authenticating of users and encrypting user logins

## db.py
Database for storing and retrieving user objects

## app,py
A simple flask app utilizing the above moodules to create a login interface
