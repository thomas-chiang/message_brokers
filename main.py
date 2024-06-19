import pika
import time

def establish_connection():
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters('rabbitmq', 5672, '/', pika.PlainCredentials('user', 'password'))
            )
            return connection
        except pika.exceptions.AMQPConnectionError as e:
            print("Connection failed. Wait for RabbitMQ to be fully ready. Retrying in 5 seconds...")
            time.sleep(5)


def send_message():
    # Establish a connection to RabbitMQ server
    connection = establish_connection()
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='test_queue')

    # Send a message
    channel.basic_publish(exchange='', routing_key='test_queue', body='Hello, World!')
    print("Sent 'Hello, World!'")

    # Close the connection
    connection.close()

def receive_messages():
    # Establish a connection to RabbitMQ server
    connection = establish_connection()
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='test_queue')

    # Define a callback for consuming messages
    def callback(ch, method, properties, body):
        print(f"Received {body}")
        print('Waiting for messages. To exit press CTRL+C')

    # Consume messages from the queue
    channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

if __name__ == '__main__':
    send_message()
    receive_messages()
