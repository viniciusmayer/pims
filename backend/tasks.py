import pika

class Queue(object):

    def notify(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='pims')
        channel.basic_publish(exchange='', routing_key='pims', body='')
