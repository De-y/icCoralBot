#cogs / setup_role.py
from discord.ext import commands
import discord
from prisma.models import Servers

    
class SetupOwner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def override_setup(self, ctx, role: discord.Role):
        """
        Setup verification for school-based discord servers(BOT OWNER OVERRIDE ONLY!)
        """
        username = '@' + ctx.author.name
        if username != '@av.c':
            ctx.send("You are not allowed to run this as you are not the owner of the bot(av.c, although he doesn't have all the special perms.)", ephemeral=True)
        Servers.prisma().create(data={'guild_id': str(ctx.guild.id), 'role_id': str(role.id)})
        await ctx.send(f"Setup complete! Verification role is now <@&{role.id}>")
    
    @override_setup.error
    async def setup_bot_permerror(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("❌ I don't have the permission to MANAGE_ROLES. Please put my role up on the hierarchial level above the designated role you are trying to add for verification of your members.", ephemeral=True)

async def setup(client):
    await client.add_cog(SetupOwner(client))