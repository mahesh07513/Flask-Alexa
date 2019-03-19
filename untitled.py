from flask import Flask
from flask_ask import Ask,statement,question,session,convert_errors
import json
import requests
import time
import unidecode


app = Flask(__name__)
ask = Ask(app, "/jochebed")
#logging.getLogger('flask_ask').setLevel(logging.DEBUG)
swid= []
swid=range(0)
swnum=[]
swnum=range(0)
num=''

def get_details(switchname):

    print "----------------------------------------"
    print "this is sw name :",switchname
    
    sw1=switchname[:3]+switchname[-3:]
    print "......",sw1
    # defining the api-endpoint 
    API_ENDPOINT = "https://jtsha.in/service/get_device"
    #API_ENDPOINT="http://192.168.10.97/service/get_device"
    # data to be sent to api
    #print API_ENDPOINT
    data = {'username':'mahesh','password':'mahesh12'}
    #print(data)
    data1=json.dumps(data)
    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = data1)
    # extracting response text 
    pastebin_url = r.text
    #print("The pastebin URL is:%s"%pastebin_url)
    o = json.loads(pastebin_url)
    #print(o)
    
    #print o['device_details']
    swnameArray=[]
    swidArray=[]
    for rec in o['device_details'] :
        #print rec['switch_name']
        swnameArray.append(rec['switch_name'])
        swidArray.append(rec['switch_id'])

        
    #print "name array is ", swnameArray
    #print "id array is ", swidArray
    getidindex=0
    for i in swnameArray:
    	#print "in side for name arry"
    	j=i.lower()
    	#print "char : ",j
    	k=j[:3]+j[-3:]
    	#print "com : ",k
    	if k==sw1:
    	   #print "inside compare"
    	   getidindex=swnameArray.index(i)

        # #i=i.lower()
        # #print "...",i
        # if i.lower()==switchname:
        #    #print "inside compare"
        #    getidindex=swnameArray.index(i)
    swid.append(swidArray[getidindex])
    print "swid......",swid[0]
    return switchname
    #print swnameArray.index(switchname.lower)
    #print "this sw id ",swnumber
    # switchname1=swidArray[getidindex]
    # print "this is sw number ",switchname1,operation
    # switchname2=''
    # if operation=="on":
    #     switchname2=operateSwitchOn(switchname1)
    # else:
    #     switchname2=operateSwitchOff(switchname1)
    # print "response :",switchname2
    # return switchname2

    
def get_operation(operation):

    print "insede.......op ..: ",swid[0]
    print operation
    switchname2=''
    if operation=="on":
        switchname2=operateSwitchOn(swid[0])
    else:
        switchname2=operateSwitchOff(swid[0])
    print "response :",switchname2
    return switchname2


#titles= get_details()
def check():
    string1 = 'Hello'
    string2 = 'hello'

    if string1.lower() == string2.lower():
        print "The strings are the same (case insensitive)"
    else:
        print "The strings are not the same (case insensitive)"
#check()



def operateSwitchOn(switchname):
    

    # defining the api-endpoint
    API_ENDPOINT = "https://jtsha.in/service/device"
    #API_ENDPOINT = "http://192.168.10.97/service/device"
    # data to be sent to api

    data = {'username':'mahesh','password':'mahesh12','switch_id':switchname,'operation':'ON'}
    data1=json.dumps(data)
    print "url  :",API_ENDPOINT
    print "json string :",data

    
    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = data1)
    # extracting response text
    pastebin_url = r.text
    print("The Response is:%s"%pastebin_url)
    o = json.loads(pastebin_url)
    print(o['error_code'])
    num=None
    return o['error_code']

def operateSwitchOff(switchname):
    
    # defining the api-endpoint
    API_ENDPOINT = "https://jtsha.in/service/device"
    #API_ENDPOINT = "http://192.168.10.97/service/device"
    # data to be sent to api
    data = {'username':'mahesh','password':'mahesh12','switch_id':switchname,'operation':'OFF'}
    data1=json.dumps(data)
    print "url  :",API_ENDPOINT
    print "json string :",data
    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = data1)
    # extracting response text
    pastebin_url = r.text
    print("The Response is:%s"%pastebin_url)
    o = json.loads(pastebin_url)
    print(o['error_code'])
    num=None
    return o['error_code']


def get_headlines():
    user_pass_dict = {'username':'admin','password':'admin','api_type':'json'}
    sess =  requests.Session()
    sess.headers.update({'User-Agent':'I am testing alexa'})
    sess.post('https://dev.jtsha.in/service/validate_web',data=user_pass_dict)
    #sess.post('https://192.168.10.97/service/validate_web',data=user_pass_dict)
    time.sleep(1)
    url = 'https://www.reddit.com/r/worldnews/.json?limit=10'
    html = sess.get(url)
    data= json.loads(html.content.decode('utf-8'))
    titles = [unidecode.unidecode(listing['data']['title']) for listing in data['data']['children']]
    #titles=[]
    #for listing in data['data']['children']:
    #   unidecode.unidecode(listing['data']['title'])
    titles='... '.join([i for i in titles])
    return titles

def p2bool(preference):
    
    if preference == 'do':
        return True
    elif preference == 'do not':
        return False
    else:
        raise ValueError("must be do or do not")




#titles= operateSwitch()
#print(titles)


#titles= get_headlines()
#print(titles)

#########################Intents########################
@app.route('/')
def homepage():
    return "hi this is mahesh from ifttt"



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
