import os
from operation_user import UserOperation
from model_admin import Admin


class AdminOperation:
    def __init__(self, file_path=None):
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = 'data/users.txt'


    def print_file_contents(self):
        try:
            with open(self.file_path, 'r') as file:
                contents = file.read()
                print(contents)
        except Exception as e:
            print(f"An error occurred: {e}")

    def register_admin(self, user_name, user_password):
        # Check if the admin account already exists
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                for line in file:
                    try:
                        user_data = eval(line.strip())
                    except SyntaxError:
                        continue

                    if user_name == user_data.get('user_name') and user_data.get('user_role') == 'admin':
                        print(f"\nWelcome, {user_data['user_name']}! You are logged in as {user_data['user_role']}.")
                        from io_interface import IOInterface
                        IOInterface.admin_menu()
                        return True

                    print("\nIncorrect/non-existent admin credentials.")
                    print("\nProceeding to the Systems' main menu...")
                    return False

