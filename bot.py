#!/usr/bin/env python3
import os
import discord
import json
from discord.ext import commands

'''
- Notes:
- Made a json config instead of a .env file.
-
'''

# make a config if it doesn't already exist
if(not os.path.isfile("./config.json")):
    import setup
    print("Configure the config file, then run again.")
    quit()

# load json config
with open("./config.json", "r") as file:
    config = json.load(file)

# make bot object
bot = commands.Bot(command_prefix = config["prefix"])



# start of core function defs


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(config["status"]))
    print(f'{bot.user} has connected to Discord!')


# Function to list all available gears
@bot.command()
async def listCogs(ctx):
    outStrActive = ""
    outStrDisabled = ""

    # add all found modules to their respective Strings
    for filename in os.listdir('./cogs'):
        if(filename.endswith('.py')):
            outStrActive += f'-{filename[:-3]}\n'
        elif(filename.endswith('.py.disabled')):
            outStrDisabled += f'-{filename[:-12]}\n'

    # cover cases where string would be empty
    if(outStrActive == ""):
        outStrActive = "-none\n"
    if(outStrDisabled == ""):
        outStrDisabled = "-none\n"

    # send over the full string
    await ctx.send(f'```\nAVAILABLE\n{outStrActive}DISABLED\n{outStrDisabled}```')


# commands for loading and unloading cogs once the bot is running
@bot.command()
async def unload(ctx, *extensions):
    # deals with all the modules
    if(extensions[0].lower() == "all"):
        for filename in os.listdir('./cogs'):
            if( filename.endswith('.py')):
                try:
                    bot.unload_extension(f'cogs.{filename[:-3]}')
                except commands.errors.ExtensionNotLoaded:
                    pass
        await ctx.send('`All cogs successfully unloaded`')
        return
    # unloads all the extensions passed
    for extension in extensions:
        extension = extension.lower()
        try:
            bot.unload_extension(f'cogs.{extension}')
            await ctx.send(f'`Cog {extension} successfully unloaded`')
        except commands.errors.ExtensionNotLoaded:
            await ctx.send(f'`Cog {extension} was not initally loaded`')


@bot.command()
async def load(ctx, *extensions):
    # deals with loading all modules
    if(extensions[0].lower() == "all"):
        for filename in os.listdir('./cogs'):
            if( filename.endswith('.py')):
                bot.load_extension(f'cogs.{filename[:-3]}')
        await ctx.send('`All cogs successfully loaded`')
        return

    # unloads the extensions passed
    for extension in extensions:
        extension = extension.lower()
        try:
            bot.load_extension(f'cogs.{extension}')
            await ctx.send(f'`Cog {extension} successfully loaded`')
        except discord.ext.commands.errors.ExtensionNotFound:
            await ctx.send(f'`Cog {extension} not found`')

# shorthand to load and unload
@bot.command()
async def reload(ctx, *extensions):
    await unload(ctx, *extensions)
    await load(ctx, *extensions)


# commands for disabling and enabling cogs
@bot.command()
async def disableCog(ctx, *extensions):
    # cycle through all extensions passed
    for extension in extensions:
        extension = extension.lower()
        # check that the module isn't loaded
        await unload(ctx, extension)

        # disable the file
        if(os.path.isfile(f'./cogs/{extension}.py')):
            os.rename(f'./cogs/{extension}.py',f'./cogs/{extension}.py.disabled')
            await ctx.send(f'`Cog {extension} successfully disabled`')
        else:
            await ctx.send(f'`Cog {extension} was not found.`')

'''
- note: doesn't load the module after reenabling it right now
'''
@bot.command()
async def enableCog(ctx, *extensions):
    # cycle through all extensions passed
    for extension in extensions:
        extension = extension.lower()
        # reenable the file
        if(os.path.isfile(f'./cogs/{extension}.py.disabled')):
            os.rename(f'./cogs/{extension}.py.disabled',f'./cogs/{extension}.py')
            await ctx.send(f'`Cog {extension} successfully enabled`')
        else:
            pass


# tester ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f'`Pong! {round(bot.latency * 1000)} ms`')


# end of core function defs


# loads all the extensions initally
for filename in os.listdir('./cogs'):
    if( filename.endswith('.py')):
        bot.load_extension(f'cogs.{filename[:-3]}')

# finally runs the bot
try:
    bot.run(config["token"])
except discord.errors.HTTPException:
    print("Invalid Token Present in Config.")
