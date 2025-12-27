import paho.mqtt.client as mqtt
import sqlite3
import json

conn = sqlite3.connect('iot.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sensor_data (
        id INTEGER PRIMARY KEY,
        timestamp TEXT,
        temperature REAL,
        humidity REAL
    )
''')
conn.commit()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("iot/sensor/data")

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    cursor.execute('''
        INSERT INTO sensor_data (timestamp, temperature, humidity)
        VALUES (?, ?, ?)
    ''', (payload['timestamp'], payload['temperature'], payload['humidity']))
    conn.commit()
    print(f"Received and saved: {payload}")

broker = "test.mosquitto.org"
port = 1883

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port, 60)
client.loop_forever()