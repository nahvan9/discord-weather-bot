import os
import discord
from dotenv import load_dotenv
from discord import app_commands

import utils 
from database import Database

intents = discord.Intents.all()
load_dotenv()

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client=client)

TOKEN = os.getenv('DISCORD_TOKEN')
APIKEY= os.getenv('WEATHERAPI')

USERDB_DESC = """CREATE TABLE IF NOT EXISTS users(
                    discordID TEXT NOT NULL, 
                    location TEXT NOT NULL
                );"""
                
@client.event
async def on_ready():
    print(f'{client.user.name} is connected to Discord!')
    # Connect to sqlite db 
    userNameDB = Database(".\\db\\userlocations.db", USERDB_DESC)
    print('db created at .\\db\\userlocations.db')
    await tree.sync()
    print('synced')

@app_commands.command(name='weather')
async def weather(interaction: discord.interactions, location: str):
    try:
        msg = utils.getWeather(APIKEY, location=location)
    except:
        msg = 'oops! Invalid location. '
        
    # Delete messages if in a server - need to check if in guild, then delay delete. otherwise, don't delete. 
    try:
        await interaction.response.send_message(f':umbrella2: The weather near {location} is...\n{msg}')
    # Don't delete in DMs
    except:
        await interaction.response.send_message(f':umbrella2: The weather near {location} is...\n{msg}')
tree.add_command(weather)

@app_commands.command(name='origin')
async def origin(interaction: discord.Interaction):
    await interaction.response.send_message(f'My birthplace: https://github.com/nahvan9/discord-weather-bot')
tree.add_command(origin)

client.run(TOKEN)