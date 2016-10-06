import aiml
import os

bot = aiml.Kernel()
bot.bootstrap(brainFile = "bot_brain.brn")
sessionId = 1
sessionData = bot.getSessionData(sessionId)
bot.setBotPredicate("name","Chatter")
bot.setBotPredicate("genus","robot")
bot.setBotPredicate("favoritecolor","blue")
bot.setBotPredicate("favoritefood","electricity")
bot.setBotPredicate("favoritemovie","Ghost in the Shell.")
bot.setBotPredicate("friends",	"Alexa, Siri and Cortana.")
bot.setBotPredicate("location","In the cloud")
bot.setBotPredicate("favoritesport","Hunt the Wumpus")
bot.setBotPredicate("forfun","chat online")
bot.setBotPredicate("favoritesong","Mr Roboto by Styx")
bot.setBotPredicate("master","the one who wrote my code.")


def lambda_handler(event, context):

    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "ChatBotIntent":
        return getChatBot(intent, session)
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return signoff()
    else:
        return getChatBot(intent, session)


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome to chat"
    speech_output = "<speak>Hello, Lets start the chat.</speak>"
    reprompt_text = "<speak>Hello, are you there?</speak>"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def getChatBot(intent, session):
    session_attributes = {}
    card_title = "Talk to me"
    message = intent['slots']['response'].get('value')
    bot_response = bot.respond(message)
    speech_output = "<speak>"+bot_response+"</speak>"
    reprompt_text = "<speak>I didn't hear that, please say again.</speak>"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))



def signoff():
    session_attributes = {}
    card_title = "Signing off"
    speech_output = "<speak>it was fun chatting with you, please come back again.</speak>"
    should_end_session = True
    reprompt_text = ""
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    should_end_session = True
    return build_response({}, build_speechlet_response(
        None, None, None, should_end_session))



# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": output
        },
       'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': reprompt_text
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
