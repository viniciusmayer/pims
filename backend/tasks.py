import pika

from backend.models import Configuracao, ConfiguracaoEnum


class Queue(object):

    def notify(self):
        host = Configuracao.objects.filter(chave='QUEUE_HOST').first()
        host = host.valor if (not host is None) else (ConfiguracaoEnum.queueHost).value
        connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        channel = connection.channel()
        _queue = Configuracao.objects.filter(chave='QUEUE_NAME').first()
        _queue = _queue.valor if (not _queue is None) else (ConfiguracaoEnum.queueName).value
        channel.queue_declare(queue=_queue)
        channel.basic_publish(exchange='', routing_key='pims', body='')