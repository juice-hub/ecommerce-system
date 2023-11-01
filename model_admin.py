import time
from model_user import User  # Import User class from model_user.py file


class Admin(User):
    def __init__(self, user_id, user_name, user_password, user_register_time=None, user_role="admin"):
        if user_register_time is None:
            user_register_time = time.strftime("00-00-00_00:00:00", time.localtime())
        else:
            # Ensure the given time string is in the expected format
            time.strptime(user_register_time, "%d-%m-%Y_%H:%M:%S")

        User.__init__(self, user_id, user_name, user_password, user_register_time, user_role)

    def __str__(self):
        return (
            f"{{'user_id':'{self.user_id}', 'user_name':'{self.user_name}', "
            f"'user_password':'{self.user_password}', 'user_register_time':'{self.user_register_time}', "
            f"'user_role':'{self.user_role}'}}"
        )

# Test creating an admin instance and printing it, see below:
# try:
#     admin = Admin("u_1234567891", "Bob", "adminpassword")
#     print(admin)
# except ValueError as e:  # Adjust the exception type as needed
#     print(e)
