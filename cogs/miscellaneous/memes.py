#cogs / funCommands / memes.py

from discord.ext import commands
from libraries.dpymemes import pyrandmeme

class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def meme(self, ctx):
        """
        Get some random memes from reddit.
        """

        await ctx.send(embed=await pyrandmeme())

async def setup(client):
    await client.add_cog(Meme(client))