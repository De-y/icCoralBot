#cogs / hello.py
from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def hello(self, ctx):
        """
        Say hello to Paradigm!
        """

        await ctx.reply(f"Hello {ctx.author.mention}!", ephemeral=True)

async def setup(client):
    await client.add_cog(Hello(client))