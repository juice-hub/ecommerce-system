import time

class User:
    def __init__(self, user_id, user_name, user_password, user_register_time=None, user_role=''):
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_register_time = user_register_time if user_register_time else time.strftime("%d-%m-%Y_%H:%M:%S")
        self.user_role = user_role

    def __str__(self):
        return (
            f"{{'user_id':'{self.user_id}', 'user_name':'{self.user_name}', "
            f"'user_password':'{self.user_password}', 'user_register_time':'{self.user_register_time}', "
            f"'user_role':'{self.user_role}'}}"
        )


