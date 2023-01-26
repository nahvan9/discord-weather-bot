import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

import utils 
from database import Database

intents = discord.Intents.all()
load_dotenv()

bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)

TOKEN = os.getenv('DISCORD_TOKEN')
APIKEY= os.getenv('WEATHERAPI')

USERDB_DESC = """CREATE TABLE IF NOT EXISTS users(
                    discordID TEXT NOT NULL, 
                    location TEXT NOT NULL
                );"""
                
@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to Discord!')
    # Connect to sqlite db 
    userNameDB = Database(".\\db\\userlocations.db", USERDB_DESC)
    print('db created at .\\db\\userlocations.db')



@bot.command(name='weather')
async def weather(ctx, arg, *args):
    guildID = ctx.message.guild.id
    add =' '
    for a in args:
        add += a+' '
    location = arg+add

    try:
        msg = utils.getWeather(APIKEY, location=location)
    except:
        msg = 'oops! Invalid location. '
        
    # Delete messages if in a server
    try:
        await ctx.message.delete()
        await ctx.send(f'The weather near {location} is...', delete_after=30)
        await ctx.send(msg, delete_after=30)
    
    # Don't delete in DMs
    except:
        await ctx.send(f'The weather near {location} is...')
        await ctx.send(msg)


@bot.command(name='origin')
async def orogin(ctx):
    await ctx.send(f'My birthplace: https://github.com/nahvan9/discord-weather-bot')

bot.run(TOKEN)