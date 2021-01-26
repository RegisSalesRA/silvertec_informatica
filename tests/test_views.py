import json
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse_lazy
from montagem.models import *
from produtos.models import *

class MontagemTests(APITestCase):

    def setUp(self):

        self.url = "/api/"

        self.usuario_id = 1
        self.placa_de_video_id = 1
        self.processador_intel_id = Processador.objects.filter(marca="INTEL").first()
        self.processador_amd_id = Processador.objects.filter(marca="AMD").first()
        self.memoria_8_Gigas_id = MemoriaRam.objects.filter(total_gigas=8).first()
        self.memoria_64_Gigas_id = MemoriaRam.objects.filter(total_gigas=16).first()
        
        self.intel_placa_mae_2_slots_16_gb_id = PlacaMae.objects.filter(marca="INTEL").first()
        
        self.amd_placa_mae_2_slots_16_gb_id = PlacaMae.objects.filter(marca="AMD").first()
        
        self.hybrid_mother_board_with_onboard_graphics_4_slots_64_gb_id = PlacaMae.objects.filter(marca="INTEL_AMD").first()
        

    def test_lista_de_pedido(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_pode_criar_a_montagem(self):
        data = {
            "usuario_id": "self.usuario_id",
            "placa_de_video_id": "self.placa_de_video_id",
            "processador_intel_id": "self.processador_amd_id",
            "intel_placa_mae_2_slots_16_gb_id": "self.amd_placa_mae_2_slots_16_gb_id",
            "memoria_8_Gigas_id": "self.memoria_8_Gigas_id",
            }
        print(data)
        response = self.client.post("/api/",data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)    