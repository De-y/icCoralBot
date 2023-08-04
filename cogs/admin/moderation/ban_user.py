#cogs / admin/ ban.py
from discord.ext import commands
import discord, typing

class banUser(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def ban(self, ctx, member: discord.Member, reason: typing.Optional[str]):
        """
        Ban certain members from your server.
        """

        if reason is None:
            await member.ban()
            await ctx.reply(f"{member} has been successfully banned from the server.", ephemeral=True)
            em = discord.Embed(color=discord.Color.from_rgb(0,0,255),title=f"**{member} has been banned from the server**.",description=f"{member} has been banned from the server.")
            await ctx.send(embed=em)
        
        else:
            await member.ban(reason = reason)
            await ctx.reply(f"{member} has been successfully banned from the server.", ephemeral=True)
            em = discord.Embed(color=discord.Color.from_rgb(0,0,255),title=f"**{member} has been banned from the server**.",description=f"{member} has been banned from the server for {reason}.")
            await ctx.send(embed=em)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You don't have permission to ban members.", ephemeral=True)
    
    @ban.error
    async def ban_bot_permerror(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("❌ I don't have the permission to ban members.", ephemeral=True)

async def setup(client):
    await client.add_cog(banUser(client))