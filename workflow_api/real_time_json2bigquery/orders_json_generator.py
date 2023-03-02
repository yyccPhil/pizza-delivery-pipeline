from random import randrange
from random import randint
from random import uniform
from datetime import timedelta
from datetime import datetime
import json


def random_customer_id(customer_max_id=6782):
    return randint(1, customer_max_id)

def random_pizza_type(pizza_type_list=["cheese", "pepperoni", "supreme", "meat lover", "veggie"]):
    return pizza_type_list[randint(0, len(pizza_type_list) - 1)]

def random_qty(max_qty = 10):
    return randint(1, max_qty)

def random_retail_price(pizza_type, qty, max_tax_rate=0.5,
                        pizza_dict={"cheese": 9.99, "pepperoni": 10.99, "supreme": 11.99, "meat lover": 12.99, "veggie": 8.99}
                        ):
    random_price_rate = uniform(1.00, (1 + max_tax_rate))
    return round(pizza_dict[pizza_type] * qty * random_price_rate, 2)     # including taxes

def random_order_date(start=datetime.strptime("10/1/2021 11:59 PM", "%m/%d/%Y %I:%M %p"),
                      end=datetime.strptime("2/18/2023 11:18 AM", "%m/%d/%Y %I:%M %p")
                      ):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return (start + timedelta(seconds=random_second)).strftime("%Y-%m-%d %I:%M:%S")

def order_json_generate(id):
	order_id = id
	customer_id = random_customer_id()
	pizza_type = random_pizza_type()
	qty = random_qty()
	retail_price = random_retail_price(pizza_type, qty)
	order_date = random_order_date()
	
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


if __name__ == "__main__":
    
    data = {"orders": []}
    write_json(data)

    with open("orders.json") as file:
        data = json.load(file)
        temp = data["orders"]

        for i in range(10000):
            new_data = json.loads(order_json_generate(i + 1))
            print(new_data)
            temp.append(new_data)

    write_json(data)
    
    # Convert nested json to newline-delimited json
    with open("orders.json", 'r') as file:
        data = '\n'.join([json.dumps(record) for record in json.load(file)["orders"]])
        
    with open("orders.json", 'w') as file:    
        file.write(data)
   
