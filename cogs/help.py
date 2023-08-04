#cogs / help.py
from discord.ext import commands
import discord
from discord import app_commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    # @app_commands.choices(choices=[
    #     app_commands.Choice(name="Rock", value="rock"),
    #     app_commands.Choice(name="Paper", value="paper"),
    #     app_commands.Choice(name="Scissors", value="scissors"),
    # ])
    # choices: app_commands.Choice[str]
    async def help(self, ctx):
        """
        Get help on things related to the Paradigm Ecosystem.
        """
        # if (choices.value == 'rock'):
        #     counter = 'paper'
        # elif (choices.value == 'paper'):
        #     counter = 'scissors'
        # else:
        #     counter = 'rock'
        # await ctx.send(f'{ctx.author.mention} {counter}!')
        embed = discord.Embed(title="**Paradigm Help**", description="Test", color=0xF54245)

        message = await ctx.send(embed=embed, ephemeral=True)

async def setup(client):
    await client.add_cog(Help(client))