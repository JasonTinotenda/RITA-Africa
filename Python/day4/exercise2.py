stored_username = "admin"
stored_password = "password"

def login () :
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    # Check if the username and password are correct
    if username == stored_username and password == stored_password:
        print("Welcome, admin!")
    else :
        print("Invalid username or password. Please try again.")
        login()

login()