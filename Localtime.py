import requests
from datetime import datetime

timezones =[]
def hora(timezone):
    url ='http://worldtimeapi.org/api/timezone/' + timezone
    resposta = requests.get(url)
    hora = datetime.fromisoformat(resposta.json()
                                  ['datetime'])
    return hora

def timezones_disponiveis():

    global timezones
    if(len(timezones)> 0):
        return timezones
    url = 'http://worldtimeapi.org/api/timezone/'
    resposta = requests.get(url)
    timezones = resposta.json()
    return timezones



