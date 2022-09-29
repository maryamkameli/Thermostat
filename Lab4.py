import time
import requests
import seeed_dht
from grove.adc import ADC
from grove.gpio import GPIO
import RPi.GPIO as GPIO

class GrovePotentiometer:
 
    def __init__(self, channel):
        self.channel = channel
 
    @property
    def angle(self):
        value = groveADC.read(self.channel)
        value = (value/1000) * 100
        return int(value)
pot = GrovePotentiometer(0)

class LEDSensor: 
    def __init__(self, channel):
        self.channel = channel
 
    @property
    def on(self):
        GPIO.output(self.channel,GPIO.HIGH)
    def off(self):
        GPIO.output(self.channel,GPIO.LOW)

temperatureSensorPort = 12 # Update this to match the port of the temperature sensor
potentiometerChannel = 0 # Update this to match the analog port of the potentiometer
#acRelay = 16 # Update this to match the GPIO port of your AC relay
#heatRelay = 4 # Update this to match the GPIO port of your Heat relay

greenLED = LEDSensor(4)
redLED = LEDSensor(16)

adcI2CAddress = 0x08 # If you get an error asking you to verify that I2C is enabled, change this to 0x04
groveADC = ADC(adcI2CAddress)

state = {'temperature': 60, 'setpoint': 70, 'ac': False, 'heat': False}
temperatureSensor = seeed_dht.DHT("11", temperatureSensorPort)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
potentiometer = GrovePotentiometer(0)

# Returns the integer value of the set point returned from the web interface 
def getSetpointFromApi():
    URL = "http://localhost:5656/setpoint"
    PARAMS = {'setpoint':setpoint}
  
# sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)
  
# extracting data in json format
    data = r.json()
    set_point = data['setpoint'][0]
    return(set_point)
    
    
                # Use the requests module to perform a get request to http://localhost:5656/setpoint
    # The response body will contain a JSON object in the form {"setpoint": XX}
    # Parse this response and return the integer value of setpoint
    


# Sends a post request to the web interface containing the current thermostat state
# newState should be an object in the form {'temperature': XX, 'setpoint': XX, heat: true/false, ac: true/false}
#def updateApi(newState):
    

#returns the converted temperature from celsius to fahrenheit
def convertTemp(temp):
    f = (temp*9/5)+32
    return(f)

    
# Returns the integer value of the temperature value returned by the temperature/humidity sensor
# Documentation for this sensor can be found here: https://wiki.seeedstudio.com/Grove-TemperatureAndHumidity_Sensor/#play-with-raspberry-pi-with-grove-base-hat-for-raspberry-pi
def readTemperatureSensor():
   humi, temp = temperatureSensor.read()
   return(int(temp))
    

# Returns the integer value of the potentiometer normalized to a value between 0 and 100


# This normalization can be done using the function ((cur - min) / (max - min)) * 100
# where cur is the current reading, min is the minimum reading of the potentiometer and max is the maximum reading of the potentiometer
# Documentation for this sensor can be found here: https://wiki.seeedstudio.com/Grove-Rotary_Angle_Sensor/                                                                                                                
def readPotentiometer():
    #cur = pot.angle
    #norm_cur = ((cur - 0)/(360))*100
    return(pot.angle)
    

# DO THIS LAST
# Takes in two boolean values. Turns on or off the associated grove relay
def setSystem(ac, heat):
    if ac==True:
        greenLED.on
    if heat==True:
        redLED.on
    if ac==False:
        greenLED.off
    if heat==False:
        redLED.off
     # You must implement

def printState(state):
    print(state) # Format this better

# This function returns two booleans. The first is whether or not the AC is on, and the second is whether or not the AC is on.
#   feel free to experiment with the control scheme
hasHitSetpoint = False
def getACHeatSettings(temperature, setpoint):
    global hasHitSetpoint
    ac = False
    heat = False
    if temperature < setpoint + 1 and temperature > setpoint - 1:
        ac = False
        heat = False
        hasHitSetpoint = True
    elif temperature > setpoint and not hasHitSetpoint:
        ac = True
        heat = False
    elif temperature < setpoint and not hasHitSetpoint:
        heat = True
        ac = False
    elif temperature > setpoint + 3:
        ac = True
        heat = False
        hasHitSetpoint = False
    elif temperature < setpoint - 3:
        heat = True
        ac = False
        hasHitSetpoint = False

    return (ac, heat)

# Main Control Loop - Runs once every second
while True:
    

    
    #apiSetpoint = getSetpointFromApi()
    potSetpoint = readPotentiometer()
    ac , heat = getACHeatSettings(readTemperatureSensor(),potSetpoint)
    setSystem(ac ,  heat)
    if (heat == True):
        print("Heat is on.")
    else:
        print("Heat is off")
    if(ac==True):
        print("AC is on")
    else:
        print("AC is off.")
    print("Current Temperature:",readTemperatureSensor())
    #setpoint = apiSetpoint # You must implement - Decide whether to use apiSetpoint or potSetpoint
    #store temperature

    #get current ac/heat settings, and then set the system to it
    
    

    

    # Update the state of the thermostat before sending it to the server. hint: look above at the format of state to update it correctly
    
    #update the Api
   

    

    time.sleep(1)
