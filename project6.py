import random
import string

def generate_random_password(length=12):
    """
    Generates a random password of a specified length, consisting of 
    lowercase letters, uppercase letters, and numbers.
    
    Args:
        length (int): The desired length of the password. Defaults to 12.

    Returns:
        str: The randomly generated password.
    """
   
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    
    password_list = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits)
    ]
    
    for _ in range(length - 3):
        password_list.append(random.choice(characters))
        
   
    random.shuffle(password_list)
   
    password = "".join(password_list)
    
    return password
new_password = generate_random_password(16)
print(f"Generated Password: {new_password}")
default_password = generate_random_password()
print(f"Generated Default Password: {default_password}")
