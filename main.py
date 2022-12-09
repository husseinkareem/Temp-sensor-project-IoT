import random  
import adafruit_dht
import time
import board
from azure.iot.device import IoTHubDeviceClient, Message
import datetime

import json
from azure.iot.device import Message


dhtDevice = adafruit_dht.DHT11(board.D4)  # Create a DHT11 object and pass it the pin that the sensor is connected to.       

pin = 4 # Set the pin that the sensor is connected to.

MSG_SND = '{{"temperature": {temperature},"humidity": {humidity}}}' # Create a string that contains the message that will be sent to the IoT Hub. The message contains two key-value pairs: temperature and humidity. The values for these keys will be set in the code below.   

dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio=False) # Create a DHT11 object and pass it the pin that the sensor is connected to.

while True:
    temperature = dhtDevice.temperature # Read the temperature from the sensor.
    humidity = dhtDevice.humidity # Read the humidity from the sensor.
    print(
            "Temp:{:.1f} C    Humidity: {}% ".format(
                temperature, humidity
            )
        )
    
    def iothub_client_init():  
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)  # Create an IoT Hub client using the connection string.
        return client
    
    def iothub_client_telemetry_sample_run():  
        try:  
            client = iothub_client_init() # Initialize the client.
            print ( "Sending data to IoT Hub, press Ctrl-C to exit" )
            
            while True:  
                body = {
                    "time": str(datetime.datetime.utcnow()),
                    "temperature": temperature,
                    "humidity": humidity
                }
                message = Message(json.dumps(body))
                
                # json format
                message.content_encoding = "UTF-8"
                message.content_type = "application/json"
        
                print( "Sending message: {}".format(message) )  
                client.send_message(message) # Send the message.
                print ( "Message successfully sent" )  
                time.sleep(600) # Wait 10 minutes before sending the next message.
                
        except KeyboardInterrupt:  
            print ( "IoTHubClient stopped" )
            
    if __name__ == '__main__':  
        print ( "Press Ctrl-C to exit" )  
        iothub_client_telemetry_sample_run()