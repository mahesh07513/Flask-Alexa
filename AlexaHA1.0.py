from flask import Flask
from flask_ask import Ask,statement,question,session,convert_errors
import json
import requests
import time
import unidecode

#####Logging############
import logging
# logging.basicConfig(
#      level = logging.INFO,
#      format = '%(asctime)s %(levelname)s %(message)s',
#      filename = 'alexa.log',
#      filemode = 'a')
# logger = logging.getLogger(__name__)



#########################


app = Flask(__name__)
ask = Ask(app, "/jochebed")
#logging.getLogger('flask_ask').setLevel(logging.DEBUG)
getidindex=None
num=''
swname=''
curname=''


def get_detailsNum(switchname):
    global swname,getidindex
    print "----------------------------------------in num"
    print "Your Word is num: ",switchname
    sw1=''
    if len(switchname)>8:
        sw1=switchname[:4]+switchname[-3:]
        print "in if s",sw1
    else:
        sw1=switchname
        print "in else s",sw1
    # defining the api-endpoint 
    #API_ENDPOINT="http://192.168.10.97/service/get_device"
    API_ENDPOINT = "https://123.176.44.4/service/get_device"
    #API_ENDPOINT = "https://jtsha.in/service/get_device"
    # data to be sent to api
    #data = {'username':'mahesh','password':'mahesh12'}
    #print API_ENDPOINT
    data = {'username':'admin','password':'admin'}
    #print(data)
    data1=json.dumps(data)
    # sending post request and saving response as response object
    session = requests.Session()
    session.verify = False
    r = session.post(url = API_ENDPOINT, data = data1)
    # extracting response text 
    pastebin_url = r.text
    #print "The response is:",pastebin_url
    o = json.loads(pastebin_url)
    swnameArray=[]
    swidArray=[]
    for rec in o['device_details'] :
        swnameArray.append(rec['switch_name'])
        swidArray.append(rec['switch_id'])
    print "cam here"
    for i in swnameArray:
        j=i.lower()
        
        if len(j)>8:
            if validateString(j):
                j=j[:-1]
                k=j[:4]+j[-3:]
                #print "in if k :",k
            else:
                k=j[:4]+j[-3:]
                #print "in else : ",k
        else:
            k=j
            #print "this is k value",k
        if k==sw1:
            getidindex=swnameArray.index(i)

    if validateString(swidArray[getidindex]):
        s1=swidArray[getidindex][:-1]
    else:
        s1=swidArray[getidindex]
    swname=s1
    return switchname
def get_details(switchname):
    global swname,getidindex
    print "----------------------------------------"
    print "Your Word is : ",switchname,", ",len(switchname)
    sw1=''
    if len(switchname)>8:
        sw1=switchname[:4]+switchname[-3:]
    else:
        sw1=switchname
        print "name : ",sw1
    # defining the api-endpoint 
    #API_ENDPOINT="http://192.168.10.97/service/get_device"
    API_ENDPOINT = "https://123.176.44.4/service/get_device"
    #API_ENDPOINT = "https://jtsha.in/service/get_device"
    # data to be sent to api
    #data = {'username':'mahesh','password':'mahesh12'}
    #print API_ENDPOINT
    data = {'username':'admin','password':'admin'}
    #print(data)
    data1=json.dumps(data)
    # sending post request and saving response as response object
    session = requests.Session()
    session.verify = False
    r = session.post(url = API_ENDPOINT, data = data1)
    # extracting response text 
    pastebin_url = r.text
    #print("The response is:%s"%pastebin_url)
    o = json.loads(pastebin_url)
    swnameArray=[]
    swidArray=[]
    for rec in o['device_details'] :
        swnameArray.append(rec['switch_name'])
        swidArray.append(rec['switch_id'])
    
    for i in swnameArray:
        j=i.lower()

        if len(j)>8:
            if validateString(j):
                j=j[:-1]
                k=j[:4]+j[-3:]
            else:
                k=j[:4]+j[-3:]
                #print "cut k ",k
        else:
            k=j
            #print "else K",k
        if k==sw1:
            getidindex=swnameArray.index(i)
    # if validateString(swidArray[getidindex]):
    #     s1=swidArray[getidindex][:-1]
    # else:
    #     s1=swidArray[getidindex]
    print "came"
    s1=swidArray[getidindex]
    swname=s1
    print "swname:",swname
    return switchname   
