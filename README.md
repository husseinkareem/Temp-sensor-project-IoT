# **Temp-sensor-project-IoT**
_Hussein Kareem, IoT21_

_IoT och molntjänster_

_Portfolio projekt_

---

# Bakgrund
Jämföra inomhus- samt utomhus tempratur/luftfuktighet. Data insamligen inomhus kommer från en DHT11 sensor som är uppkopplat med en Raspberry pi 4 model B. Utomhus datan  är taget från Yr.no

---

# Målet med projektet
Målet med min portfolio projekt är att få bättre inblick på hur molntjänsten (Azure) fungerar. 

---


# Arkitektur



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