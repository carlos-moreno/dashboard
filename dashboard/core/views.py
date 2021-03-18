import requests
from decouple import config
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/accounts/login/')
def home(request):
    disk = requests.get(config("API") + 'disk_space._')
    load = requests.get(config("API") + 'system.load')
    ram = requests.get(config("API") + 'system.ram')
    net = requests.get(config("API") + 'net.eth0')
    context = {
        "disk_label": ['Disponível', 'Usado', 'Reservado para o root'],
        "disk_data": disk.json()['data'][0][1:],
        "load_labels": ['1 minuto', '5 minutos', '15 minutos'],
        "load_data": load.json()['data'][0][1:],
        "ram_labels": ['Mem. livre', 'Mem. usada', 'Mem. cacheada', 'Buffers'],
        "ram_data": ram.json()['data'][0][1:],
        "recebido": net.json()['data'][0][1],
        "enviado": net.json()['data'][0][2] * -1,
    }
    return render(request, 'index.html', context)
