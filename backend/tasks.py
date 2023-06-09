import pika

from backend.models import Configuracao


class Queue(object):

    def notify(self):
        host = Configuracao.objects.filter(chave='QUEUE_HOST').first()
        connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        channel = connection.channel()
        queue = Configuracao.objects.filter(chave='QUEUE_NAME').first()
        channel.queue_declare(queue=queue)
        channel.basic_publish(exchange='', routing_key='pims', body='')
