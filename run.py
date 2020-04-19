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
            
def main():
    print("Hello Welcome to your password locker.Please input your name...")
    
    user_name = input()
    
    print (f"Hello {user_name}. What would you like to do?")
    print('\n')
    
    while True:
        print("Use these short codes : ca -create an account, cc - create credentials, lg - log in to your account, dc - display credentials, ex - exit")
        
        short_code = input().lower()
        
        if short_code == "ca":
            print("New Account")
            print("-"*100)
            
            print("User name ....")
            uname = input()
            
            print("password ....")
            password = input()
            
            save_users(create_user(uname, password)) # create and save new user.
            print('\n')
            print(f"New account: username is {uname} and the password is {password}")
            print('\n')
            
        elif short_code == 'cc':
            print("Create new account credentials")
            print("-"*100)
            
            print("User name ....")
            uname = input()
            
            print("Account name ....")
            account = input()
            
            print("Account username .....")
            account_username = input()
            while True:
                print(' ')
                print("-"*60)
                print('Please use the short codes to choose an option to set a password: ep-enter a password gp-generate a password ex-exit') 
                psw_choice =input("Enter an option....")
                print("-"*60)
                if psw_choice == 'ep':
                    print(" ")
                    password =input("Enter your password.....")
                    break
                elif psw_choice == 'gp':
                    password = generate_password()
                    break
                elif psw_choice == 'ex':
                    break
                else:
                    print("please try again")
            
            save_credentials(create_credential(uname, account, account_username, password)) #create and save new credentials
            print('\n')
            print(f"New credentials for {uname} ,*{account}* account and the username for the account is *{account_username}* password **{password}**")
            print('\n')
            
        elif short_code == 'lg':
            print("-" *40)
            print('')
            print(f"Fill out your details to login to your account")  
            print("User name ....")
            uname = input()
        
            print("password ...")
            password = input()
            
            for user in Users.user_list:
                if user == uname:
                    print("You are already registered")
                else:
                    print("You are already logged in to the account")
                    break
                print('\n')
        elif short_code == 'dc':
            print('')      
            if display_credential():
                print("Here is all your credentials list ;")    .lower().strip()
                print(' ')
                for credential in display_credential():
                    print(f"Account name: {credential.account} , Account username: {credential.account_username} ,Password: {credential.password}")
                print(' ')    
            else:
                print(' ')
                print("There are no credentials saved")
                print(' ') 
                
        elif short_code == 'ex':
            print("Thank you for passing by see you again.......")
            break
        else:
            print("Please use the short codes provided")             
        
if __name__ == '__main__':
    main()        
        