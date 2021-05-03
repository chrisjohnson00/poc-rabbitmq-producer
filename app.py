# example_publisher.py
import pika
import os
import logging

logging.basicConfig()

# Parse AMQP_URL (fallback to localhost)
url = os.environ.get('AMQP_URL', 'amqp://guest:guest@localhost/%2f')
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)  # Connect to AMQP_URL
channel = connection.channel()  # start a channel
channel.queue_declare(queue='pdfprocess')  # Declare a queue
# send a message

channel.basic_publish(exchange='', routing_key='pdfprocess', body='User information')
print("[x] Message sent to consumer", flush=True)
connection.close()
