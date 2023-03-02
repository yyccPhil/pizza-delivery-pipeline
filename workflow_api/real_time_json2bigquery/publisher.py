import os
import json
from orders_json_generator import order_json_generate
from google.cloud import pubsub_v1


credentials_path = "pizza_delivery_privatekey.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

publisher = pubsub_v1.PublisherClient()
topic_path = "projects/artful-turbine-378406/topics/pizza-delivery"

count = 0
for i in range(10):
	
	order_id = i + 1

	data = f"Message for order {order_id} is ready!"
	data = data.encode("utf-8")
	attributes = json.loads(order_json_generate(order_id))


	future = publisher.publish(topic_path, data, **attributes)
	print(f"published message id {future.result()}\n")
	
	count += 1

print(f"Successfully publish {count} messages!")
