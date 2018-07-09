# Steve Jobs discord bot

import random
import time

from discord import Game
from discord.ext.commands import Bot
import requests

import config

client = Bot(command_prefix=config.BOT_PREFIX)

@client.command(name='iTunes',
                description='Describes iTunes on Windows',
                brief='Describes iTunes',
                aliases='',
                category='Apple',
                pass_context=True)
async def itunes(context):
    await client.say('iTunes on Windows is like giving a cold glass of water to someone in hell, '+ context.message.author.mention)


@client.command(name='bitcoin',
                description='Returns the current bitcoin price from Coinbase',
                brief='Displays the current bitcoin price',
                aliases='',
                category='Currency',
                pass_context=True)
async def bitcoin():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
    value = response.json()['bpi']['USD']['rate']
    await client.say(f'The current Bitcoin price is: {value}')
    # diff =  
    await client.say(f'At a current market cap of $924 billion dollars, that makes a bitcoin worth 0.000000007327922% of Apple.')
    await client.say(f'Boy, that\'s a lot of 0s...')
    time.sleep(2)
    await client.say('rofl fake money...')


@client.command(name='quit',
                description='Ends the process, immediately killing the bot.',
                brief='Tells Steve to go away',
                aliases='',
                category='Apple',
                pass_context=True)
async def quit(context):
    await client.say('Disconnecting immediately, '+ context.message.author.mention)
    time.sleep(1)
    exit(0)
    

@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('---------------')
    await client.change_presence(game=Game(name='Apple II'))

client.run(config.TOKEN)