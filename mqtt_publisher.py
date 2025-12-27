import paho.mqtt.client as mqtt
import pandas as pd
import json
import time

data = pd.read_csv('iot_sensor_data.csv')

broker = "test.mosquitto.org"  
port = 1883
topic = "iot/sensor/data"

client = mqtt.Client()
client.connect(broker, port, 60)

for index, row in data.iterrows():
    payload = json.dumps({
        "timestamp": row['timestamp'],
        "temperature": row['temperature'],
        "humidity": row['humidity']
    })
    client.publish(topic, payload)
    print(f"Sent: {payload}")
    time.sleep(1)  

client.disconnect()