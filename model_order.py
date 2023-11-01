from datetime import datetime

class Order:
    def __init__(self, order_id=None, user_id=None, pro_id=None,
                 order_time=datetime.strptime("00-00-0000_00:00:00", "%d-%m-%Y_%H:%M:%S")):
        self.order_id = order_id
        self.user_id = user_id
        self.pro_id = pro_id
        self.order_time = order_time

    def __str__(self):
        formatted_order_time = self.order_time.strftime("%d-%m-%Y_%H:%M:%S")
        return (
            f"{{'order_id':'{self.order_id}', 'user_id':'{self.user_id}', "
            f"'pro_id':'{self.pro_id}', 'order_time':'{formatted_order_time}'}}"
        )