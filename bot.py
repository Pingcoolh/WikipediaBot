import discord
from discord.ext import commands
import asyncio
import requests, bs4

file = open("token.txt", "r")
TOKEN = file.readline().strip()
print(TOKEN)
file.close()

client = commands.Bot(command_prefix = '!')

@client.command()
async def test():
    embed = discord.Embed(title="Test!", description="This is a test.", color=0x1976D2)
    await client.say(embed=embed)

@client.command()
async def ping():
    await client.say("Pong!")

# Wikipedia
@client.command()
async def wikipedia(*name):


def search(search):
    res = requests.get("https://en.wikipedia.org/wiki/Special:Sea
    

@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)
    print('User ID: ' + client.user.id)
    print('Bot is ready')

client.run(TOKEN)