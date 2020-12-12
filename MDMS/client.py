import paho.mqtt.client as mqtt
import sched, time
import threading
from datetime import datetime

class MDMSClient (mqtt.Client):

    def __init__(self):
        self.id="99e6854add854azafa87af"
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
    
    def connect(self):
        self.client.connect("mqtt-broker", 1883, 60)

    def connect_and_listen_forever(self):
        self.connect()
        self.publish_prix()
        self.publish_reduction()
        self.client.loop_forever()

    def publish_prix(self,prix=4):
        self.client.publish("prix",qos=0, payload=str({"id": self.id, "prix":prix}))
        threading.Timer(60.0*60.0, self.publish_prix).start()

    def publish_reduction(self, reduction=2):
        self.client.publish("reduction",qos=2,payload=str({"id": self.id, "reduction":reduction}))
        threading.Timer(60.0, self.publish_reduction).start()
    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("production/#")
        client.subscribe("consomation/#")

    @staticmethod
    def on_message(client, userdata, msg):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time+" "+msg.topic+" "+str(msg.payload))