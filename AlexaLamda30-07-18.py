
from __future__ import print_function
import json
from botocore.vendored import requests
#import requests
import time
# --------------- Helpers that build all of the responses ----------------------
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------
def get_switch_on(switchname):
    getidindex = None
    API_ENDPOINT = "https://123.176.44.4/service/get_device"
    data = {'username':'admin','password':'admin'}
    data1=json.dumps(data)
    r = requests.post(url = API_ENDPOINT, data = data1,verify=False)
    req1 = r.text
    o = json.loads(req1)
    swnameArray=[]
    swidArray=[]
    for rec in o['device_details'] :
        swnameArray.append(rec['switch_name'])
        swidArray.append(rec['switch_id'])
    
    for i in swnameArray:
        j=i.lower()
        if j==switchname:
            getidindex=swnameArray.index(i)
    switchid=swidArray[getidindex]
    API_ENDPOINT2 = "https://123.176.44.4/service/device"
    data2 = {'username':'admin','password':'admin','switch_id':switchid,'operation':'ON'}
    data3=json.dumps(data2)
    req2 = requests.post(url = API_ENDPOINT2, data = data3,verify=False)
    res = req2.text
    res = json.loads(res)
    errorcode=res['error_code']
    speach=''
    if errorcode==str(0):
        speach="successfully perform ON operation for : "+switchname
    else:
        speach="unable to operate device operation for : "+switchname
    session_attributes = {}
    card_title = "Test"
    #speech_output = "This is switch on function : "+switchname
    speech_output = speach
    reprompt_text = "You never responded to the first test message. Sending another one."
    print("switch on funtion")
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
      
      

        
def get_switch_off(switchname):
    getidindex = None
    
    API_ENDPOINT = "https://123.176.44.4/service/get_device"
    data = {'username':'admin','password':'admin'}
    data1=json.dumps(data)
    r = requests.post(url = API_ENDPOINT, data = data1,verify=False)
    req1 = r.text
    o = json.loads(req1)
    swnameArray=[]
    swidArray=[]
    for rec in o['device_details'] :
        swnameArray.append(rec['switch_name'])
        swidArray.append(rec['switch_id'])
    
    for i in swnameArray:
        j=i.lower()
        if j==switchname:
            getidindex=swnameArray.index(i)
    switchid=swidArray[getidindex]
    API_ENDPOINT2 = "https://123.176.44.4/service/device"
    data2 = {'username':'admin','password':'admin','switch_id':switchid,'operation':'OFF'}
    data3=json.dumps(data2)
    req2 = requests.post(url = API_ENDPOINT2, data = data3,verify=False)
    res = req2.text
    res = json.loads(res)
    errorcode=res['error_code']
    speach=''
    if errorcode==str(0):
        speach="successfully perform OFF operation for : "+switchname
    else:
        speach="unable to operate device operation for curtain : "+switchname
    session_attributes = {}
    card_title = "Test"
    #speech_output = "This is switch on function : "+switchname
    speech_output = speach
    reprompt_text = "You never responded to the first test message. Sending another one."
    print("switch off funtion")
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
        
        
def get_switch_curtain(switchname):
    getidindex = None
    swtype='curtain '+switchname
    operation_name=''
    if switchname=="up" or switchname=="open":
        operation_name='ON'
    elif switchname=="down" or switchname=="close":
        operation_name='OFF'
    API_ENDPOINT = "https://123.176.44.4/service/get_device"
    data = {'username':'admin','password':'admin'}
    data1=json.dumps(data)
    r = requests.post(url = API_ENDPOINT, data = data1,verify=False)
    req1 = r.text
    o = json.loads(req1)
    swnameArray=[]
    swidArray=[]
    for rec in o['device_details'] :
        swnameArray.append(rec['switch_name'])
        swidArray.append(rec['switch_id'])
    
    for i in swnameArray:
        j=i.lower()
        if j==swtype:
            getidindex=swnameArray.index(i)
    switchid=swidArray[getidindex]
    API_ENDPOINT2 = "https://123.176.44.4/service/device"
    data2 = {'username':'admin','password':'admin','switch_id':switchid,'operation':operation_name}
    data3=json.dumps(data2)
    req2 = requests.post(url = API_ENDPOINT2, data = data3,verify=False)
    res = req2.text
    res = json.loads(res)
    errorcode=res['error_code']
    speach=''
    if errorcode==str(0):
        speach="successfully curtain : "+switchname+" Ok"
    else:
        speach="unable to operate curtain "+switchname+" operation"
    session_attributes = {}
    card_title = "Test"
    #speech_output = "This is switch on function : "+switchname
    speech_output = speach
    reprompt_text = "You never responded to the first test message. Sending another one."
    print("curtain funtion")
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))



