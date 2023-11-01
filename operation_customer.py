import re
import time
import os

from operation_user import UserOperation
from model_customer import Customer


FILE_PATH = 'data/users.txt'


class CustomerOperation:
    def validate_email(self, user_email: str):
        pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
        return bool(pattern.fullmatch(user_email))

    def validate_mobile(self, user_mobile: str):
        pattern = re.compile(r'^(04|03)\d{8}$')
        return bool(pattern.fullmatch(user_mobile))

    def register_customer(self, user_name, user_password, user_email, user_mobile):
        user_operation = UserOperation()

        # Validate user information
        if not (user_operation.validate_username(user_name) and
                user_operation.validate_password(user_password) and
                self.validate_email(user_email) and
                self.validate_mobile(user_mobile)):
            return False

        if user_operation.check_username_exist(user_name):
            return False

        user_id = user_operation.generate_unique_user_id()
        register_time = time.strftime("%d-%m-%Y_%H:%M:%S", time.localtime())

        new_customer = Customer(user_id, user_name, user_password, user_email, user_mobile, register_time)

        # Append new customer info to data/users.txt
        with open('data/users.txt', 'a') as file:
            file.write(str(new_customer) + '\n')

        return True

    def update_profile(self, attribute_name, value, customer_object):
        if attribute_name == "user_name" and not UserOperation().validate_username(value):
            return False
        elif attribute_name == "user_password" and not UserOperation().validate_password(value):
            return False
        elif attribute_name == "user_email" and not self.validate_email(value):
            return False
        elif attribute_name == "user_mobile" and not self.validate_mobile(value):
            return False

        # Update the attribute value
        customer_object[attribute_name] = value

        # Update the record in the data/users.txt file
        customers = []
        with open('data/users.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == customer_object['user_id']:
                    data = [str(getattr(customer_object, attr)) for attr in data[0].split(',')]
        customers.append(','.join(data))

        # Read the current records
        with open('data/users.txt', 'r') as file:
            customers = file.readlines()

        # Update the specific customer's record in memory
        updated_customers = []
        for customer in customers:
            data = customer.strip().split(',')
            if data[0] == customer_object['user_id']:  # Assuming customer_object is a dictionary
                setattr(customer_object, attribute_name, value)
                updated_customers.append(','.join([str(getattr(customer_object, attr)) for attr in data]))
            else:
                updated_customers.append(customer)

        # Write the updated records back to the file
        with open('data/users.txt', 'w') as file:
            file.write('\n'.join(updated_customers))

        return True

    def delete_customer(self, user_id):
        with open('data/users.txt', 'r') as file:
            customers = file.readlines()

        with open('data/users.txt', 'w') as file:
            is_deleted = False
            for customer in customers:
                if customer.split(',')[0] != user_id:
                    file.write(customer)
                else:
                    is_deleted = True

            return is_deleted

    @staticmethod
    def parse_dict_string(s):
        items = s.strip('{}').split(',')
        result = {}
        for item in items:
            key, value = item.split(':')
            result[key.strip("'")] = value.strip("'")
        return result

    def get_customer_list(self, page_number):
        with open('data/users.txt', 'r') as file:
            lines = file.readlines()
            all_users = [Customer(**self.parse_dict_string(line.strip())) for line in lines]
        # Filtering for customer users only
        customer_users = [user for user in all_users if user.user_role == 'customer']
        # Calculating total pages
        total_pages = -(-len(customer_users) // 10)
        # Getting the start and end index for the given page
        start_index = (page_number - 1) * 10
        end_index = min(start_index + 10, len(customer_users))
        paged_customers = customer_users[start_index:end_index]
        print("Paged Customers:", paged_customers)
        print("Page Number:", page_number)
        print("Total Pages:", total_pages)
        # Return the results
        return paged_customers, page_number, total_pages

    def generate_test_customer_data(self):
        with open('data/users.txt', 'a') as file:
            for i in range(10):
                user_name = f"user_{i}"
                user_password = f"pass_{i}"
                user_email = f"user_{i}@test.com"
                user_mobile = f"12345678{i}"

                user_id = UserOperation.generate_unique_user_id(self)
                register_time = time.strftime("%d-%m-%Y_%H:%M:%S", time.localtime())
                new_customer = Customer(user_id, user_name, user_password, user_email, user_mobile, register_time)
                # Append new customer info to data/users.txt
                file.write(str(new_customer) + '\n')

    def delete_all_customers(self):
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'r') as file:
                lines = file.readlines()
            non_customers = [line for line in lines if eval(line.strip()).get('user_role') != 'customer']
            with open(FILE_PATH, 'w') as file:
                file.writelines(non_customers)
            return True
        else:
            print(f"The file {FILE_PATH} does not exist.")
            return False
