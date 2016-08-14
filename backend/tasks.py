import pika
from backend.models import Configuracao

class Queue(object):

    def notify(self):
        host = Configuracao.objects.get(chave='QUEUE_HOST')
        connection = pika.BlockingConnection(pika.ConnectionParameters(host.valor))
        channel = connection.channel()
        _queue = Configuracao.objects.get(chave='QUEUE_NAME')
        channel.queue_declare(queue=_queue.valor)
        channel.basic_publish(exchange='', routing_key='pims', body='')