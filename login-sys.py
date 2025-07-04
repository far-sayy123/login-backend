from colorama import Fore
from tqdm import tqdm
import time
import os



# og_username = ""
# og_password = ""


# this func will be used only for Validating
def login(username, password):


    # reading the credentials file
    try:
        storage = open(f"credentials/{username}.txt", "r")
        credentials = storage.readlines() # ["user123\n", "pass123"]
        og_username = credentials[0] # user123\n
        og_password = credentials[1] # pass123

        og_username = og_username.replace("\n", "")


         # validation logic
        if username == og_username and password == og_password:
            Home(user=username, status="login")
        elif user_username == og_username and password != og_password:
            return "Username matched but password is incorrect"
        elif user_password == og_password and user_username != og_username:
            return "Password matched but Username is incorrect"
        elif user_username != og_username and password != og_password:
            return "Credentials are wrong"
        else:
            return "Something went wrong"
        
    except:
        print("Sorry, Your acc doesnt exist! Please Register first")



   
    
def register(username, password):
    # 1. create the file to store data
    open(f"credentials/{username}.txt", "x")

    # 2. store data into the created file
    storage = open(f"credentials/{username}.txt", "a")
    storage.write(username + "\n")
    storage.write(password)

    # send to Home page
    Home(user=username, status="register")


# this func will be called when LOGIN IS SUCCESSFUL
def Home(user, status):
    for i in tqdm(range(1, 10)):
        time.sleep(0.1)
    
    if status == "login":
        print(Fore.GREEN + f"WELCOME BACK {user} TO THE HOME PAGE")
    else:
        print(Fore.GREEN + f"Signin Successfull, Welcome {user} to our website :)")


    print("This is my content bro")

    logout = input("Logout?")

    if logout == "y" or logout == "yes":
        print("logging out...")
        os._exit(status=1)
    else:
        print("ok 🙂")
        Home(user=user, status=status)
    



while True:
    print("Choose one")
    print("1. Login")
    print("2. Register")

    user = int(input(">> "))

    
    if user == 1:
        print("Login page")
        user_username = input("Enter Username: ")
        user_password = input("Enter Password: ")

        x= login(username=user_username, password=user_password)

        print(x)

    
    elif user == 2:
        print("Signup page")
        user_username = input("Enter Username: ")
        user_password = input("Enter Password: ")
        x= register(username=user_username, password=user_password)

        print(x)


    else:
        print("Sorry, invalid input")
       



    