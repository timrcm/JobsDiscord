# Steve Jobs discord bot
# Python 3.6.6

import datetime
import os
import random
import socket
import time

from discord import Game
from discord.ext.commands import Bot
import requests

import config
import repeats

socket.setdefaulttimeout(5)
client = Bot(command_prefix=config.BOT_PREFIX, pm_help=True)


@client.command(name='android',
                description='Describes Android',
                brief='Describes Android',
                aliases='',
                pass_context=True)
async def android(context):
    path = './content/reactions/'
    choices = os.listdir(path)
    r = ''

    while r != 1:
        img = random.choice(choices)
        r = repeat_check(repeats.reactions, img)

    await client.send_file(context.message.channel, f'{path}{img}')

    repeat_block(repeats.reactions, repeats.usable_reactions, img)

@client.command(name='appl',
                description='Proivdes the current market valuation of Apple',
                brief='Checks Apple\'s market value',
                aliases='',
                pass_context=True)
async def appl(context):
    # Uses pandas_datareader.data to spit out Apple's current stock value, number of shares, & market cap
    # Maybe use Alpha Vantage instead? 
    await client.say("This command is a work in progress. Suffice it to say, Apple is worth... a lot.")
    pass

@client.command(name='itunes',
                description='Describes iTunes on Windows',
                brief='Describes iTunes',
                aliases='iTunes',
                pass_context=True)
async def itunes(context):
    await client.say('iTunes on Windows is like giving a cold glass of water to someone in hell, '+ context.message.author.mention)
    await client.send_typing(context.message.channel)
    time.sleep(2)
    await client.say('https://www.youtube.com/watch?v=Vp18clQ1tjE')


@client.command(name='bitcoin',
                description='Returns the current bitcoin price from Coinbase',
                brief='Displays the current bitcoin price',
                aliases='',
                category='Currency',
                pass_context=True)
async def bitcoin(context):
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
    value = response.json()['bpi']['USD']['rate']
    await client.say(f'The current Bitcoin price is: {value}')
    # diff =  
    await client.say(f'At a current market cap of $924 billion dollars, that makes a bitcoin worth 0.000000007327922% of Apple.')
    await client.say(f'Boy, that\'s a lot of 0s...')
    await client.send_typing(context.message.channel)
    time.sleep(2)
    await client.say('rofl fake money...')


@client.command(name='windows',
                description='Describes Microsoft Windows',
                brief='Describes Microsoft Windows',
                aliases='',
                pass_context=True)
async def windows(context):
    # Use os.listdir to list the files in the meme dir, and then send one of them at random to the channel
    path = './content/windows/'
    choices = os.listdir(path)
    w = ''

    # Use the repeat_check function to look for repeats endlessly until one is found 
    while w != 1:
        img = random.choice(choices)
        w = repeat_check(repeats.windows, img)

    # Send the meme of choice, and then block it from being repeated by future uses of the command
    await client.send_file(context.message.channel, f'{path}{img}')
    repeat_block(repeats.windows, repeats.usable_windows, img)

    # Fake typing 
    await client.send_typing(context.message.channel)
    time.sleep(2)

    # Now, send a reaction to the meme, avoiding repeats again 
    path = './content/reactions/'
    choices = os.listdir(path)
    r = ''

    while r != 1:
        img = random.choice(choices)
        r = repeat_check(repeats.reactions, img)

    await client.send_file(context.message.channel, f'{path}{img}')
    repeat_block(repeats.reactions, repeats.usable_reactions, img)


    # Anndddd send a 'response' / quote, avoiding repeats here as well 
    i = ''
    while i != 1:
        with open('./content/responses.txt', 'r') as f:
            response = random.choice(f.read().splitlines())
            i = repeat_check(repeats.responses, response)

    await client.say(response + ', ' + context.message.author.mention)
    repeat_block(repeats.responses, repeats.usable_responses, response)


@client.command(name='meme',
                description='Be graced with a meme from Mr. Jobs himself',
                brief='Be graced with a meme from Mr. Jobs himself',
                aliases='',
                pass_context=True)
async def meme(context):
    # Use os.listdir to list the files in the meme dir, and then send one of them at random to the channel
    path = './content/memes/'
    choices = os.listdir(path)
    w = ''

    # Use the repeat_check function to look for repeats endlessly until one is found 
    while w != 1:
        img = random.choice(choices)
        w = repeat_check(repeats.memes, img)

    # Send the meme of choice, and then block it from being repeated by future uses of the command
    await client.send_file(context.message.channel, f'{path}{img}')
    repeat_block(repeats.memes, repeats.usable_memes, img)


@client.command(name='quote',
                description='Provides an inspirational quote from Steve Jobs himself',
                brief='Provides an inspirational quote from Steve Jobs himself',
                aliases='',
                pass_context=True)
async def quote(context):
    # Pick a random quote in the text file, and spam it out to the channel 
        a = ''
        while a != 1:
            with open('./content/quotes.txt', 'r') as f:
                quote = random.choice(f.read().splitlines())
                a = repeat_check(repeats.quotes, quote)

        await client.say(f"\"{quote}\"")
        await client.send_typing(context.message.channel)
        time.sleep(2)
        await client.say("-Steven Paul Jobs")

        repeat_block(repeats.quotes, repeats.usable_quotes, quote)


@client.command(name='where',
                description='Returns where the bot is currently being hosted/ran',
                brief='Returns the bot\'s IP',
                aliases='',
                pass_context=True)
async def where(context):
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
    if context.message.author.id == config.BOT_OWNER:
        await client.say('Disconnecting immediately, '+ context.message.author.mention)
        time.sleep(1)
        exit(0)
    else:
        await client.say('Who are you and why should I care?')


def repeat_block(c_type, c_type_max, selected):
    '''Blocks repeats of content-driven commands for X many runs of that command'''

    if len(c_type) >= c_type_max:
        c_type.pop(0)

    c_type.append(selected)

def repeat_check(c_type, c_selected):
    '''Checks for repeats of content-driven commands - see repeat_block for more info''' 

    if c_selected in c_type:
        answer = 0
    else:
        answer = 1

    return answer


@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('---------------')
    await client.change_presence(game=Game(name='Apple II'))


if __name__ == '__main__':
    client.run(config.TOKEN)
