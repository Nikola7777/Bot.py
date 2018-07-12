import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import time

bot = commands.Bot(command_prefix='#')
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Made By Niko#7360'))
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    
    bot.run(os.environ['TOKEN'])
    
