# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client
from datetime import date
from datetime import datetime

currentDate = date.today()
currentTime = datetime.now()

dateInText = '{}/{}/{}'.format(currentDate.day, currentDate.month,currentDate.year)
updateTime = currentTime.strftime('%H:%M')

broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set('emqx', 'public')
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

dadosSobreAsVagas = [
    {
        "id": 1,
        "situacao": "ocupada",
        "dataDaUltimaAtualizacao":  dateInText,
        "horaDaUltimaAtualizacao":  updateTime
    },
    {
        "id": 2,
        "situacao": "livre",
        "dataDaUltimaAtualizacao":  dateInText,
        "horaDaUltimaAtualizacao":  updateTime
    },   
    {
        "id": 3,
        "situacao": "livre",
        "dataDaUltimaAtualizacao":  dateInText,
        "horaDaUltimaAtualizacao":  updateTime    
    },    
    {
        "id": 4,
        "situacao": "livre",
        "dataDaUltimaAtualizacao":  dateInText,
        "horaDaUltimaAtualizacao":  updateTime    
    },    
    {
        "id": 5,
        "situacao": "ocupada",
        "dataDaUltimaAtualizacao":  dateInText,
        "horaDaUltimaAtualizacao":  updateTime    
    }
]
        
def publish(client):    
      while True:
        numeroVaga = 0
        time.sleep(1)
        
        result = client.publish(topic, f"{dadosSobreAsVagas}")
        status = result[0]
        if status == 0:
           print(dadosSobreAsVagas)
           idSelect =  int(input("Digite a vaga que deseja alterar: "))

           if(idSelect):
            print("    ")
            print("    ")
            print("    ")
            dadosSobreAsVagas[idSelect-1]["situacao"] = "ocupada"
                
        else:
            print(f"Falhou ao enviar mensagem para o topico {topic}")
        numeroVaga += 1

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()