def get_switch_number(switchname):
    # getidindex = None
    # swtype='curtain '+switchname
    # operation_name=''
    # if switchname=="up" or switchname=="open":
    #     operation_name='ON'
    # elif switchname=="down" or switchname=="close":
    #     operation_name='OFF'
    # API_ENDPOINT = "https://123.176.44.4/service/get_device"
    # data = {'username':'admin','password':'admin'}
    # data1=json.dumps(data)
    # r = requests.post(url = API_ENDPOINT, data = data1,verify=False)
    # req1 = r.text
    # o = json.loads(req1)
    # swnameArray=[]
    # swidArray=[]
    # for rec in o['device_details'] :
    #     swnameArray.append(rec['switch_name'])
    #     swidArray.append(rec['switch_id'])
    
    # for i in swnameArray:
    #     j=i.lower()
    #     if j==swtype:
    #         getidindex=swnameArray.index(i)
    # switchid=swidArray[getidindex]
    # API_ENDPOINT2 = "https://123.176.44.4/service/device"
    # data2 = {'username':'admin','password':'admin','switch_id':switchid,'operation':operation_name}
    # data3=json.dumps(data2)
    # req2 = requests.post(url = API_ENDPOINT2, data = data3,verify=False)
    # res = req2.text
    # res = json.loads(res)
    # errorcode=res['error_code']
    # speach=''
    # if errorcode==str(0):
    #     speach="successfully curtain : "+switchname+" Ok"
    # else:
    #     speach="unable to operate curtain "+switchname+" operation"
    speach="this is number switch intent"+switchname
    session_attributes = {}
    card_title = "Test"
    #speech_output = "This is switch on function : "+switchname
    speech_output = speach
    reprompt_text = "You never responded to the first test message. Sending another one."
    print("curtain funtion")
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))




def get_switch_not():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    
    session_attributes = {}
    card_title = "Test"
    speech_output = "This switch is not exists"
    reprompt_text = "You never responded to the first test message. Sending another one."
    print("mahesh babu hi")
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))




def get_switch_response(msg):
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "Test"
    speech_output = "This switch name : "+msg
    reprompt_text = "You never responded to the first test message. Sending another one."
    print("mahesh babu hi")
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to JTS Demo House!"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I don't know if you heard me, welcome to your custom alexa application!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific 
        variables from a previous state stored in an external database
    """
    # Add additional code here as needed
    pass

    

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    # Dispatch to your skill's launch message
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    
    
    #intent_speach = intent_request['intent']['slots']['switchname']['value']#getting text what user talk
    intent_name= intent_request['intent']['name'] #intent name 
    #intent_value='type' in intent['slots']
    #intent_value=intent_request['intent']['slots']['switchname']['resolutions'] #name of the intent 
    # if 'switchname' in intent['slots']:
    #     intent_value = intent['slots']['switchname']['value']
    

    #return get_switch_response(str(intent_value))

    # Dispatch to your skill's intent handlers
    
    if intent_name == "switchOn":
        if 'switchname' in intent['slots']:
         intent_value = intent['slots']['switchname']['value']
        return get_switch_on(str(intent_value))
    elif intent_name == "switchOff":
        if 'switchname' in intent['slots']:
         intent_value = intent['slots']['switchname']['value']
        return get_switch_off(str(intent_value))
    elif intent_name == "curtain":
        if 'operation' in intent['slots']:
         intent_value = intent['slots']['operation']['value']
        return get_switch_curtain(str(intent_value))
    elif intent_name == "swnumber":
        if 'numberswitch' in intent['slots']:
         intent_value = intent['slots']['operation']['value']
        return get_switch_number(str(intent_value))
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    
    else:
        #this.event.request.intent.slots.<yourslotname>.resolutions.resolutionsPerAuthority[0].values[0].value.name
        return get_switch_not()
    # else:
    #     raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("Incoming request...")
    
    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")
    try:
        if event['session']['new']:
            on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

        if event['request']['type'] == "LaunchRequest":
            return on_launch(event['request'], event['session'])
        elif event['request']['type'] == "IntentRequest":
            return on_intent(event['request'], event['session'])
        elif event['request']['type'] == "SessionEndedRequest":
            return on_session_ended(event['request'], event['session'])
    except Exception,e:
        raise e
        #return get_switch_not()
    
