import paho.mqtt.client as mqtt

# This is the Publisher
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client = mqtt.Client("sdfaaaghjaacvbnvbn")
client.on_publish= on_publish
client.connect("www.ioturtle.com",1883,60)
client.publish("topic/test", "This is my server move back bitches !!")
#client.disconnect();
