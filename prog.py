from colorama import Fore
from tqdm import tqdm
import time
import os


def login(username, password):
    try:
        storage = open(f"credentials/{username}.txt", "r")
        credentials = storage.readlines()  # ["user123\n", "pass123"]
        storage.close()
        og_username = credentials[0].replace("\n", "")
        og_password = credentials[1]

        if username == og_username and password == og_password:
            Home(user=username, status="login")
        elif username == og_username and password != og_password:
            return "Username matched but password is incorrect"
        elif password == og_password and username != og_username:
            return "Password matched but Username is incorrect"
        elif username != og_username and password != og_password:
            return "Credentials are wrong"
        else:
            return "Something went wrong"

    except FileNotFoundError:
        print("Sorry, Your acc doesnt exist! Please Register first")


def register(username, password):
    # Check if credentials folder exists, if not create it
    if not os.path.exists("credentials"):
        os.makedirs("credentials")

    # Check if user already exists
    if os.path.exists(f"credentials/{username}.txt"):
        print(Fore.RED + "User already exists! Please login instead.")
        return

    # Create the file to store data
    open(f"credentials/{username}.txt", "x").close()

    # Store data into the created file
    storage = open(f"credentials/{username}.txt", "a")
    storage.write(username + "\n")
    storage.write(password)
    storage.close()

    print(Fore.GREEN + f"Registration successful! Welcome {username} :)")

    # Send to Home page
    Home(user=username, status="register")


def Home(user, status, show_loading=True):
    if show_loading:
        for i in tqdm(range(1, 10)):
            time.sleep(0.1)
    
    if status == "login":
        print(Fore.GREEN + f"WELCOME BACK {user} TO THE HOME PAGE")
    else:
        print(Fore.GREEN + f"Signin Successful, Welcome {user} to our website :)")

    print("This is my content bro")

    logout = input("Logout? ")

    if logout.lower() in ["y", "yes"]:
        print("logging out...")
        os._exit(status=0)
    else:
        print("ok 🙂")
        # Call Home again without loading next time
        Home(user=user, status=status, show_loading=False)


while True:
    print("Choose one")
    print("1. Login")
    print("2. Register")

    user = int(input(">> "))

    if user == 1:
        print("Login page")
        user_username = input("Enter Username: ")
        user_password = input("Enter Password: ")

        x = login(username=user_username, password=user_password)
        if x:
            print(x)

    elif user == 2:
        print("Signup page")
        user_username = input("Enter Username: ")
        user_password = input("Enter Password: ")
        register(username=user_username, password=user_password)

    else:
        print("Sorry, invalid input")
