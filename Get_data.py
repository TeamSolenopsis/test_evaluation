import paho.mqtt.client as mqtt
import time
import datetime

robot_count = 4

def print_message(client, userdata, msg):
    timestamp = datetime.time()
    print('Received a new temperature data ', str(msg.payload.decode('utf-8')))
    print(timestamp)
    print('message topic=', msg.topic)
    print('message qos=', msg.qos)

def print_message_v(msg):
    timestamp = datetime.datetime.today()
    print('Received a new temperature data ', msg)
    print(timestamp.time())

# Give a name to this MQTT client
client = mqtt.Client('test_evaluation')
for i in range(robot_count):
    robot_topics = f"r{i}"
    client.message_callback_add('/{robot_topics}/#', print_message)
    print_message_v(robot_topics)

# IP address of your MQTT broker, using ipconfig to look up it  
client.connect('192.168.1.101', 1883)
# 'greenhouse/#' means subscribe all topic under greenhouse



for i in range(robot_count):
    robot_topics = f"r{i}"
    client.subscribe('/{robot_topics}/#')

client.loop_forever()
# stop the loop
# client.loop_stop()