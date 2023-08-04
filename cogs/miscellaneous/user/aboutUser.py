#cogs / misc / about.py

from discord.ext import commands
import typing, discord

class getAbout(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def about(self, ctx, user: typing.Optional[discord.Member]):
        """
        Get information about an user.
        """
        if user is None:
            m = ctx.message.author
            creation_date = m.created_at
            creation_date = creation_date.strftime('%m/%d/%Y at %I:%M %p.')
            avatar_embed = discord.Embed(title="Information about: " + m.name, description = f'📅 Created on:\n {creation_date}\n\n📋 User ID:\n{m.id}\n\n👤Full Username: {m}', color=0x3f51b5)
            avatar_embed.set_thumbnail(url=m.avatar)
            avatar_embed.set_footer(text='Requested by ' + ctx.message.author.name, icon_url=ctx.message.author.avatar)
            await ctx.send(embed = avatar_embed)

        else:
            m = user
            creation_date = m.created_at
            creation_date = creation_date.strftime('%m/%d/%Y at %I:%M %p.')
            avatar_embed = discord.Embed(title="Information about: " + m.name, description = f'📅 Created on:\n {creation_date}\n\n📋 User ID:\n{m.id}\n\n👤Full Username: {m}', color=0x3f51b5)
            avatar_embed.set_thumbnail(url=m.avatar)
            avatar_embed.set_footer(text='Requested by ' + ctx.message.author.name, icon_url=ctx.message.author.avatar)
            await ctx.send(embed = avatar_embed)

async def setup(client):
    await client.add_cog(getAbout(client))