# Steve Jobs discord bot

import discord
import config

client = discord.Client()

@client.event
async def on_message(message):
    # Do not allow the bot to reply to itself 
    if message.author == client.user:
        return

    if message.content.startswith('!itunes'):
        msg = 'iTunes on Windows is like giving a cold glass of water to someone in hell, {0.author.mention}.'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------------')

client.run(config.TOKEN)