from random import randrange
from random import randint
from random import uniform
from datetime import timedelta
from datetime import datetime
import pandas as pd
import csv


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


d1 = datetime.strptime("10/1/2021 11:59 PM", "%m/%d/%Y %I:%M %p")
d2 = datetime.strptime("2/18/2023 11:18 AM", "%m/%d/%Y %I:%M %p")

type_list = ["cheese", "pepperoni", "supreme", "meat lover", "veggie"]
price_list = [9.99, 10.99, 11.99, 12.99, 8.99]

customers_csv = pd.read_csv("customers.csv")
count_customers = len(customers_csv) + 1

# for i in range(10):
#     print([i + 1, randint(1, 6782), type_list[randint(0, 4)], randint(1, 10), round(uniform(0.01, 999.99), 2),
#            random_date(d1, d2).strftime("%Y-%m-%d %I:%M:%S")])

with open('orders.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(10000):
        order_id = i + 1
        customer_id = randint(1, count_customers)

        list_i = randint(0, 4)
        pizza_type = type_list[list_i]
        qty = randint(1, 10)
        retail_price = round(qty * price_list[list_i] * uniform(1.00, 1.50), 2)     # including taxes
        order_date = random_date(d1, d2).strftime("%Y-%m-%d %I:%M:%S")

        writer.writerow([order_id, customer_id, pizza_type, qty, retail_price, order_date])
