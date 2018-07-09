# Steve Jobs discord bot

import os
import random
import socket
import time

from discord import Game
from discord.ext.commands import Bot
import requests

import config

socket.setdefaulttimeout(5)

client = Bot(command_prefix=config.BOT_PREFIX)

@client.command(name='iTunes',
                description='Describes iTunes on Windows',
                brief='Describes iTunes',
                aliases='',
                pass_context=True)
async def itunes(context):
    await client.say('iTunes on Windows is like giving a cold glass of water to someone in hell, '+ context.message.author.mention)
    await client.send_typing(context.message.channel)
    time.sleep(5)
    await client.say('https://www.youtube.com/watch?v=Vp18clQ1tjE')


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


@client.command(name='windows',
                description='Describes Microsoft Windows',
                brief='Describes Microsoft Windows',
                aliases='',
                pass_context=True)
async def windows(context):
    # Use os.listdir to list the files in the meme dir, and then send one of them at random to the channel
    path = './img/windows/'
    choices = os.listdir(path)
    img = random.choice(choices)
    await client.send_file(context.message.channel, f'{path}{img}')


@client.command(name='where',
                description='Returns where the bot is currently being hosted/ran',
                brief='Returns the bot\'s IP',
                aliases='',
                pass_context=True)
async def where():
    response = requests.get('https://www.icanhazip.com/')
    ip = response.text
    host = socket.getfqdn(ip)
    await client.say(f'This bot is currently running at {ip}')
    await client.say(f"Reverse lookup shows the hostname to be {host}")


@client.command(name='whoami',
                description='Testing purposes only.',
                brief='Testing purposes only',
                aliases='',
                pass_context=True)
async def whoami(context):
    iam = context.message.author.id
    await client.say(f'You have been detected as "{iam}"')


@client.command(name='quit',
                description='Ends the process, immediately killing the bot. You probably do not have access to do this.',
                brief='Tells Steve to go away',
                aliases='',
                pass_context=True)
async def quit(context):
    sentby = context.message.author.id
    if sentby == config.BOT_OWNER:
        await client.say('Disconnecting immediately, '+ context.message.author.mention)
        time.sleep(1)
        exit(0)
    else:
        await client.say('Who are you and why should I care?')


@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('---------------')
    await client.change_presence(game=Game(name='Apple II'))

client.run(config.TOKEN)