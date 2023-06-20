import paho.mqtt.client as mqtt
import time
import datetime

robot_count = 4

def print_message(client, userdata, msg):
    print('Received a new odom data ', str(msg.payload.decode('utf-8')))
    print('message topic=', msg.topic)
    print('message qos=', msg.qos)

    #use a diffrent file for each robot
    robot_number = 1
    with open(f'robot{robot_number}.txt', 'a') as f:
        f.write(str(msg.payload.decode('utf-8') + ', ' + str(datetime.datetime.now().time())))
        f.write('\n')

# Give a name to this MQTT client
client = mqtt.Client('test_evaluation')
# for i in range(robot_count):
#     robot_topics = f"r{i}"
#     client.message_callback_add('/{robot_topics}/#', print_message)
#     print(f"Added callback for {robot_topics}")
client.message_callback_add('odom', print_message)

# IP address of your MQTT broker 
client.connect('192.168.75.201', 1883)

# for i in range(robot_count):
#     robot_topics = f"r{i}"
#     client.subscribe('/{robot_topics}/#')
#     print(f"Subscribed to {robot_topics}")
client.subscribe('odom', qos=1)

client.loop_forever()

# stop the loop
# client.loop_stop()