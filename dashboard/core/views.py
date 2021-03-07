from django.shortcuts import render
from decouple import config
import requests


def home(request):
    disk = requests.get(config("API") + 'disk_space._')
    load = requests.get(config("API") + 'system.load')
    ram = requests.get(config("API") + 'system.ram')
    context = {
        "disk_label": ['Disponível', 'Usado', 'Reservado para o root'],
        "disk_data": disk.json()['data'][0][1:],
        "load_labels": ['1 minuto', '5 minutos', '15 minutos'],
        "load_data": load.json()['data'][0][1:],
        "ram_labels": ['Mem. livre', 'Mem. usada', 'Mem. cacheada', 'Buffers'],
        "ram_data": ram.json()['data'][0][1:],
    }
    return render(request, 'index.html', context)
