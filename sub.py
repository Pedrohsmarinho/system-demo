# python3.6

import random

from paho.mqtt import client as mqtt_client


broker = '127.0.0.1'
port = 8888
topic = "parkAssistant/vagas"

client_id = f'python-mqtt-{random.randint(0, 100)}'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# def clear_retained(retained): #accepts single topic or list
#     msg=""
#     if isinstance(retained[0],str):
#         client.publish(retained[0],msg,qos=QOS1,retain=RETAIN)
#     else:
#         try:
#             for t in retained:
#                 client.publish(t[0],msg,qos=QOS1,retain=RETAIN)
#                 print ("Clearing retaind on ",msg,"topic -",t[0]," qos=",QOS1," retain=",RETAIN)
#         except:
#             Print("problems with topic")
#             return -1

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
