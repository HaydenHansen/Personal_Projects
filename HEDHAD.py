# HEDHAD V1.1.2
# This is the HEDHAD discord bot made by Hayden Hansen, Ethan Anderson, and Drake Davis! Enjoy!
import os
import random
import discord
import json
import requests
from discord.ext.commands import Bot
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
KEY = os.getenv('TENOR_KEY')
bot = Bot(command_prefix='!')
limit = 8
# TOKEN and GUILD refer to your own token and guild name that should be in a .env file
client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

# The code below runs the ! commands and monitors message content in order to run those commands
# the await is to ensure that it waits for the message to be done before it sends it and the message.author == client
# .user is to make sure its a human and not a bot doing the commands
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    random_words = [
        'I\'m the human form of the 100 emoji.',
        'Bingpot!',
        'lets do this together',
        'drake is ultra man',
        'ethan is drippy',
        'chasen likes snails',
        'hayden is cool',
        'vicky is icy',
        'TJ is a master chef',
        'Nestor is the sax man',
    ]

    PasswordContents = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z',
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '{',
        '}',
        '!',
        '[',
        ']',
    ]
    if message.content == '!random':
        response = random.choice(random_words)
        await message.channel.send(response)
    elif message.content == '!test':
        response = 'just sending you a message'
        await message.author.send(response)
    elif message.content == '!pacer':
        response = 'The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets ' \
                'more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at ' \
                'the start. The running speed starts slowly, but gets faster each minute after you hear this ' \
                'signal. A single lap should be completed each time you hear this sound.  Remember to run in a ' \
                'straight line, and run as long as possible. The second time you fail to complete a lap before the '\
                'sound, your test is over. The test will begin on the word start.'
        await message.channel.send(response)
        response = 'On your mark'
        await message.channel.send(response)
        response = 'Get ready'
        await message.channel.send(response)
        response = 'Start'
        await message.channel.send(response)
    elif message.content == '!poggers':
        response = 'https://tenor.com/view/pingu-poggers-pingu-poggers-gif-19868149'
        await message.channel.send(response)
    elif 'baka' in message.content.lower():
            response = 'sus'
            await message.channel.send(response)
    elif message.content == '!roulette':
        number = random.randint(1, 6)
        if number == 1:
            response = 'Sheeeeeesh, unlucky kid'
            await message.channel.send(response)
            response = 'https://tenor.com/view/dead-gif-18865199'
            await message.channel.send(response)
        else:
            response = 'nothing special, you lived.'
            await message.channel.send(response)
    elif message.content == '!GeneratePassword':
        x = 0
        password = ""
        while x <= 25:
            password = password + random.choice(password_contents)
            x = x + 1
        response = (password)
        response2 = 'The password was sent to your private dms'
        response3 = 'Make sure to save this password somewhere safe'
        await message.author.send(response)
        await message.channel.send(response2)
        await message.channel.send(response3)
    elif message.content == '!Gif':
        search_term = 'poggers'
        r = requests.get(
            "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, KEY, limit))
        if r.status_code == 200:
            top8gifs = (json.load(r.content))
            print(top8gifs)
        else:
            print('oops')


client.run(TOKEN)
