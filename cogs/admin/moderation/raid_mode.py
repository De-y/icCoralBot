#cogs / admin/ raid_mode.py
from discord.ext import commands
import discord

class raidMode(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def raidmode(self, ctx):
        """
        Activate raid mode for damage control. Run /disableraidmode to deactivate raid mode.
        """

        # guild_id = ctx.guild.id
        # validator = await raidMode.prisma().find_first(where={'guildID': guild_id})
        # print('TEST')
        # if validator is None:
            # print('E')
        await ctx.send('Raid mode is enabled. Run /disableraidmode to disable raid mode.', ephemeral=True)

        # raidMode.prisma().create(data={'guildID': guild_id})
        channels = ctx.guild.channels
        everyone_role = ctx.guild.roles[0] # strictly get the @everyone role (lowest in hierarchy), in case an owner has a role named @everyone

        
        for channel in channels:
            if isinstance(channel, discord.TextChannel): # don't change permissions for voice chat or categories
                await channel.set_permissions(everyone_role, send_messages=False)

        # else:
        #     raidMode.prisma().delete(where={'guildID': guild_id})
        #     ctx.send('Raid mode disabled. Run this command again to enable raid mode.', ephemeral=True)
        #     channels = ctx.guild.channels
        #     everyone_role = ctx.guild.roles[0] # strictly get the @everyone role (lowest in hierarchy), in case an owner has a role named @everyone

            
        #     for channel in channels:
        #         if isinstance(channel, discord.TextChannel): # don't change permissions for voice chat or categories
        #             await channel.set_permissions(everyone_role, send_messages=True)


    @raidmode.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You don't have permission to run this command.", ephemeral=True)
    
    @raidmode.error
    async def ban_bot_permerror(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("❌ I don't have the permission to manage_channels.", ephemeral=True)

async def setup(client):
    await client.add_cog(raidMode(client))