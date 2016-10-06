import os
import aiml

bot = aiml.Kernel()

bot.bootstrap(learnFiles = "startup.xml", commands = "LOAD ALICE")
bot.saveBrain("bot_brain.brn")
