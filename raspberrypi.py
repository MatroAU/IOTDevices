import paho.mqtt.client as mqtt

MQTT_ADDRESS = '172.20.20.198'
MQTT_TOPIC = 'barrettOutTopic'
MQTT_USER = 'mb70'
MQTT_PASSWORD = 'candib123'
COUNTER = 0

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global COUNTER
    if msg.payload.decode("utf-8") == "connected to arduino":
        COUNTER += 1
        print(f"Button Press Counter: {COUNTER}")
    else:
        print(msg.payload.decode("utf-8"))
    client.publish("barrettInTopic", f"Button Press Counter: {COUNTER}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_ADDRESS, 1883, 60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()