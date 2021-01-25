from django.test import TestCase
from django.test import client
from rest_framework import status
from django.urls import reverse_lazy
from montagem.models import *
from produtos.models import *

class MontagemTests(TestCase):

    def setUp(self):
        self.url = "/api/"

        self.nome = 1
        self.placa_de_video = 1
        self.processador_intel = Processador.objects.filter(marca="INTEL").first()
        self.processador_amd = Processador.objects.filter(marca="AMD").first()
        self.memoria_8_Gigas = MemoriaRam.objects.filter(total_gigas=8).first()
        self.memoria_16_Gigas = MemoriaRam.objects.filter(total_gigas=16).first()
        
        self.intel_placa_mae_2_slots_16_gb_id = PlacaMae.objects.filter(marca="INTEL").first()
        
        self.amd_placa_mae_2_slots_16_gb_id = PlacaMae.objects.filter(marca="AMD").first()
        
        self.hybrid_mother_board_with_onboard_graphics_4_slots_64_gb_id = PlacaMae.objects.filter(marca="INTEL_AMD").first()
        

    def test_lista_de_pedido(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_pode_fazer_a_montagem(self):
        data = {
            "nome": str(self.nome),
            "processador": str(self.processador_amd),
            "placa_mae": str(self.amd_placa_mae_2_slots_16_gb_id),
            "memoria": [str(self.memoria_16_Gigas)],
            "placa_de_video": str(self.placa_de_video),
        }
        print(data)
        response = self.nome(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)    