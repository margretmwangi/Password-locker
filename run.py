#!/usr/bin/env python3.7
from user import Users

def create_user(uname,password):
    '''
    Function to create a new user
    '''
    new_user = Users(uname,password)
    return new_user

def save_users(user):
    '''
    Fuunction to save users
    '''
    user.save_user()

def generate_password():
    '''
    Function that generates a password
    '''
    def create_credential(uname, account, account_username, account_password):
    '''
    Function to create new credential
    '''
    new_credential = Credentials(uname, account, account_username, account_password)
    return new_credential

def save_credentials(credential):
    '''
    Function to save credentials
    '''
    credential.save_credential()

def del_credential(Credential):
    '''
    Function to delete credential
    '''
    

def display_credential():
    '''
    returns all the saved credentials
    '''
    return Credentials.display_credential()        
        