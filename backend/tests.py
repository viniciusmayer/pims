import unittest
import uuid
from datetime import datetime

from backend.builders import PontoBuilder, PeriodoBuilder, ContaBuilder


class UUIDGenerator:
    @staticmethod
    def uuid():
        return str(uuid.uuid4())[:29]


class PontoTestCase_SemMovimento(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_diferencaEntreDoisPontos(self):
        periodoA = PeriodoBuilder.create(datetime.now())
        periodoB = PeriodoBuilder.create(datetime.now(), periodoA)
        conta = ContaBuilder.create(UUIDGenerator.uuid())
        pontoA = PontoBuilder.create(100, periodoA, conta)
        pontoB = PontoBuilder.create(101, periodoB, conta, pontoA)
        diferenca = pontoB.diferenca()
        valor = 1
        self.assertEqual(
            diferenca, valor, "A diferenca nao eh %s: %s" % (valor, diferenca)
        )

    def test_diferencaPercentualEntreDoisPontos(self):
        periodoA = PeriodoBuilder.create(datetime.now())
        periodoB = PeriodoBuilder.create(datetime.now(), periodoA)
        conta = ContaBuilder.create(UUIDGenerator.uuid())
        pontoA = PontoBuilder.create(100, periodoA, conta)
        pontoB = PontoBuilder.create(102, periodoB, conta, pontoA)
        diferencaPercentual = pontoB.diferencaPercentual()
        valor = 2
        self.assertEqual(
            diferencaPercentual,
            valor,
            "A diferenca percentual nao eh %s: %s" % (valor, diferencaPercentual),
        )


class PontoTestCase_ComMovimento(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_diferencaEntreDoisPontos_comCredito(self):
        periodoA = PeriodoBuilder.create(datetime.now())
        periodoB = PeriodoBuilder.create(datetime.now(), periodoA)
        conta = ContaBuilder.create(UUIDGenerator.uuid())
        pontoA = PontoBuilder.create(100, periodoA, conta)
        pontoB = PontoBuilder.create(103, periodoB, conta, pontoA)
        # MovimentoBuilder.create("CR", 2, pontoB)
        diferenca = pontoB.diferenca()
        valor = 1
        self.assertEqual(
            diferenca, valor, "A diferenca nao eh %s: %s" % (valor, diferenca)
        )

    def test_diferencaEntreDoisPontos_comDebito(self):
        periodoA = PeriodoBuilder.create(datetime.now())
        periodoB = PeriodoBuilder.create(datetime.now(), periodoA)
        conta = ContaBuilder.create(UUIDGenerator.uuid())
        pontoA = PontoBuilder.create(100, periodoA, conta)
        pontoB = PontoBuilder.create(101, periodoB, conta, pontoA)
        # MovimentoBuilder.create("DE", 2, pontoB)
        diferenca = pontoB.diferenca()
        valor = 3
        self.assertEqual(
            diferenca, valor, "A diferenca nao eh %s: %s" % (valor, diferenca)
        )

    def test_diferencaEntreDoisPontos_comDebitoECredito(self):
        periodoA = PeriodoBuilder.create(datetime.now())
        periodoB = PeriodoBuilder.create(datetime.now(), periodoA)
        conta = ContaBuilder.create(UUIDGenerator.uuid())
        pontoA = PontoBuilder.create(100, periodoA, conta)
        pontoB = PontoBuilder.create(101, periodoB, conta, pontoA)
        # MovimentoBuilder.create("CR", 4, pontoB)
        # MovimentoBuilder.create("DE", 5, pontoB)
        diferenca = pontoB.diferenca()
        valor = 2
        self.assertEqual(
            diferenca, valor, "A diferenca nao eh %s: %s" % (valor, diferenca)
        )

    def test_diferencaPercentualEntreDoisPontos_comCredito(self):
        periodoA = PeriodoBuilder.create(datetime.now())
        periodoB = PeriodoBuilder.create(datetime.now(), periodoA)
        conta = ContaBuilder.create(UUIDGenerator.uuid())
        pontoA = PontoBuilder.create(100, periodoA, conta)
        pontoB = PontoBuilder.create(105, periodoB, conta, pontoA)
        # MovimentoBuilder.create("CR", 3, pontoB)
        diferencaPercentual = pontoB.diferencaPercentual()
        valor = 2
        self.assertEqual(
            diferencaPercentual,
            valor,
            "A diferenca percentual nao eh %s: %s" % (valor, diferencaPercentual),
        )

    def test_diferencaPercentualEntreDoisPontos_comDebito(self):
        periodoA = PeriodoBuilder.create(datetime.now())
        periodoB = PeriodoBuilder.create(datetime.now(), periodoA)
        conta = ContaBuilder.create(UUIDGenerator.uuid())
        pontoA = PontoBuilder.create(100, periodoA, conta)
        pontoB = PontoBuilder.create(101, periodoB, conta, pontoA)
        # MovimentoBuilder.create("DE", 2, pontoB)
        diferencaPercentual = pontoB.diferencaPercentual()
        valor = 3
        self.assertEqual(
            diferencaPercentual,
            valor,
            "A diferenca percentual nao eh %s: %s" % (valor, diferencaPercentual),
        )

    def test_diferencaPercentualEntreDoisPontos_comDebitoECredito(self):
        periodoA = PeriodoBuilder.create(datetime.now())
        periodoB = PeriodoBuilder.create(datetime.now(), periodoA)
        conta = ContaBuilder.create(UUIDGenerator.uuid())
        pontoA = PontoBuilder.create(100, periodoA, conta)
        pontoB = PontoBuilder.create(101, periodoB, conta, pontoA)
        # MovimentoBuilder.create("CR", 2, pontoB)
        # MovimentoBuilder.create("DE", 1, pontoB)
        diferencaPercentual = pontoB.diferencaPercentual()
        valor = 0
        self.assertEqual(
            diferencaPercentual,
            valor,
            "A diferenca percentual nao eh %s: %s" % (valor, diferencaPercentual),
        )
