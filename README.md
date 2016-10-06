# Alexa-AIML-Chatbot

A demo of a simple AIML chatbot.  The chatbot will respond to whatever you say, sometimes correctly, other times not. To end the chat, say Stop or Cancel.

This is my first attempt at making an AIML chatbot, so I am sure there are ways to improve it.

Instructions:

Zip the contents of the src folder and upload to AWS Lambda. 

The configuration is Runtime: Python 2.7, Handler: index.lambda_handler, Existing Role: lambda_basic_execution. In the Advanced settings, set the timeout to 20 seconds.

In the Amazon Developer Console, use the files from the speechAssets folder, you will need to make a custom slot named CHATTER and fill the slots with random words and phrases.

If you want to modify the bot_brain, put the files, build.py, std-startup.xml, and folders alice and standard into a folder (ie: Build).  Move the .aiml files you want to use into the Build folder.  In the Terminal, cd to the folder, then enter the command python build.py, this should build the bot_brain.brn file.

Known issues: the bot_brain is loaded each time, you make a statement, so the more AIML files you add to the bot_brain, the longer the delay in responding.  Sessions is not working, so the bot will not remember things.  

Hopefully, someone more experienced could help me solve those issues.


