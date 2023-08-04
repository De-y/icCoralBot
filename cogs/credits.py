#cogs / credits.py
from discord.ext import commands
import discord

class Credits(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def credits(self, ctx):
        """
        Show Credits.
        """
        embed = discord.Embed(title="**:coin: Credits**", description="©2023 Defy. All rights reserved.\n\nDiscord.py for the bot framework.", color=0xF54245)

        message = await ctx.send(embed=embed, ephemeral=True)

async def setup(client):
    await client.add_cog(Credits(client))