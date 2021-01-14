# necessary import for cog
import discord
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

# function that actually gets run when adding a cog
def setup(bot):
	bot.add_cog(Example_Cog(bot))
