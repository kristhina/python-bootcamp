import pika

parameters = pika.URLParameters('amqp://guest:guest@10.1.1.240:32803/%2f')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.basic_publish(
    'krysia_p_ex',
    'krysialove',
    'tresc kolejnej wiadomosci',
    pika.BasicProperties(
        content_type='text/plain',
        delivery_mode=1
    )
)

connection.close()