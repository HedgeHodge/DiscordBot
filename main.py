# Import libraries
import os
import random
import re
import discord

# Make connection to Discord using token from .env
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

# Set up list of words to use
responseList = ['ADULT', 'CHILD', 'E', 'YEET', 'BEHIND', 'NEAR', 'FAR']

print("Thomas is ready for scarebears...")

# Get message event
@client.event
async def on_message(message):

    # Bail if message is sent from the bot itself
    if message.author == client.user:
        return

    # Remove punctuation from messages
    message = re.sub(r'[^\w\s]', '', message)

    # Make list of words from the message event
    wordList = message.content.lower().split(' ')
    print(wordList)

    # Response accordingly 
    if 'old' in wordList or 'age' in wordList:
        response = responseList[random.randrange(0, 2)]
        await message.channel.send(response)
    elif 'where' in wordList or 'here' in wordList:
        response = responseList[random.randrange(4, 6)]
        await message.channel.send(response)
    else:
        response = responseList[random.randrange(0, 6)]
        await message.channel.send(response)

client.run(TOKEN)

