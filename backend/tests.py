from datetime import datetime
import unittest
import uuid

from backend.builders import PontoBuilder, ContaBuilder, MovimentoBuilder


class UUIDGenerator():
    @staticmethod
    def uuid():
        return str(uuid.uuid4())[:29]

class PontoTestCase_SemMovimento(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
        
    def test_diferencaEntreDoisPontos(self):
        conta = ContaBuilder.create(UUIDGenerator.uuid())
        pontoA = PontoBuilder.create(100, datetime.now(), conta)
        pontoB = PontoBuilder.create(101, datetime.now(), conta)
        diferenca = pontoB.diferenca()
        valor = 1
        self.assertEqual(diferenca, valor, 'A diferenca nao eh %s: %s' % (valor, diferenca))
    
    def test_diferencaPercentualEntreDoisPontos(self):
        conta = ContaBuilder.create(UUIDGenerator.uuid())
        pontoA = PontoBuilder.create(100, datetime.now(), conta)
        pontoB = PontoBuilder.create(102, datetime.now(), conta)
        diferencaPercentual = pontoB.diferencaPercentual()
        valor = 2
        self.assertEqual(diferencaPercentual, valor, 'A diferenca percentual nao eh %s: %s' % (valor, diferencaPercentual))    

     
class PontoTestCase_ComMovimento(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
        
    def test_diferencaEntreDoisPontos_comCredito(self):
        conta = ContaBuilder.create(UUIDGenerator.uuid())
        pontoA = PontoBuilder.create(100, datetime.now(), conta)
        pontoB = PontoBuilder.create(103, datetime.now(), conta)
        MovimentoBuilder.create('CR', 2, pontoB)
        diferenca = pontoB.diferenca()
        valor = 1
        self.assertEqual(diferenca, valor, 'A diferenca nao eh %s: %s' % (valor, diferenca))
    
    def test_diferencaEntreDoisPontos_comDebito(self):
        conta = ContaBuilder.create(UUIDGenerator.uuid())
        pontoA = PontoBuilder.create(100, datetime.now(), conta)
        pontoB = PontoBuilder.create(101, datetime.now(), conta)
        MovimentoBuilder.create('DE', 2, pontoB)
        diferenca = pontoB.diferenca()
        valor = 3
        self.assertEqual(diferenca, valor, 'A diferenca nao eh %s: %s' % (valor, diferenca))
    
    def test_diferencaEntreDoisPontos_comDebitoECredito(self):
        conta = ContaBuilder.create(UUIDGenerator.uuid())
        pontoA = PontoBuilder.create(100, datetime.now(), conta)
        pontoB = PontoBuilder.create(101, datetime.now(), conta)
        MovimentoBuilder.create('CR', 4, pontoB)
        MovimentoBuilder.create('DE', 5, pontoB)
        diferenca = pontoB.diferenca()
        valor = 2
        self.assertEqual(diferenca, valor, 'A diferenca nao eh %s: %s' % (valor, diferenca))
        
    def test_diferencaPercentualEntreDoisPontos_comCredito(self):
        conta = ContaBuilder.create(UUIDGenerator.uuid())
        pontoA = PontoBuilder.create(100, datetime.now(), conta)
        pontoB = PontoBuilder.create(105, datetime.now(), conta)
        MovimentoBuilder.create('CR', 3, pontoB)
        diferencaPercentual = pontoB.diferencaPercentual()
        valor = 2
        self.assertEqual(diferencaPercentual, valor, 'A diferenca percentual nao eh %s: %s' % (valor, diferencaPercentual))
        
    def test_diferencaPercentualEntreDoisPontos_comDebito(self):
        conta = ContaBuilder.create(UUIDGenerator.uuid())
        pontoA = PontoBuilder.create(100, datetime.now(), conta)
        pontoB = PontoBuilder.create(101, datetime.now(), conta)
        MovimentoBuilder.create('DE', 2, pontoB)
        diferencaPercentual = pontoB.diferencaPercentual()
        valor = 3
        self.assertEqual(diferencaPercentual, valor, 'A diferenca percentual nao eh %s: %s' % (valor, diferencaPercentual))
        
    def test_diferencaPercentualEntreDoisPontos_comDebitoECredito(self):
        conta = ContaBuilder.create(UUIDGenerator.uuid())
        pontoA = PontoBuilder.create(100, datetime.now(), conta)
        pontoB = PontoBuilder.create(101, datetime.now(), conta)
        MovimentoBuilder.create('CR', 2, pontoB)
        MovimentoBuilder.create('DE', 1, pontoB)
        diferencaPercentual = pontoB.diferencaPercentual()
        valor = 0
        self.assertEqual(diferencaPercentual, valor, 'A diferenca percentual nao eh %s: %s' % (valor, diferencaPercentual))