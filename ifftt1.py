from flask import Flask
from flask_ask import Ask,statement,question,session,convert_errors
import json
import requests
import time
import unidecode


app = Flask(__name__)
ask = Ask(app, "/jochebed")
#logging.getLogger('flask_ask').setLevel(logging.DEBUG)

#########################Intents########################
@app.route('/')
def homepage():
    return "hi this is mahesh from ifttt homepage"


@app.route('/ifttt/v1/status',methods = ['POST', 'GET'])
def homepage1():


    #report = {}  
    #report["value1"] = "this is ifttt programm"  
    #requests.post("https://maker.ifttt.com/trigger/Mahesh/cE-g8Ez3Be3ryVsJKlQTHL/hNbw-WNROGyCMAn4O8Vtk_o9fSYD1XvjufNGWYtfOfXUUtwpScf0xl2ywKhvU-3p", data=report) 
    return "hi this is mahesh from ifttt homepage1"


@app.route('/ifttt/v1/test/setup',methods = ['POST', 'GET'])
def homepage2():
    #return "hi this is mahesh from ifttt. homepage2"
    #report = {}  
    #report["value1"] = "this is ifttt programm"  
    #requests.post("https://maker.ifttt.com/trigger/Mahesh/cE-g8Ez3Be3ryVsJKlQTHL/hNbw-WNROGyCMAn4O8Vtk_o9fSYD1XvjufNGWYtfOfXUUtwpScf0xl2ywKhvU-3p", data=report) 
    return "hi this is mahesh from ifttt homepage2"

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='192.168.173.7', port=5905)


# CurtainClose
# CurtainDown
# CurtainOpen
# CurtainUp 
# Curtain Close
# CurtainOpen
# demo area light fan
# DemoArea Door
# DemoArea Door1
# Demo area Fan
# Demo Area Light
# Dining Fan
# Dining Light
# Director's Fan
# Director's Light
# G4G Fan
# G4G light
# HC1 FAN
# HC2 fan
# Halfcubes top lights
# HC1 Light
# iot all
# IOT fan1
# IOT fan2
# IOT light
# josh01
# Kitchen Light
# Library Fan
# Library Light
# Light_Sensor
# Mop Floor
# Motion_Sensor
# Opendoor DemoArea
# Open Office
# OP Director's Fan
# OP Director's Light
# reception
# Frontdesk fan
# Reception fan2
# Reception fan3
# Frontdesk light
# Recording Fan
# Recording Light
# Restroom1 Light
# Restroom2 Light
# test5
# test_light1
# test_sw mahesh updated
# Turnoff Director
# Turn On Fan 1
# Turn OFF All Lights
# Water_Sensor1
#  -------------------------------------------------------
# CurtainClose
# CurtainDown
# CurtainOpen
# CurtainUp 
# curtain_down
# curtain_up
# demoarealightandfan
# DemoArea_door
# DemoArea_door1
# DemoArea_fan
# DemoArea_light
# Dining_fan
# Dining_light
# Dir_fan
# Dir_light
# g4g_fan
# g4g_light
# Hc_fan1
# Hc_fan2
# Hc_Led_lights
# Hc_light
# iotall
# Iot_fan1
# Iot_fan2
# Iot_light
# josh01
# Kitchen_light
# Library_fan
# Library_light
# Light_Sensor1
# MopFloor
# Motion_Sensor1
# Opendoor_DemoArea
# Open_office
# OpsDir_fan
# OpsDir_light
# reception
# Recep_fan1
# Recep_fan2
# Recep_fan3
# Recep_light1
# Rec_fan
# Rec_light
# Restrm_light_1
# Restrm_light_2
# test5
# test_light1
# test_sw_mahesh
# turnoffDirector
# TurnOnFan1
# Turn_OFF_All_Lights
# Water_Sensor1
