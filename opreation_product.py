import os
import matplotlib.pyplot as plt

class ProductOperation:
    def __init__(self, products_file='data/products.txt'):
        self.products_file = products_file

    def extract_products_from_files(self, source_dir='data/product'):
        products = []
        for filename in os.listdir(source_dir):
            if filename.endswith('.csv'):
                with open(os.path.join(source_dir, filename), mode='r') as file:
                    lines = file.readlines()
                    for line in lines:
                        items = line.strip().split('\t')  # Using '\t' for tab
                        if len(items) != 22:  # 22 fields are expected
                            continue  # skip the current iteration and move to the next line

                        product = {
                            'pro_id': items[20],
                            'pro_model': items[21],
                            'pro_category': items[0],
                            'pro_name': items[2],
                            'pro_current_price': items[3],
                            'pro_raw_price': items[4],
                            'pro_discount': items[6],
                            'pro_likes_count': items[7]
                        }
                        products.append(product)

        # Writing the products to the products_file in CSV-like format
        with open(self.products_file, 'w') as file:
            # Header
            file.write(','.join(products[0].keys()) + '\n')
            # Rows
            for product in products:
                file.write(','.join(product.values()) + '\n')

    # Implement other methods as needed

    def get_product_list(self, page_number, products_per_page=10):
        products = []
        with open(self.products_file, 'r') as file:
            lines = file.readlines()[1:]  # skip the header
            start_index = (page_number - 1) * products_per_page
            end_index = start_index + products_per_page
            for line in lines[start_index:end_index]:
                items = line.strip().split(',')
                product = {
                    'pro_id': items[0],
                    'pro_model': items[1],
                    'pro_category': items[2],
                    'pro_name': items[3],
                    'pro_current_price': items[4],
                    'pro_raw_price': items[5],
                    'pro_discount': items[6],
                    'pro_likes_count': items[7]
                }
                products.append(product)
        return products

    def delete_product(self, product_id):
        with open(self.products_file, 'r') as file:
            lines = file.readlines()

        with open(self.products_file, 'w') as file:
            for line in lines:
                if not line.startswith(product_id + ','):
                    file.write(line)

    def get_product_list_by_keyword(self, keyword):
        matching_products = []
        with open(self.products_file, 'r') as file:
            lines = file.readlines()[1:]  # skip the header
            for line in lines:
                if keyword.lower() in line.lower():  # case-insensitive search
                    matching_products.append(line)
        return matching_products

    def get_product_by_id(self, product_id):
        with open(self.products_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(product_id + ','):
                    return line
        return None

    def generate_category_figure(self):
        categories = {}
        with open(self.products_file, 'r') as file:
            lines = file.readlines()[1:]  # skip the header
            for line in lines:
                category = line.strip().split(',')[2]  # 3rd column is category
                categories[category] = categories.get(category, 0) + 1

        plt.bar(categories.keys(), categories.values())
        plt.xlabel('Category')
        plt.ylabel('Number of Products')
        plt.title('Products by Category')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def generate_discount_figure(self):
        discounts = []
        with open(self.products_file, 'r') as file:
            lines = file.readlines()[1:]  # skip the header
            for line in lines:
                discount = float(line.strip().split(',')[6])  # 7th column is discount
                discounts.append(discount)

        plt.hist(discounts, bins=20, edgecolor='black')
        plt.xlabel('Discount')
        plt.ylabel('Number of Products')
        plt.title('Distribution of Discounts')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def generate_likes_count_figure(self):
        likes_counts = []
        with open(self.products_file, 'r') as file:
            lines = file.readlines()[1:]  # skip the header
            for line in lines:
                likes_count = int(line.strip().split(',')[7])  # 8th column is likes count
                likes_counts.append(likes_count)

        plt.hist(likes_counts, bins=20, edgecolor='black')
        plt.xlabel('Likes Count')
        plt.ylabel('Number of Products')
        plt.title('Distribution of Likes Count')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def generate_discount_likes_count_figure(self):
        discounts = []
        likes_counts = []
        with open(self.products_file, 'r') as file:
            lines = file.readlines()[1:]  # skip the header
            for line in lines:
                items = line.strip().split(',')
                discount = float(items[6])  # 7th column is discount
                likes_count = int(items[7])  # 8th column is likes count
                discounts.append(discount)
                likes_counts.append(likes_count)

        plt.scatter(discounts, likes_counts, edgecolor='black', linewidth=0.5, alpha=0.75)
        plt.xlabel('Discount')
        plt.ylabel('Likes Count')
        plt.title('Relationship between Discounts and Likes Count')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def delete_all_products(self):
        if os.path.exists(self.products_file):
            os.remove(self.products_file)

product_op = ProductOperation()

# Check if products.txt is empty
if os.path.getsize(product_op.products_file) == 0:
    product_op.extract_products_from_files()


