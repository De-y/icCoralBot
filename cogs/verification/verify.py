#cogs / verify.py
from discord.ext import commands
import aiohttp, json
from prisma.models import Servers

async def verify(username, authorization):
    async with aiohttp.ClientSession() as session:
        data = {
            'username': username,
            'authorization': authorization
        }
        data = json.dumps(data)
        url = 'https://capi.avnce.tech/api/getinfo'
        headers = {'Content-Type': 'application/json'}
        response = await session.post(url, data=data, headers=headers)
        result = await response.text()
        return result
    
class Verify(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def verify(self, ctx):
        """
        Verify you are a student of the school.
        """
        username = '@' + ctx.author.name
        authorization = 'PRIVATE_KEY_HERE!!!'
        result = await verify(username, authorization)
        if result == 'True':
            role_id = Servers.prisma().find_first(where = {'guild_id': ctx.guild.id})
            await ctx.reply('You have been verified as a student of the school(or may have already been verified, in which case will make the command not work). However, you may now join the server.', ephemeral=True)
            await ctx.author.add_roles(ctx.guild.get_role(int(role_id.role_id)))
        else:
            await ctx.reply('You have not been verified as a student of the school. Please try again using the link that I sent you in the DM\'s.', ephemeral=True)

async def setup(client):
    await client.add_cog(Verify(client))