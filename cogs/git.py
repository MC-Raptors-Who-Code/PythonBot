import discord
import os
from discord.ext import commands

class Git_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def sync(self, ctx):  
        pass

def setup(bot):   
    bot.add_cog(Git_Commands(bot))
