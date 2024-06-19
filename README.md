# Question 2: Message Brokers

## Problem Statement:
Write a Python script that sends and receives messages using RabbitMQ. The script should have two functions: one for sending a message to a queue and another for receiving messages from the queue.


### Requirements:


* Use the Pika library to interact with RabbitMQ.
* Create a queue named test_queue .
* The sending function should send a message "Hello, World!" to the test_queue. 
* The receiving function should listen for messages from the test_queue and print them. 
* Ensure proper connection and channel handling to RabbitMQ.


## Run
```
docker compose up --build -d && docker-compose logs -f python-script
```
and run below for cleanout
```
docker-compose down --rmi all
```

