# Alexa-AIML-Chatbot

A demo of a simple AIML chatbot.  The chatbot will respond to whatever you say, sometimes correctly, other times not.

Instructions:

Zip the contents of the src folder and upload to AWS Lambda. 

The configuration is Runtime: Python 2.7, Handler: index.lambda_handler, Existing Role: lambda_basic_execution. In the Advanced settings, set the timeout to 20 seconds.

In the Amazon Developer Console, use the files from the speechAssets folder, you will need to make a custom slot named CHATTER and fill the slots with random words and phrases.

Known issues: the bot_brain is loaded each time, you make a statement, so the more AIML files you add to the bot_brain, the longer the delay in responding.  Sessions is not working, so the bot will not rememeber things.


