from model_user import User


class Customer(User):
    def __init__(self, user_id, user_name, user_password, user_email, user_mobile,
                 user_register_time="00-00-0000_00:00:00", user_role="customer"):
        User.__init__(self, user_id, user_name, user_password, user_register_time, user_role)
        self.user_email = user_email
        self.user_mobile = user_mobile

    def __str__(self):
        return (
            f"{{'user_id':'{self.user_id}', 'user_name':'{self.user_name}', "
            f"'user_password':'{self.user_password}', 'user_register_time':'{self.user_register_time}', "
            f"'user_role':'{self.user_role}', 'user_email':'{self.user_email}', "
            f"'user_mobile':'{self.user_mobile}'}}")


# Creating a customer object
try:
    customer = Customer("u_1234567890", "Alice", "password123", "alice@email.com", "04123456789")
except ValueError as e:
    print(e)
