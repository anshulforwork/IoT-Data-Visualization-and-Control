
import paho.mqtt.client as mqtt
import json
import time
# Define the MQTT broker details
broker = "192.168.3.176"
port = 1883
topic = "group_id/supercap/group_roll_number/OUT"

# Define the callback function for when a message is received
def on_message(client, userdata, message):
    # Decode the message payload from bytes to a string
    payload_str = message.payload.decode()

    # Parse the JSON string to a dictionary
    payload = json.loads(payload_str)

    # Print the received JSON data
    print(f"Received message: {payload}")

# Create a new MQTT client instance
client = mqtt.Client()

# Attach the callback function to the client
client.on_message = on_message

# Connect to the broker
client.connect(broker, port)

# Subscribe to the topic
client.subscribe(topic)

# Start the MQTT client loop in a separate thread
client.loop_start()
# Function to publish a JSON message
def publish_message():
    # Initial values for the parameters
    bank_voltage = 150
    charging_current = 40
    discharging_current = 120
    ambient_temperature = 37
    charge_level = 70

    # Increment step for each parameter
    voltage_step = 1
    current_step = 1
    temperature_step = 1
    charge_step = 1

    x = 0
    while x < 50:
        # Update the payload with the new values
        payload = {
            "sender": "supercap",
            "receiver": "Broker",
            "message_id": "PER_DT",
            "group_roll_number": "01",
            "hw_id": "XXYYZZNNNN",
            "group_id": "abcd1234efgh5678",
            "state": "OPERN",
            "timestamp": str(int(time.time())),
            "data": {
                "bank_voltage": str(bank_voltage),
                "charging_current": str(charging_current),
                "discharging_current": str(discharging_current),
                "capacitor_voltage": list(range(1, 57)),
                "ambient_temperature": str(ambient_temperature),
                "charge_level": str(charge_level),
                "auxiliary_capacitor_bank_parameters": "Auxiliary capacitor bank parameters"
            }
        }

        # Convert the payload to a JSON string
        message = json.dumps(payload)
        client.publish(topic, message)
        print(f"Published message: {payload}")

        # Increment the values
        bank_voltage += voltage_step
        charging_current += current_step
        discharging_current += current_step
        ambient_temperature += temperature_step
        charge_level += charge_step

        x += 1
        time.sleep(1)  # Sleep for 1 second between each iteration

# Give some time for the subscription to complete
time.sleep(2)

# Publish a message
publish_message()

# Keep the script running to receive messages
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Disconnecting from broker")
    # Stop the MQTT client loop
    client.loop_stop()
    # Disconnect from MQTT broker
    client.disconnect()