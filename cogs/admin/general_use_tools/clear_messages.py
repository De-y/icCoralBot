#cogs / admin / clear_user.py
from discord.ext import commands
import discord, typing, time

class clearMessages(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def clear(self, ctx, number: int, member: typing.Optional[discord.Member]):
        """
        Clear Discord messages.
        """

        if member is not None:
            await ctx.send("Deleted messages!", ephemeral=True)        
            await ctx.channel.purge(limit=number, check=lambda message: message.author == ctx.author)
        else:
            await ctx.send("Deleted messages!", ephemeral=True)
            await ctx.channel.purge(limit=number)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You don't have permission to purge members' messages.", ephemeral=True)

    @clear.error
    async def bot_clear_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("❌ I don't have permission to purge members' messages.", ephemeral=True)

async def setup(client):
    await client.add_cog(clearMessages(client))