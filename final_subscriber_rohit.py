import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with rohit server "+str(rc))
  client.subscribe("topic/test")

def on_message(client, userdata, message):
    print ("Message received: "  + message.payload.decode())
    #print("Yes!")
    #client.disconnect()
    
client = mqtt.Client("sdfghjertycvbn")
client.connect("www.ioturtle.com",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()