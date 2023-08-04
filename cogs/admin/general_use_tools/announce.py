#cogs / admin/ ban.py
from discord.ext import commands
import discord

class announce(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @commands.bot_has_permissions(send_messages=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def announce(self, ctx, title: str, description: str):
        """
        Announce something in your server!
        """

        embed = discord.Embed(title=title, description=description, color=0xF54245)
        await ctx.send(embed=embed)

    @announce.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You don't have permission to do this.", ephemeral=True)
    
    @announce.error
    async def ban_bot_permerror(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("❌ I don't have the permission to send embeds. Please rerun the command after adjusting my roles a little bit.", ephemeral=True)

async def setup(client):
    await client.add_cog(announce(client))