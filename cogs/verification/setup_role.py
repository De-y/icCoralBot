#cogs / setup_role.py
from discord.ext import commands
import discord
from prisma.models import Servers

    
class Setup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def setup(self, ctx, role: discord.Role):
        """
        Setup verification for school-based discord servers(ADMIN ONLY)
        """
        
        Servers.prisma().create(data={'guild_id': ctx.guild.id, 'role_id': role.id})
        await ctx.send(f"Setup complete! Verification role is now <@&{role.id}>")
    @setup.error
    async def setup_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You don't have permission to MANAGE_ROLES.", ephemeral=True)
    
    @setup.error
    async def setup_bot_permerror(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("❌ I don't have the permission to MANAGE_ROLES. Please put my role up on the hierarchial level above the designated role you are trying to add for verification of your members.", ephemeral=True)

async def setup(client):
    await client.add_cog(Setup(client))