def validateString(s):
    letter_flag = False
    number_flag = False
    for i in s:
        if i.isalpha():
            letter_flag = True
        if i.isdigit():
            number_flag = True
    return letter_flag and number_flag
def get_operation(operation):
    switchname2=''
    if num==None:
        if operation=="on":
            switchname2=operateSwitchOn(swname)
        elif operation=="off":
            switchname2=operateSwitchOff(swname)
    else:
       if operation=="on":
           switchname2=operateSwitchOnNum(swname,num)
       elif operation=="off":
           switchname2=operateSwitchOffNum(swname,num)
    return switchname2
def operateSwitchOn(switchname):
    global swname,logger
    # defining the api-endpoint
    #API_ENDPOINT = "http://192.168.10.97/service/device"
    API_ENDPOINT = "https://123.176.44.4/service/device"
    #API_ENDPOINT = "https://jtsha.in/service/device"
    # data to be sent to api
    data = {'username':'admin','password':'admin','switch_id':switchname,'operation':'ON'}
    data1=json.dumps(data)
    print "url  :",API_ENDPOINT
    print "json string :",data
    # sending post request and saving response as response object
    session = requests.Session()
    session.verify = False
    r = session.post(url = API_ENDPOINT, data = data1)
    # extracting response text
    pastebin_url = r.text
    print("The Response is:%s"%pastebin_url)
    swname=None    
    return o['error_code']
def operateSwitchOff(switchname):
    global swname
    # defining the api-endpoint
    #API_ENDPOINT = "http://192.168.10.97/service/device"
    API_ENDPOINT = "https://123.176.44.4/service/device"
    #API_ENDPOINT = "https://jtsha.in/service/device"
    # data to be sent to api
    data = {'username':'admin','password':'admin','switch_id':switchname,'operation':'OFF'}
    data1=json.dumps(data)
    # sending post request and saving response as response object
    session = requests.Session()
    session.verify = False
    r = session.post(url = API_ENDPOINT, data = data1)
    # extracting response text
    pastebin_url = r.text
    print("The Response is:%s"%pastebin_url)
    o = json.loads(pastebin_url)
    swname=None
    return o['error_code']
def operateSwitchOnNum(switchname,number):
    global swname
    # defining the api-endpoint
    #API_ENDPOINT = "http://192.168.10.97/service/device"
    API_ENDPOINT = "https://123.176.44.4/service/device"
    #API_ENDPOINT = "https://jtsha.in/service/device"
    # data to be sent to api
    data = {'username':'admin','password':'admin','switch_id':switchname+number,'operation':'ON'}
    data1=json.dumps(data)
    print "url  :",API_ENDPOINT
    print "json string :",data
    # sending post request and saving response as response object
    session = requests.Session()
    session.verify = False
    r = session.post(url = API_ENDPOINT, data = data1)
    # extracting response text
    pastebin_url = r.text
    print("The Response is:%s"%pastebin_url)
    o = json.loads(pastebin_url)
    swname=None
    return o['error_code']
def operateSwitchOffNum(switchname,number):
    global swname
    # defining the api-endpoint
    #API_ENDPOINT = "http://192.168.10.97/service/device"
    API_ENDPOINT = "https://123.176.44.4/service/device"
    #API_ENDPOINT = "https://jtsha.in/service/device"
    # data to be sent to api
    data = {'username':'admin','password':'admin','switch_id':switchname+number,'operation':'OFF'}
    data1=json.dumps(data)
    print "url  :",API_ENDPOINT
    print "json string :",data
    # sending post request and saving response as response object
    session = requests.Session()
    session.verify = False
    r = session.post(url = API_ENDPOINT, data = data1)
    # extracting response text
    pastebin_url = r.text
    print("The Response is:%s"%pastebin_url)
    o = json.loads(pastebin_url)
    swname=None
    return o['error_code']

