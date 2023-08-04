#cogs / funCommands / avatar.py

from discord.ext import commands
import typing, discord

class getAvatar(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def avatar(self, ctx, user: typing.Optional[discord.Member]):
        """
        Get a users avatar.
        """
        if user is None:
            avatar_embed = discord.Embed(title=ctx.message.author.name + "'s avatar", color=0x3f51b5)
            avatar_embed.set_image(url=ctx.message.author.avatar)
            avatar_embed.set_footer(text='Requested by ' + ctx.message.author.name, icon_url=ctx.message.author.avatar)
            await ctx.send(embed = avatar_embed)

        else:
            avatar_embed = discord.Embed(title=user.name + "'s avatar", color=0x3f51b5)
            avatar_embed.set_image(url=user.avatar)
            avatar_embed.set_footer(text='Requested by ' + ctx.message.author.name, icon_url=ctx.message.author.avatar)
            await ctx.send(embed = avatar_embed)

async def setup(client):
    await client.add_cog(getAvatar(client))