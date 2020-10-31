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
       	result = subprocess.check_output("git pull --no-commit https://github.com/MC-Raptors-Who-Code/PythonBot.git")
        await ctx.send(f'```{result.decode("utf-8")}```')

def setup(bot):   
    bot.add_cog(Git_Commands(bot))
