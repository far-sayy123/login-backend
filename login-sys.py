from colorama import Fore
from tqdm import tqdm
import time



og_username = ""
og_password = ""


# this func will be used only for Validating
def login(username, password):
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
    
def register(username, password):
    global og_username
    global og_password

    og_username =  username
    og_password = password

    Home(user=og_username, status="register")


# this func will be called when LOGIN IS SUCCESSFUL
def Home(user, status):
    for i in tqdm(range(1, 10)):
        time.sleep(0.1)
    
    if status == "login":
        print(Fore.GREEN + f"WELCOME BACK {user} TO THE HOME PAGE")
    else:
        print(Fore.GREEN + f"Signin Successfull, Welcome {user} to our website :)")
    



while True:
    print("Choose one")
    print("1. Login")
    print("2. Register")

    user = int(input(">> "))

    
    if user == 1:
        print("Login page")
        user_username = input("Enter Username")
        user_password = input("Enter Password")

        x= login(username=user_username, password=user_password)

        print(x)

        

   
    elif user == 2:
        print("Signup page")
        user_username = input("Enter Username")
        user_password = input("Enter Password")
        x= register(username=user_username, password=user_password)

        print(x)

       



    