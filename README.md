# **Temp-sensor-project-IoT**
_Hussein Kareem, IoT21_

_IoT och molntjänster_

_Portfolio projekt_

---

# Bakgrund
Jämföra inomhus- samt utomhus tempratur/luftfuktighet. Data insamligen inomhus kommer från en DHT11 sensor som är uppkopplat med en Raspberry pi 4 model B. Utomhus datan  är taget från Openweathermap.

---

# Målet med projektet
Målet med min portfolio projekt är att få bättre inblick på hur molntjänsten (Azure) fungerar och i första hand hur man bygger upp en IoT helhetslösning från början till slut. Det vill säga att koppla hårdvaran och programmera den. Skicka data till molnet som då lagras där och visualisera så att användaren kan se tempraturen både inomhus och utomhus lätt och smidigt via powerbi appen som finns både till Ios och Andorid.    

---


# Arkitektur
<img src="/img/project.jpg">

# Projekt beskrivning
_Inomhus tempratur/fukt:_
    DHT11 sensorn är kopplad med 3 hona till hane kablar. 
        
        Raspberry pi Pinout:
        GND --> pin06 (Ground)
        VCC(+) --> pin02 (DC Power 5v)
        DATA --> pin07 (GPIO04)
    
    Efter att jag lyckades koppla min sensor så skapade jag en IoT hub i Azure.
    Därefter körde jag dessa kommandon på min raspberrypi för att kunna skicka in data till min IoT hub från sensorn med hjälp av iothubens connction string.    
        sudo pip3 install azure-iot-device  
        sudo pip3 install azure-iot-hub  
        sudo pip3 install azure-iothub-service-client  
        sudo pip3 install azure-iothub-device-client  
    Därefter skapade jag en Cosmos databas som jag kopplade till min IoT hub. 
    Sen förde jag över datan till PowerBI för att kunna
    visualisera den i desktop versionen och mobilappen. 
# API
_Utomhus tempratur/fukt:_
Utomhus tempratur/fukt hämtar jag från ett API i Openweathermap där jag har fått skapa ett konto som ger mig en API nykel som jag kan använda mig utav för att skicka förfrågan så att jag kan hämta temp/fukt med en azure funktion som triggas var tionde minut.




---


# Hårdvara
* Raspberry pi Model B 
* Temperatur- och luftfuktighetssensor (DHT11)
* 3 kablar hona till hane 

<img src="/img/IMG_8704.jpg">


---


# Mjukvara 
* raspbian 32 bit 
* Python 
* SQL

---

# Program 
* VNC Viewer
* Thonny 

---

# Libraries
random  
adafruit_dht 
time 
board   
azure.iot.device 
IoTHubDeviceClient, Messag


---

# Kod
[Sensorkoden](https://github.com/husseinkareem/Temp-sensor-project-IoT/blob/main/main.py)