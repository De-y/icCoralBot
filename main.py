"""
Main.py

The place where it all begins.
"""

import os, discord, json
from dotenv import load_dotenv
from discord.ext import commands
import aiohttp, json, prisma


db = prisma.Prisma()
db.connect()
prisma.register(db)

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


def get_env(env_var):
    load_dotenv()
    e = os.getenv(env_var)
    return e


class Client(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = commands.when_mentioned_or("&"),
            intents = discord.Intents.all(),
            help_command = None,
        )

    async def setup_hook(self) -> None:
        # ...        
        cogs_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "cogs"))
        for root, dirs, files in os.walk(cogs_folder):
            for file in files:
                if file.endswith(".py"):
                    cog_path = os.path.join(root, file)
                    cog_name = cog_path[len(cogs_folder) + 1: -3].replace(os.path.sep, ".")
                    await client.load_extension(f"cogs.{cog_name}")
        await client.tree.sync()
        print("Loaded cogs")

        @client.event
        async def on_ready():
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="this Discord server."))
            print(f"Bot is in about {len(client.guilds)} servers.")

        @client.event
        async def on_command_error(ctx, error):
            if isinstance(error, commands.CommandOnCooldown):
                await ctx.send(f'The command that you ran is on cooldown, you can use it in {round(error.retry_after, 2)} seconds.', ephemeral=True)
        @client.event
        async def on_member_join(ctx):
                a = get_env("PRIVATE_KEY")
                authorization = a
                username = '@' + ctx.name
                result = await verify(username, authorization)
                if result == 'True':
                    await ctx.add_roles(ctx.guild.get_role(1088598080133271592))
                    await ctx.send('You have already been verified as a student of the school because you have verified yourself in the past in a school-affiliated server. You may now join the server!')
                else:
                    await ctx.send(f'Welcome to a Coral Academy-related discord, {ctx.mention}! Please visit <https://capi.avnce.tech/> to verify yourself as a student of the school. Once you have done that, you may run the command /verify in the server to verify yourself.')

client = Client()
client.run(get_env("TOKEN"))