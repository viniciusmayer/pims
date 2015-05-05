from django.contrib.auth.models import User
import uuid

from backend.models import Ponto, Periodo, Conta, Local, Tipo, Movimento


class UsuarioBuilder():
    usuario = None  # usarei o mesmo usuario para execucao de todos os testes
    @staticmethod
    def sessionUser():
        if UsuarioBuilder.usuario is None:
            UsuarioBuilder.usuario = User.objects.create(username='usuario_teste',
                                                         password='password',)
        return UsuarioBuilder.usuario

class UUIDGenerator():
    @staticmethod
    def uuid():
        return str(uuid.uuid4())[:29]

class PontoBuilder():
    @staticmethod
    def create(valor, periodo, conta, pontoAnterior=None):
        return Ponto.objects.create(
            valor=valor,
            periodo=periodo,
            pontoAnterior=pontoAnterior,
            conta=conta,
            usuario_criacao=UsuarioBuilder.sessionUser(),
            usuario_atualizacao=UsuarioBuilder.sessionUser(),)

class PeriodoBuilder():
    @staticmethod
    def create(data, periodoAnterior=None):
        return Periodo.objects.create(
            data=data,
            periodoAnterior=periodoAnterior,
            usuario_criacao=UsuarioBuilder.sessionUser(),
            usuario_atualizacao=UsuarioBuilder.sessionUser(),)

class ContaBuilder():
    @staticmethod
    def create(nome, rendimento=False):
        return Conta.objects.create(
            nome=nome,
            rendimento=rendimento,
            local=LocalBuilder.create(UUIDGenerator.uuid()),
            tipo=TipoBuilder.create(UUIDGenerator.uuid()),
            usuario_criacao=UsuarioBuilder.sessionUser(),
            usuario_atualizacao=UsuarioBuilder.sessionUser(),)

class LocalBuilder():
    @staticmethod
    def create(nome):
        return Local.objects.create(
            nome=nome,
            tipo=TipoBuilder.create(UUIDGenerator.uuid()),
            usuario_criacao=UsuarioBuilder.sessionUser(),
            usuario_atualizacao=UsuarioBuilder.sessionUser(),)

class TipoBuilder():
    @staticmethod
    def create(nome):
        return Tipo.objects.create(nome=nome,
            categoria='CO',
            usuario_criacao=UsuarioBuilder.sessionUser(),
            usuario_atualizacao=UsuarioBuilder.sessionUser(),)
        
class MovimentoBuilder():
    @staticmethod
    def create(operacao, valor, ponto):
        return Movimento.objects.create(operacao=operacao,
            valor=valor,
            ponto=ponto,
            usuario_criacao=UsuarioBuilder.sessionUser(),
            usuario_atualizacao=UsuarioBuilder.sessionUser(),)