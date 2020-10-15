import discord 
from discord.ext import commands

class Test_Cog(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		pass

	@commands.command()
	async def test(self, ctx):
		await ctx.send("Hi\nhello\nhey")


def setup(bot):
	bot.add_cog(Test_Cog(bot))
