import os
from google.cloud import pubsub_v1

credentials_path = "pizza_delivery_privatekey.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

publisher = pubsub_v1.PublisherClient()
topic_path = "projects/artful-turbine-378406/topics/pizza-delivery"

count = 0
orders_csv = open('orders.csv')
orders = orders_csv.readlines()
for order in orders:
	
	order_id, customer_id, pizza_type, qty, retail_price, order_date = order.strip().split(',')

	data = "My order message is ready!"
	data = data.encode("utf-8")
	attributes = {
		"order_id": order_id,
		"customer_id": customer_id,
		"type": pizza_type,
		"qty": qty,
		"retail_price": retail_price,
		"order_date": order_date
	}


	future = publisher.publish(topic_path, data, **attributes)
	print(f"published message id {future.result()}\n")
	
	count += 1

print(f"Successfully publish {count} messages!")
orders_csv.close()
