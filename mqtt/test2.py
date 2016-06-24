import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("Connected with result code: "+str(rc))
	client.suscribe("natimqtt")

def on_mesagge(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	if str(msg.payload) == "piztu":
		client.publish("natimqtt", "piztuta")
	if str(msg.payload) == "itzali":
		client.publish("natimqtt", "itzalita")
	if str(msg.payload) == "egoera":
		client.publish("natimqtt", "egoera")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()