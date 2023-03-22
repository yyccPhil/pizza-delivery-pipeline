from random import randrange
from random import randint
from random import uniform
from datetime import timedelta
from datetime import datetime
import json


class random_order():
    def __init__(self):
        self.customer_max_id = 6782
        self.pizza_type_list = ["cheese", "pepperoni", "supreme", "meat lover", "veggie"]
        self.max_qty = 10
        self.pizza_dict = {"cheese": 9.99, "pepperoni": 10.99, "supreme": 11.99, "meat lover": 12.99, "veggie": 8.99}
        self.start_time = datetime.strptime("10/1/2021 11:59 PM", "%m/%d/%Y %I:%M %p")
        self.end_time = datetime.strptime("2/18/2023 11:18 AM", "%m/%d/%Y %I:%M %p")

    def random_customer_id(self, customer_max_id=None):
        if customer_max_id == None:
            customer_max_id = self.customer_max_id
        return randint(1, customer_max_id)

    def random_pizza_type(self, pizza_type_list=None):
        if pizza_type_list == None:
            pizza_type_list = self.pizza_type_list
        return pizza_type_list[randint(0, len(pizza_type_list) - 1)]

    def random_qty(self, max_qty=None):
        if max_qty == None:
            max_qty = self.max_qty
        return randint(1, max_qty)

    def random_retail_price(self, pizza_type, qty, max_tax_rate=0.5, pizza_dict=None):
        if pizza_dict == None:
            pizza_dict = self.pizza_dict
        random_price_rate = uniform(1.00, (1 + max_tax_rate))
        return round(pizza_dict[pizza_type] * qty * random_price_rate, 2)     # including taxes

    def random_order_date(self, start=None, end=None):
        if start == None:
            start = self.start_time
        if end == None:
            end = self.end_time
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return (start + timedelta(seconds=random_second)).strftime("%Y-%m-%d %I:%M:%S")

    def order_json_generate(self, id):
        order_id = id
        customer_id = self.random_customer_id()
        pizza_type = self.random_pizza_type()
        qty = self.random_qty()
        retail_price = self.random_retail_price(pizza_type, qty)
        order_date = self.random_order_date()
        
        order_dict = {
            "order_id": f"{order_id}",
            "customer_id": f"{customer_id}",
            "pizza_type": f"{pizza_type}",
            "qty": f"{qty}",
            "retail_price": f"{retail_price}",
            "order_date": f"{order_date}"
        }
        
        return json.dumps(order_dict)
    

def write_json(data, filename="orders.json"):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def is_date_yesterday(strtime):
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%m%d%y')
    order_date = (datetime.strptime(strtime, "%Y-%m-%d %I:%M:%S")).strftime('%m%d%y')
    return yesterday == order_date



if __name__ == "__main__":
    
    data = {"orders": []}
    write_json(data)

    with open("orders.json") as file:
        data = json.load(file)
        temp = data["orders"]

        ro = random_order()
        for i in range(10000):
            new_data = json.loads(ro.order_json_generate(i + 1))
            print(new_data)
            temp.append(new_data)

    write_json(data)
    
    # Convert nested json to newline-delimited json
    with open("orders.json", 'r') as file:
        data = '\n'.join([json.dumps(record) for record in json.load(file)["orders"] if is_date_yesterday(record["order_date"])])
        
    with open("orders_yesterday.json", 'w') as file:    
        file.write(data)
   
