# necessary import for cog
from discord.ext import commands


# how to inherit from the commands.Cog class
class Example_Cog(commands.Cog):

# constructor allows class to always access the bot object
    def __init__(self, bot):
        self.bot = bot

# decorator for an event
    @commands.Cog.listener()
    async def on_ready(self):
        pass

# decorator for an additional command
    @commands.command()
    async def test(self, ctx):
        await ctx.send("Hi\nhello\nhey")

# a slighly more complex command
    @commands.command()
    async def status(self, ctx):
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game("yo"))


# function that actually gets run when adding a cog
def setup(bot):
    bot.add_cog(Example_Cog(bot))
