class Product:
    def __init__(self, pro_id=None, pro_model=None, pro_category=None,
                 pro_name=None, pro_current_price=None, pro_raw_price=None,
                 pro_discount=None, pro_likes_count=None):
        self.pro_id = pro_id
        self.pro_model = pro_model
        self.pro_category = pro_category
        self.pro_name = pro_name
        self.pro_current_price = pro_current_price
        self.pro_raw_price = pro_raw_price
        self.pro_discount = pro_discount
        self.pro_likes_count = pro_likes_count

    def __str__(self):
        return (
            f"{{'pro_id':'{self.pro_id}', 'pro_model':'{self.pro_model}', "
            f"'pro_category':'{self.pro_category}', 'pro_name':'{self.pro_name}', "
            f"'pro_current_price':'{self.pro_current_price}', 'pro_raw_price':'{self.pro_raw_price}', "
            f"'pro_discount':'{self.pro_discount}', 'pro_likes_count':'{self.pro_likes_count}'}}"
        )


# Reading products from a file
file_path = "'C:\\Users\\amena\\Downloads\\A2_student_template\\data\\products.txt"

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            attributes = line.strip().split(',')
            if len(attributes) == 8:
                product = Product(*attributes)
                print(product)
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
