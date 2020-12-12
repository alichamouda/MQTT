import paho.mqtt.client as mqtt

from client import MDMSClient

smclient = MDMSClient()
smclient.connect_and_listen_forever()
