import uuid
from django.test import TestCase
from model_mommy import mommy
from acessorios.models import Cores    
from informacoes.models import Tamanhos
from montagem.models import Montagem
from produtos.models import MemoriaRam,Processador,PlacaDeVideo, PlacaMae

class CoresTestCase(TestCase):

    def setUp(self):
        self.cor = mommy.make('Cores')

    def test_str(self):
        self.assertEquals(str(self.cor), self.cor.cor)

class TamanhosTestCase(TestCase):
    
    def setUp(self):
        self.tamanho = mommy.make('Tamanhos')
    
    def test_str(self):
        self.assertEquals(str(self.tamanho), str(self.tamanho))

class ProcessadorTestCase(TestCase):
    
    def setUp(self):
        self.descricao = mommy.make('Processador')
    
    def test_str(self):
        self.assertAlmostEquals(str(self.descricao), self.descricao.descricao)

class PlacaMaeTestCase(TestCase):
    
    def setUp(self):
        self.descricao = mommy.make('PlacaMae')
    
    def test_str(self):
        self.assertAlmostEquals(str(self.descricao), self.descricao.descricao)

class PlacaDeVideoTestCase(TestCase):
    
    def setUp(self):
        self.descricao = mommy.make('PlacaDeVideo')
    
    def test_str(self):
        self.assertAlmostEquals(str(self.descricao), self.descricao.descricao)

class MemoriaRamTestCase(TestCase):
    
    def setUp(self):
        self.descricao = mommy.make('MemoriaRam')
    
    def test_str(self):
        self.assertAlmostEquals(str(self.descricao), self.descricao.descricao)

class MontagemTestCase(TestCase):

    def setUp(self):
        self.nome = mommy.make('Montagem')

    def test_str(self):
        self.assertAlmostEquals(str(self.nome),str(self.nome))