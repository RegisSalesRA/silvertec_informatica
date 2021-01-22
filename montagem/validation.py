from rest_framework import serializers


def validar_processador_compatibilidade(data):
    placa_mae = data['placa_mae']
    processador = data['processador']
    
    if not ((processador.marca == placa_mae.marca) or (
            (placa_mae.marca == placa_mae.INTEL_AMD))):
            raise serializers.ValidationError("Processador imcompativel com a placa mae")


def validar_memoria_slot(data):
    placa_mae = data['placa_mae']
    memoria = data['memoria']
    
    if (placa_mae.slots < memoria.quantidade):
        raise serializers.ValidationError("Placa mae nao possui slots suficientes")
    

def validar_memoria_quantidade_gigas(data):
    placa_mae = data['placa_mae']
    memoria = data['memoria']
    if (placa_mae.memoria_suportada.tamanho < memoria.total_gigas.tamanho):
        raise serializers.ValidationError("Placa mae nao possui quantidade de memoria suficiente")



def validar_placa_de_video(data):
    placa_mae = data['placa_mae']
    placa_de_video = data['placa_de_video']

    if not placa_mae.video_integrado:
        if placa_de_video is None:
            raise serializers.ValidationError("Escolha uma placa mae com video integrado")