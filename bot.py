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
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("In a Meeting..."))
    print(f'{bot.user} has connected to Discord!')

# Function to list all available gears 
@bot.command()
async def listCogs(ctx):
    outStrActive = ""
    outStrDisabled = ""
    for filename in os.listdir('./cogs'):
        if(filename.endswith('.py')):
            outStrActive += f'-{filename[:-3]}\n'
        elif(filename.endswith('.py.disabled')):
            outStrDisabled += f'-{filename[:-12]}\n'
    if(outStrActive == ""):
        outStrActive = "-none\n";
    if(outStrDisabled == ""):
        outStrDisabled = "-none\n";    
    await ctx.send(f'```\nAVAILABLE\n{outStrActive}DISABLED\n{outStrDisabled}```')

# commands for loading and unloading cogs once the bot is running
@bot.command()
async def unload(ctx, extension):
    extension = extension.lower()
    if(not (extension == "all")):
        try:
            bot.unload_extension(f'cogs.{extension}')
            await ctx.send(f'`Cog {extension} successfully unloaded`')
        except commands.errors.ExtensionNotLoaded:
            await ctx.send(f'`Cog {extension} was not initally loaded`')
    else:
        for filename in os.listdir('./cogs'):
            if( filename.endswith('.py')):
                try:
                    bot.unload_extension(f'cogs.{filename[:-3]}')
                except commands.errors.ExtensionNotLoaded:
                    pass
        await ctx.send('`All cogs successfully unloaded`')


@bot.command()
async def load(ctx, extension):
    extension = extension.lower()
    if(not (extension == "all")):
        try:
            bot.load_extension(f'cogs.{extension}')
            await ctx.send(f'`Cog {extension} successfully loaded`')
        except discord.ext.commands.errors.ExtensionNotFound:
            await ctx.send(f'`Cog {extension} not found`')
    else:
        for filename in os.listdir('./cogs'):
            if( filename.endswith('.py')):
                bot.load_extension(f'cogs.{filename[:-3]}')
        await ctx.send('`All cogs successfully loaded`')

@bot.command()
async def reload(ctx, extension):
    await unload(ctx, extension)
    await load(ctx, extension)

# commands for disabling and enabling cogs
@bot.command()
async def disableCog(ctx, extension):
    extension = extension.lower()
    await unload(ctx, extension)
    if(os.path.isfile(f'./cogs/{extension}.py')):
        os.rename(f'./cogs/{extension}.py',f'./cogs/{extension}.py.disabled')
        await ctx.send(f'`Cog {extension} successfully disabled`')
    else:
        pass

@bot.command()
async def enableCog(ctx, extension):
    extension = extension.lower()
    if(os.path.isfile(f'./cogs/{extension}.py.disabled')):
        os.rename(f'./cogs/{extension}.py.disabled',f'./cogs/{extension}.py')
        await ctx.send(f'`Cog {extension} successfully enabled`')
    else:
        pass

# simple ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f'`Pong! {round(bot.latency * 1000)} ms`')


# loads all the extensions initally 
for filename in os.listdir('./cogs'):
    if( filename.endswith('.py')):
        bot.load_extension(f'cogs.{filename[:-3]}')

# runs the bot
bot.run(TOKEN)
