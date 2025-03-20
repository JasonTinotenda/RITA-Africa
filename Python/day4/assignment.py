password = input("Please enter your password: ")
has_uppercase = any((char.isupper() for char in password))
has_lowercase = any((char.islower() for char in password))
has_digit = any((char.isdigit() for char in password))
has_special = any((not char.isalnum() for char in password))

#Check if the password meets the criteria
if len(password) >= 8 and has_uppercase and has_lowercase and has_digit and has_special:
    print("Password is strong")
else:
    print("Password is weak")