def get_number(number):
    global num
    num=number
    return num
def check():
     op="-1"
     if str(op)=="-1":
        print "equal"
     else:
        print "not equal"
     str1='"mahesh1"'
     print str1
     print str1[:-1]
     
     if str1[:-1].endswith('1'):
        print "hi"
     else:
        print "condition fails"

     pass


    

    
#check()
#########################Intents########################
@app.route('/')
def homepage():
    return "hi this is mahesh"

@ask.intent("SwitchOperate",convert={'switchname':get_details,'operation':get_operation})
def switchOperate(switchname,operation):
    print "11111111111111"
    global num,swname
    num=''
    swname=''
    
    if operation == str(0):
        return statement("successfully performed device operation {}".format(switchname))
    elif str(operation)=="-1":
        return statement("Failed to call device operation {}".format(switchname))
    else:
        return statement("unable to perform device operation Please check once {}".format(switchname))
    raise Exception()

@ask.intent("SwitchOperateNum",convert={'switchname':get_detailsNum,'number':get_number,'operation':get_operation})
def switchOperate(switchname,number,operation):
    print "222222222222222"
    global num,swname
    num=''
    swname=''
    
    if operation == str(0):
        return statement("successfully performed device operation {}".format(switchname))
    elif operation==str(-1):
        return statement("Failed to call device operation {}".format(switchname))
    else:
        return statement("unable to perform device operation Please check once {}".format(switchname))
    raise Exception()
    

@ask.intent("SwitchCurtain",convert={'curop':''})
def switchOperate(curop):
    global getidindex
    data=''
    print "----------------------------------------in Curtain"
    print "33333333333333",curop
    
    swname="curtain "+curop
    print "swname is : ",swname
   
    
    # defining the api-endpoint 
    #API_ENDPOINT="http://192.168.10.97/service/get_device"
    API_ENDPOINT = "https://123.176.44.4/service/get_device"
    #API_ENDPOINT = "https://jtsha.in/service/get_device"
    # data to be sent to api
    #data = {'username':'mahesh','password':'mahesh12'}
    #print API_ENDPOINT
    data = {'username':'admin','password':'admin'}
    #print(data)
    data1=json.dumps(data)
    # sending post request and saving response as response object
    session = requests.Session()
    session.verify = False
    r = session.post(url = API_ENDPOINT, data = data1)
    # extracting response text 
    pastebin_url = r.text
    #print "The response is:",pastebin_url
    o = json.loads(pastebin_url)
    swnameArray=[]
    swidArray=[]
    for rec in o['device_details'] :
        swnameArray.append(rec['switch_name'])
        swidArray.append(rec['switch_id'])
    print "cam here"
    for i in swnameArray:
        j=i.lower()
        if j==swname:
            getidindex=swnameArray.index(i)

    
    s1=swidArray[getidindex]
    API_ENDPOINT = "https://123.176.44.4/service/device"
    #API_ENDPOINT = "https://jtsha.in/service/device"
    # data to be sent to api
    if curop=="up" or curop=="open":
        data = {'username':'admin','password':'admin','switch_id':s1,'operation':'ON'}
    elif curop=="down" or curop=="close":
        data = {'username':'admin','password':'admin','switch_id':s1,'operation':'OFF'}

    data1=json.dumps(data)
    print "url  :",API_ENDPOINT
    print "json string :",data
    # sending post request and saving response as response object
    session = requests.Session()
    session.verify = False
    r = session.post(url = API_ENDPOINT, data = data1)
    # extracting response text
    pastebin_url = r.text
    print("The Response is:%s"%pastebin_url)
    res=o['error_code']
    if res == str(0):
        return statement("successfully performed device operation")
    elif res==str(-1):
        return statement("Failed to call device operation ")
    else:
        return statement("unable to perform device operation Please check once ")
    raise Exception()


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
