import os

from operation_customer import CustomerOperation
from opreation_product import ProductOperation
from operation_order import OrderOperation


class IOInterface:

    def __init__(self):
        self.customer_operation = CustomerOperation()

    def main_menu(self):
        while True:
            print("\nWelcome to the E-Commerce System!\n__________________________________")
            print("(1) Login\n(2) Register\n(3) Quit\n__________________________________")
            try:
                choice = int(input("\nPlease choose an option from the menu. "
                                   "If you are an existing customer, select 1 to login."
                                   "\nTo register an account with us, select 2. To quit, select 3: "))

                if choice == 1:
                    from main import login_control  # Delayed import
                    login_control()

                elif choice == 2:
                    print("\n\nLet's get you registered in the E-Commerce System!")
                    print("Follow the prompts below to create an account with us.\n")
                    user_name = input("Enter username: ")
                    user_password = input("Enter password: ")
                    user_email = input("Enter email: ")
                    user_mobile = input("Enter mobile: ")

                    self.customer_operation.register_customer(user_name, user_password, user_email, user_mobile)
                    print("\nYou have successfully registered!")
                    print("Login with your registered details to continue using the E-Commerce System.")
                    print("\n__________________________________")
                    from main import login_control  # Delayed import
                    login_control()

                elif choice == 3:
                    print("\nThank you for using the E-Commerce System!")
                    return False

                else:
                    print("\nInvalid option, please try again.")
                    continue

            except ValueError:
                print("\nPlease enter a valid number.")

    @staticmethod
    def admin_menu(self=None):
        while True:  # This will keep displaying the admin menu when an admin account has successfully logged in.
            options = [
                "\n(1) Show products",
                "(2) Add customers",
                "(3) Show customers",
                "(4) Show orders",
                "(5) Generate test data",
                "(6) Generate all statistical figures",
                "(7) Delete all data",
                "(8) Logout"
            ]
            print("\nAdmin menu\n__________________________________")
            print("\n".join(options))

            try:
                admin_steps = int(input("\nWhat would you like to do? "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            try:
                if admin_steps == 1:
                    show_products_to_admin = IOInterface()
                    show_products_to_admin.show_products()

                elif admin_steps == 2:
                    print("\nLet's add a customer to the system! Please provide the required information, following the prompts below:")
                    user_name = input("Enter new customer's username: ")
                    user_password = input("Enter password for new customer: ")
                    user_email = input("Enter email of new customer: ")
                    user_mobile = input("Enter new customer''s mobile number: ")

                    add_customer = CustomerOperation()
                    add_customer.register_customer(user_name, user_password, user_email, user_mobile)
                    print(f"\nYou have successfully registered {user_name}! as a customer in the E-Commerce System!")

                elif admin_steps == 3:
                    print("\nList of Customers in the E-Commerce System:\n____________________________________________")
                    customer_list_instance = IOInterface()
                    customer_list_instance.show_customers_only()

                elif admin_steps == 4:
                    show_orders_to_admin = OrderOperation()
                    orders, current_page, total_pages = show_orders_to_admin.get_order_list(customer_id='', page_number=1)
                    if not orders:
                        print("There are currently no orders in the E-Commerce System.")
                    else:
                        for order in orders:
                            print(f"Order details: {order}")
                    print(f"Page {current_page} of {total_pages+1}")

                elif admin_steps == 5:
                    IOInterface.generate_all_test_data(self)

                elif admin_steps == 6:
                    consumption_data = OrderOperation()  # Creating an instance of the OrderOperation class
                    consumption_data.generate_all_customers_consumption_figure()

                elif admin_steps == 7:
                    data_manager = IOInterface()
                    data_manager.delete_all_data()
                    print("\nAll customer and order data have been deleted!")

                elif admin_steps == 8:
                    print("\nYou have logged out as an admin user.")
                    break

                else:
                    print("\nInvalid selection. You can onlu enter a number between 1-8. Try again.")

            except Exception as e:
                print(f"An error occurred: {e}")

    def customer_menu(self, user_details):
        while True:  # This will keep displaying the customer menu
            customer_options = [
                "\n(1) Show profile",
                "(2) Update profile",
                "(3) Show products",
                "(4) Show history orders",
                "(5) Generate all consumption figures",
                "(6) Logout"
            ]
            print("\nCustomer menu\n__________________________________")
            print("\n".join(customer_options))

            try:
                customer_steps = int(input("\nWhat would you like to do? "))

                if customer_steps == 1:
                    self.show_user_details(user_details)

                elif customer_steps == 2:
                    self.update_user_menu(user_details)

                elif customer_steps == 3:
                    self.show_products()

                elif customer_steps == 4:
                    order_op_instance = OrderOperation()
                    orders_data = order_op_instance.get_order_list(user_details['user_id'],1)
                    self.show_list(user_details['user_role'], 'Order', orders_data)

                elif customer_steps == 5:
                    order_op = OrderOperation()  # Creating an instance of the OrderOperation class
                    order_op.generate_single_customer_consumption_figure(user_details['user_id'])

                elif customer_steps == 6:
                    print("\nLogging you out...")
                    print("You are now logged out!")
                    print("Taking you back to the main menu...")
                    break  # This will break the loop, effectively logging the user out

                else:
                    print("Invalid option, please try again.")

            except ValueError:
                print("Please enter a valid number.")

    def show_user_details(self, details):
        print("\nUser Details:\n______________")
        print(f"User ID:{details['user_id']}")
        print(f"Username:{details['user_name']}")
        print(f"User password: {details['user_password']}")
        print(f"User registration time: {details['user_register_time']}")
        print(f"User role: {details['user_role']}")
        print(f"User email: {details['user_email']}")
        print(f"User mobile: {details['user_mobile']}")

    def update_user_menu(self, user_details):
        while True:
            print("\nWhat would you like to update?")
            print("1. Username")
            print("2. Password")
            print("3. Email")
            print("4. Mobile")
            print("5. Go back")

            try:
                choice = int(input("\nEnter your choice: "))

                if choice == 1:
                    new_value = input("Enter new username: ")
                    attribute_name = "user_name"

                elif choice == 2:
                    new_value = input("Enter new password: ")
                    attribute_name = "user_password"

                elif choice == 3:
                    new_value = input("Enter new email: ")
                    attribute_name = "user_email"

                elif choice == 4:
                    new_value = input("Enter new mobile: ")
                    attribute_name = "user_mobile"

                elif choice == 5:
                    return

                else:
                    print("Invalid choice. Try again.")
                    continue

                customer_op_instance = CustomerOperation()
                if customer_op_instance.update_profile(attribute_name, new_value, user_details):
                    print(f"{attribute_name.replace('_', ' ').capitalize()} updated successfully!")
                else:
                    print(f"Failed to update {attribute_name.replace('_', ' ').capitalize()}. Please try again.")

            except ValueError:
                print("Please enter a valid number.")

    def show_products(self):
        product_op = ProductOperation()
        products = product_op.get_product_list(1)  # Assuming page 1 for now
        if products is None:
            print("No products available.")
            return

        print("\nList of Products:\n_________________")
        for product in products:
            print(
                f'ID: {product['pro_id']}, '
                f'Name: {product['pro_name']}, '
                f'Price: {product['pro_current_price']}, '
                f'Likes: {product['pro_likes_count']}')

    @staticmethod
    def show_list(user_role: str, list_type: str, data: dict):
        if user_role == 'admin' or (user_role == 'customer' and list_type in ['Product', 'Order']):

            print(f"--- {list_type} List ---")

            # Access the items list using the 'items' key and iterate over it
            items_list = data.get('items', [])
            for index, item in enumerate(items_list, start=1):
                print(f"{index}. {item}")

            # Access the current page and total pages using their respective keys
            current_page = data.get('current_page', 1)  # default to 1 if not provided
            total_pages = data.get('total_pages', 1)  # default to 1 if not provided
            print(f"Page {current_page} of {total_pages}")

        else:
            print("You do not have permission to view this list.")

    def print_unsuccessful_login(self):
        print("Incorrect password. Try again.")

    def io_login(self):
        login_username = input("\nEnter your username: ")
        login_password = input("Enter your password: ")
        print(f"\nChecking existence for username: {login_username}")  # Printing the username being checked...

        from operation_user import UserOperation
        userop_login_instance = UserOperation()

        if userop_login_instance.check_username_exist(login_username):
            login_status, user_details, user_role = userop_login_instance.login(login_username, login_password)
            if login_status:
                print(f"Welcome {login_username}! You are logged in as {user_details['user_role']}.")
                self.customer_menu(user_details)

            else:
                from io_interface import IOInterface
                IOInterface.print_unsuccessful_login(self)
        else:
            print("User does not exist.")

    def show_customers_only(self):
        file_path = 'data/users.txt'
        with open(file_path, 'r') as file:
            lines = file.readlines()
        if not lines:
            print("\nThere are no customers in the system. To add a customer, select 2.")
            return
        for line in lines:
            user = eval(line.strip())
            if user.get('user_role') == 'customer':
                print(f"User id: {user['user_id']}, "
                      f"Username: {user['user_name']}, "
                      f"Email address: {user['user_email']}, "
                      f"Mobile number: {user['user_mobile']}")
            else:
                print("\nThere are no customers in the system. To add a customer, select 2.")
                return
        print("Page 1 of 1")

    def generate_all_test_data(self):
        customer_test_instance = CustomerOperation()
        order_test_instance = OrderOperation()
        customer_test_instance.generate_test_customer_data()
        order_test_instance.generate_test_order_data()
        print("\nTest data has been generated!")

    def delete_all_data(self):
        ORDER_FILE_PATH = 'data/orders.txt'
        USER_FILE_PATH = 'data/users.txt'
        if os.path.exists(ORDER_FILE_PATH):
            with open(ORDER_FILE_PATH, 'w') as file:
                pass
        else:
            print(f"The file {ORDER_FILE_PATH} does not exist.")
        if os.path.exists(USER_FILE_PATH):
            with open(USER_FILE_PATH, 'r') as file:
                lines = file.readlines()
            non_customers = [line for line in lines if eval(line.strip()).get('user_role') != 'customer']
            with open(USER_FILE_PATH, 'w') as file:
                file.writelines(non_customers)
        else:
            print(f"The file {USER_FILE_PATH} does not exist.")