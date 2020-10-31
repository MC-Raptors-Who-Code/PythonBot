import discord
import subprocess
from discord.ext import commands

class Git_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def sync(self, ctx):  
    	#hardcode location of repo, make more modular going further
       	subprocess.call("git pull https://github.com/MC-Raptors-Who-Code/PythonBot.git", shell = True)

def setup(bot):   
    bot.add_cog(Git_Commands(bot))
