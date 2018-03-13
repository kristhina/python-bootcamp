import pika

def on_message(channel, method_frame, header_frame, body):
    print(method_frame.delivery_tag)
    print(body)
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)

parameters = pika.URLParameters('amqp://guest:guest@10.1.1.240:32803/%2f')

connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.basic_consume(on_message, 'krysia_p')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()
