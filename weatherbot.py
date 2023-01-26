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
    add =' '
    for a in args:
        add += a+' '
    location = arg+add

    msg = utils.getWeather(APIKEY, location=location)

    await ctx.send(f'The weather near {location} is...', delete_after=30)
    await ctx.send(msg, delete_after=30)
    await ctx.message.delete()

bot.run(TOKEN)