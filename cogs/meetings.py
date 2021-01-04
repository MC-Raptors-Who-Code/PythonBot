import discord
import json
from os import path
from discord.ext import commands

class Meetings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        if(path.isfile("./cogData/meetings.json")):
            with open("./cogData/meetings.json", "r") as file:
            self.meetings = json.load(file)
        else:
            self.meetings = dict()

    def __del__(self):
        with open("./cogData/meetings.json", "w") as file:
            json.dump(self.meetings, file)

''' human readable output file
        with open("./cogData/meetings.json", "w") as file:
            json.dumps(self.meetings, indent = 4)
'''

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def addMeeting(self, ctx, day, time):
        pass



def setup(bot):
    bot.add_cog(Meetings(bot))
