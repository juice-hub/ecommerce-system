from io_interface import IOInterface
from operation_admin import AdminOperation


def login_control():
    from io_interface import IOInterface
    io_login_instance = IOInterface()
    io_login_instance.io_login()


def customer_control():
    print("Customer control is under development.")

def admin_control():
    from operation_admin import AdminOperation
    admin_operation = AdminOperation("data/users.txt")
    print("\nTo login as admin, provide the admin credentials below.")
    print("For the customer interface, enter any other input to bypass admin login.\n")
    user_name = input("Enter admin username: ")
    user_password = input("Enter admin password: ")

    admin_operation.register_admin(user_name, user_password)

def main():
    # main() starts with a prompt for admin login upon every startup, by calling admin_control()
    admin_control()
    io_interface = IOInterface()
    while io_interface.main_menu():
        pass  # This will keep displaying the main menu until the user chooses to quit.

if __name__ == "__main__":
    main()


