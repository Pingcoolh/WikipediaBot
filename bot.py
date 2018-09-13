import discord
from discord.ext import commands
import asyncio
import requests, bs4

file = open("token.txt", "r")
TOKEN = file.readline().strip()
print(TOKEN)
file.close()

client = commands.Bot(command_prefix = '!')