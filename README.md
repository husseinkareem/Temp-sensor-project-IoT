# **Temp-sensor-project-IoT**
_Hussein Kareem, IoT21_

_IoT och molntjänster_

_Portfolio projekt_

---

# Bakgrund
Jämföra inomhus- samt utomhus tempratur/luftfuktighet. Data insamligen inomhus kommer från en DHT11 sensor som är uppkopplat med en Raspberry pi 4 model B. Utomhus datan  är taget från Openweathermap.

---

# Målet med projektet
Målet med min portfolio projekt är att få bättre inblick på hur molntjänsten (Azure) fungerar och i första hand hur man bygger upp en IoT helhetslösning från början till slut. Det vill säga att koppla hårdvaran och programmera den. Skicka data till molnet som då lagras där och visualisera så att användaren kan se tempraturen både inomhus och utomhus(API) lätt och smidigt via powerbi appen som finns både till IOS och Andorid.    

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
    Därefter körde jag dessa kommandon på min raspberrypi för
    att kunna skicka in data till min IoT hub från sensorn med 
    hjälp av iothubens connction string.    
        sudo pip3 install azure-iot-device  
        sudo pip3 install azure-iot-hub  
        sudo pip3 install azure-iothub-service-client  
        sudo pip3 install azure-iothub-device-client  
    Därefter skapade jag en Cosmos databas som jag kopplade till min IoT hub. 
    Varför jag just valde att lagra min data i en databas istället för
    tillexempel blob storge är för att jag behöver visa upp datan på BI verktyg. 
    Data som sparas i blob storge eller S3 är data som inte behöver läsas ofta och 
    det är ett billigt sätt att spara data på (Cold Path).  
    Sen förde jag över datan till PowerBI för att kunna
    visualisera den i desktop versionen och mobilappen. 

Skalbarhet för den här produkten kan vara att tillexempel göra färre tempratur/fukt anrop. Istället för 6 anrop i timmen så kan man anropa 2 gånger i timmen. Då blir det mindre lagring i CosmosDB och mer effektivare för kunden. Det beror ju såklart på vart man ska installera sensorn. 

Säkerhetslösningar för detta system som jag har byggt kan vara att inte dela ut offentligt på github (api nyckel, connection string för IoT huben). Man ska helst inte maila api nycklar eller certifikat. Man kan istället ladda ner den i en usb-minne med lösenord som man posta den vidare. Skaffa ett starkt lösenord för databasen är en av de viktigaste delarna för IoTlösningen. 

# API
_Utomhus tempratur/fukt:_
Utomhus tempratur/fukt hämtar jag från ett API i Openweathermap där jag har fått skapa ett konto som ger mig en API nykel som jag kan använda mig utav för att skicka förfrågan så att jag kan hämta temp/fukt med en azure funktion som triggas var tionde minut.




---


# Hårdvara
* Raspberry pi Model B 
* Temperatur- och luftfuktighetssensor (DHT11)
* Breadboard
* 3 kablar hona till hane 

<img src="/img/IMG_8704.jpg">


---


# Mjukvara 
* raspbian 32 bit 
* Python 
* NoSQL

---

# Program 
* VNC Viewer
* Thonny 
* Visual Studio code
* Microsoft Power BI desktop

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