#!/usr/bin/env python3.7

import random
from user import User
from credentials import Credentials

def create_user(platform, fname, lname, uname, pword):
    '''
    Function to create a new user
    '''
    new_user = User(platform, fname, lname, uname, pword)
    return new_user


def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()


def del_user(ind):
    '''
    Function to delete a user
    '''
    Credentials.delete_user(ind)


def display_credentials():
    '''
    Function that returns all saved users
    '''
    return Credentials.display_credentials()


def main():
    print('\n')
    print('Hello! Welcome to  Your Password Locker. What is your name?')
    name = input()
    print('\n')
    print(f'Welcome, {name}. What would you like to do today?')
    

    while True:
        print('\n')
        print('Use the following short codes to tell us how to help you: cc - refer to the  existing credentials, ca - create new account on a new platform and have credentials saved here, dc - dislpay the credentials, del - delete existing credentials, ex - exit the application')
        print('\n')
        short_code = input().lower()

        if short_code == 'cc':
            print("-"*16)
            print("Existing Account")
            print("-"*16)

            print('Platform on which existing account is categorized: (e.g. Instagram, Twitter, etc.)')
            platform = input()

            print ("First name registered on existing account:")
            firstname = input()

            print ("Last name registered on existing account:")
            lastname = input()

            print('Username registered on existing account:')
            username = input()

            print('Password registered on existing account: (Your password is secure with the password manager)')
            password = input()

            save_user(create_user(platform, firstname, lastname, username, password))
            print ('\n')
            print(f"New Credentials for {platform} ( {username} ), created")
            print ('\n')


        elif short_code == 'ca':
            print("-"*11)
            print("New Account")
            print("-"*11)

            print('Platform on which new account will be categorized: (e.g. Telegram,, Instagram, Snapchat, etc.) ')
            platform = input()

            print ("First name:")
            firstname = input()

            print ("Last name:")
            lastname = input()

            print('Prefered username:')
            username = input()

            print('\n')
            print('-'*35)
            print('Password Generation for new account:')
            print('-'*35)
            

            print('\n')
            print('Use the following short codes to tell us if you would like to set your own password or if you would like a generated password: rg - your own password, gp -  generated password')
            print('\n')
            passcode = input().lower()

            if passcode == 'rg':
                print('\n')
                print('Kindly enter your prefered password: (Your password is secure with us)')
                password = input()
                print('\n')
                print('Password stored successfully')
                print("Account setup complete")

            elif passcode == 'gp':
                    print('\n')
                    password = random.randint(87677,110465)
                    print('\n')
                    print("Password setup is SUCCESSFUL!")
                    print("Account setup complete")

            else:
                print('\n')
                print("I really didn't get that. Please use the short codes")
            

            save_user(create_user(platform, firstname, lastname, username, password))
            print('\n')

        elif short_code == 'del':
            print("-"*14)
            print("Delete Account")
            print("-"*14)

            print('Kindly enter the name of the platform to be deleted:')
            del_platform = input()

            print('Kindly enter username of account to be deleted:')
            del_username = input()

            if del_username and del_platform :
                found_credentials = Credentials.find_credential(del_platform,del_username)
                
                if found_credentials:
                    print('\n')
                    print(f'The following account is going to be permanetly deleted => {found_credentials.platform}:{found_credentials.username}')
                    print('\n')

                    del_user(found_credentials)

                else:
                    print('\n')
                    print("Credentials  are not available")
                    print('\n')

        
        elif short_code == 'dc ':
            print("-"*16)
            print(" Display the Credentials")
            print("-"*16)

            if display_credentials():
                print('\n')
                print("Here is a list of all your credentials:")
                print('\n')

                for user in display_credentials():
                    
                    print(f'{user.platform} account, Username: {user.username}, Password : {user.password}')
                    

            else:
                print('\n')
                print("You dont seem to have any saved  credentials  yet")
                print('\n')

        elif short_code == "ex":
            print('\n')
            print("THANK YOU FOR DROPPING IN !!!")
            print('\n')
            break

        else:
            print('\n')
            print("I really didn't get that. Please use the short codes")
            print('\n')
        

if __name__ == '__main__':
    main()
