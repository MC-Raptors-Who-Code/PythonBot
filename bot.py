#!/usr/bin/env python3
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# loads the token from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = "!") 

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Studying..."))
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


# simple ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)} ms')


# loads all the extensions
for filename in os.listdir('./cogs'):
    if( filename.endswith('.py')):
        bot.load_extension(f'cogs.{filename[:-3]}')
# runs the bot
bot.run(TOKEN)
