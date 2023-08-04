#cogs / admin / eval.py
from discord.ext import commands
import discord, typing, time, contextlib, io, psutil

class stats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.guild_only()
    @commands.is_owner()
    async def stats(self, ctx):
        """
            Get Server statistics.
        """
        embed=discord.Embed(title=f"Server statistics for {ctx.guild.name}", color=0x3f51b5)
        embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.add_field(name="Users:", value=ctx.guild.member_count, inline=False)
        embed.add_field(name="Channels:", value=len(ctx.guild.channels), inline=False)
        embed.set_footer(text='Requested by ' + ctx.message.author.name, icon_url=ctx.message.author.avatar)

        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(stats(client))