import paho.mqtt.client as mqtt

from client import SMClient

smclient = SMClient()
smclient.connect_and_listen_forever()
