import random
import string


import ast  # Import the ast module

class UserOperation:
    def __init__(self):
        self.users = {}
        self.user_id = None
        self.user_password = None
        self.user_role = None
        self.user_registered_time = None
        with open('data/users.txt', 'r') as file:
            for line in file:
                if line.strip():
                    user_data = ast.literal_eval(line.strip())  # Parse the dictionary-like string
                    self.users[user_data['user_name']] = user_data  # Add the user data to the users dictionary

    def generate_unique_user_id(self):
        self.user_id = 'u_' + ''.join(random.choices(string.digits, k=10))
        return self.user_id

    def encrypt_password(self, user_password: str) -> str:
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choices(characters, k=2 * len(user_password)))

        encrypted_password_list = ["^^"]
        for i in range(len(user_password)):
            encrypted_password_list.append(random_string[2 * i:2 * (i + 1)])
            encrypted_password_list.append(user_password[i])
            encrypted_password_list.append("$$")

        encrypted_password = ''.join(encrypted_password_list)
        return encrypted_password

    def decrypt_password(self, encrypted_password: str) -> str:
        decrypted_password = encrypted_password[4:-2:4]  # Extracting the original password characters
        return decrypted_password

    def check_username_exist(self, user_name):
        return user_name in self.users

    def validate_username(self, user_name: str) -> bool:
        return user_name.isidentifier() and len(user_name) >= 5

    def validate_password(self, user_password: str) -> bool:
        has_letter = any(c.isalpha() for c in user_password)
        has_digit = any(c.isdigit() for c in user_password)
        return has_letter and has_digit and len(user_password) >= 5

    def login(self, user_name, user_password):
        with open("data/users.txt", "r") as f:
            for line in f:
                try:
                    details = eval(line.strip())
                    if (details['user_name'] == user_name and details['user_password'] == user_password):
                        return True, details, details
                except SyntaxError:
                    continue
        return False, None, None
