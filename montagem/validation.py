from rest_framework import serializers


def validar_processador_compatibilidade(data):
    placa_mae = data['placa_mae_id']
    #placa_mae = data.get('placa_mae_id')
    processador = data['processador_id']
    # if not placa_mae and not processador:
    #     raise serializers.ValidationError("Voce precisa preencher esses campos")
    if not ((processador.marca == placa_mae.marca) or (
            (placa_mae.marca == placa_mae.INTEL_AMD))):
            raise serializers.ValidationError("Processador imcompativel com a placa mae")


def validar_memoria_slot(data):
    placa_mae = data['placa_mae_id']
    memorias_rams = data['memoria_id']
    contagem_memoria = len(memorias_rams)
        
    if (placa_mae.slots < contagem_memoria):
        raise serializers.ValidationError("Placa mae nao possui slots suficientes")
  


def validar_memoria_quantidade_gigas(data):
    placa_mae = data['placa_mae_id']
    memorias_rams = data['memoria_id']

    qtd_memoria_ram_gigas = []
    for memoria in memorias_rams:
        qtd_memoria_ram = int(memoria.total_gigas.tamanho)
        qtd_memoria_ram_gigas.append(qtd_memoria_ram)
    total_gigas = sum(qtd_memoria_ram_gigas)

    if (int(placa_mae.memoria_suportada.tamanho) < total_gigas):
        raise serializers.ValidationError("Placa mae nao possui quantidade de memoria suficiente")
        

def validar_placa_de_video(data):
    placa_mae = data['placa_mae_id']
    placa_de_video = data['placa_de_video_id']

    if not placa_mae.video_integrado:
        if placa_de_video is None:
            raise serializers.ValidationError("Escolha uma placa mae com video integrado")