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
ask = Ask(app, "/")
#logging.getLogger('flask_ask').setLevel(logging.DEBUG)
swid= []
swid=range(0)
swnum=[]
swnum=range(0)

getidindex=None
num=''
swname=''
checknum=False
def get_detailsNum():
    
    # defining the api-endpoint 
    #API_ENDPOINT="http://192.168.10.97/service/get_device"
    #API_ENDPOINT = "https://123.176.44.4/service/get_device"
    API_ENDPOINT = "https://jtsha.in/service/get_device"
    # data to be sent to api
    data = {'username':'mahesh','password':'mahesh12'}
    #print API_ENDPOINT
    #data = {'username':'admin','password':'admin'}
    #print(data)
    data1=json.dumps(data)
    # sending post request and saving response as response object
    session = requests.Session()
    session.verify = False
    r = session.post(url = API_ENDPOINT, data = data1)
    # extracting response text 
    pastebin_url = r.text
    print "The response is:",pastebin_url
    o = json.loads(pastebin_url)
    return o
get_detailsNum=get_detailsNum()
print get_detailsNum


#########################Intents########################
@app.route('/')
def homepage():
    return "hi this is mahesh"


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='123.176.44.4', port=3780)