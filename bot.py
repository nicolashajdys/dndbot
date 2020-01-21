import discord
from data.weapon import Character
from rasa_api import call_for

token = 'NjU1MzYxMDIwOTQ4MTE5NTUz.XfTA8g.q6S4VdyMalPmt-5CuH6o8L3OkOI'
client = discord.Client()


@client.event
async def on_ready():
    print('Ready to talk to botsssss')


@client.event
async def on_message(message):
    print(f"{message.author}, {message.content}")
    message_info = call_for(message.content)
    data = message_info['intent']['name']
    if message.author == client.user:
        return
    # check confidence here
    print(data)
    if data == 'create_character':
        Character.createCharacter()
        return True
    elif data == 'attack':
        Character.attack()
        return await message.channel.send('You attack with your weapon')
    else:
        return await message.channel.send(f'We will contact you for the query "{message.content}"')


client.run(token)
