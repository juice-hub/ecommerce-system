import os
import random
import time
import matplotlib.pyplot as plt

class OrderOperation:
    def __init__(self, orders_file='data/orders.txt'):
        self.orders_file = orders_file

    def generate_unique_order_id(self):
        while True:
            order_id = 'o_' + ''.join(random.choices('0123456789', k=5))
            with open(self.orders_file, 'r') as file:
                if order_id not in file.read():
                    return order_id

    def create_an_order(self, customer_id, product_id, create_time=None):
        create_time = create_time or time.strftime("%d-%m-%Y_%H:%M:%S")
        order_id = self.generate_unique_order_id()
        with open(self.orders_file, 'a') as file:
            file.write(f'{order_id},{customer_id},{product_id},{create_time}\n')
        return True

    def delete_order(self, order_id):
        with open(self.orders_file, 'r') as file:
            lines = file.readlines()
        with open(self.orders_file, 'w') as file:
            for line in lines:
                if order_id not in line:
                    file.write(line)
                else:
                    return True
        return False

    def get_order_list(self, customer_id, page_number):
        orders = []
        with open(self.orders_file, 'r') as file:
            for line in file:
                items = line.strip().split(',')
                if items[1] == customer_id:
                    orders.append(items)
        total_pages = -(-len(orders) // 10)
        start_index = (page_number - 1) * 10
        end_index = start_index + 10
        order_list = orders[start_index:end_index]

        return {
            'items': order_list,
            'current_page': page_number,
            'total_pages': total_pages
        }

    def generate_test_order_data(self):
        for i in range(10):
            customer_id = f"c_{i}"
            num_orders = random.randint(50, 200)
            for j in range(num_orders):
                product_id = self._get_random_product_id()
                month = random.randint(1, 12)
                day = random.randint(1, 28)
                date_str = f"{day}-{month}-2023_12:00:00"
                self.create_an_order(customer_id, product_id, date_str)

    def generate_single_customer_consumption_figure(self, customer_id):
        order_counts = {}
        with open(self.orders_file, 'r') as file:
            for line in file:
                items = line.strip().split(',')
                if items[1] == customer_id:
                    product = items[2]
                    order_counts[product] = order_counts.get(product, 0) + 1

        # Plotting
        plt.bar(order_counts.keys(), order_counts.values())
        plt.xlabel('Products')
        plt.ylabel('Number of Orders')
        plt.title(f'Consumption for Customer: {customer_id}')
        plt.show()

    def generate_all_customers_consumption_figure(self):
        product_counts = {}
        with open(self.orders_file, 'r') as file:
            for line in file:
                product = line.strip().split(',')[2]
                product_counts[product] = product_counts.get(product, 0) + 1

        # Plotting
        plt.bar(product_counts.keys(), product_counts.values())
        plt.xlabel('Products')
        plt.ylabel('Total Orders')
        plt.title('Total Consumption for All Customers')
        plt.show()

    def generate_all_top_10_best_sellers_figure(self):
        product_counts = {}
        with open(self.orders_file, 'r') as file:
            for line in file:
                product = line.strip().split(',')[2]
                product_counts[product] = product_counts.get(product, 0) + 1

        # Sort products by order counts and take top 10
        sorted_products = sorted(product_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        products, counts = zip(*sorted_products)

        # Plotting
        plt.bar(products, counts)
        plt.xlabel('Products')
        plt.ylabel('Total Orders')
        plt.title('Top 10 Best Sellers')
        plt.show()

    def delete_all_orders():
        if os.path.exists('data/orders.txt'):
            with open('data/orders.txt', 'w') as file:
                pass
        else:
            print("The file data/orders.txt does not exist.")

    def _get_random_product_id(self):
        # Mock implementation
        return random.choice(['p_0001', 'p_0002', 'p_0003', 'p_0004'])
