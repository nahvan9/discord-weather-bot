import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

import utils 

intents = discord.Intents.all()
load_dotenv()

bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)

TOKEN = os.getenv('DISCORD_TOKEN')
APIKEY= os.getenv('WEATHERAPI')

@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to Discord!')

@bot.command(name='weather')
async def weather(ctx, arg, *args):
    delAfter = 30
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
        await ctx.message.delete(delay=delAfter)
        await ctx.send(f':umbrella2: The weather near {location} is...', delete_after=delAfter)
        await ctx.send(msg, delete_after=delAfter)
    
    # Don't delete in DMs
    except:
        await ctx.send(f':umbrella2: The weather near {location} is...')
        await ctx.send(msg)


@bot.command(name='origin')
async def orogin(ctx):
    await ctx.send(f'My birthplace: https://github.com/nahvan9/discord-weather-bot')

bot.run(TOKEN)