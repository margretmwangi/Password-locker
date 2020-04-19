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