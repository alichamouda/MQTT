import paho.mqtt.client as mqtt
import threading
from datetime import datetime

class SMClient (mqtt.Client):
    def __init__(self):
        self.id="4aea554ada5d4azafa87af"
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
    
    def connect(self):
        self.client.connect("mqtt-broker", 1883, 60)

    def connect_and_listen_forever(self):
        self.connect()
        self.publish_consommation()
        self.publish_production()
        self.client.loop_forever()

    def publish_consommation(self,consomation=4):
        self.client.publish("consomation",qos=2,payload=str({"id": self.id, "consomation":consomation}))
        threading.Timer(60.0*60.0, self.publish_consommation).start()

    def publish_production(self, production=2):
        self.client.publish("production",qos=2,payload=str({"id": self.id, "production":production}))
        threading.Timer(60.0*15.0, self.publish_production).start()

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("reduction/#")
        client.subscribe("prix/#")

    # The callback for when a PUBLISH message is received from the server.
    @staticmethod
    def on_message(client, userdata, msg):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time+" "+msg.topic+" "+str(msg.payload))