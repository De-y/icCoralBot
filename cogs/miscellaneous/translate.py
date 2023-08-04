#cogs / funCommands / translate.py

from libraries.translate_text import translate
from discord.ext import commands

class translateText(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def translate(self, ctx, text: str, language: str):
        """
        Translate text with the power of Google Translate.
        """

        try:
            await ctx.send(translate(text, language))
        except:
            await ctx.send('Invalid language or the bot encountered an error whilst trying to translate.')

async def setup(client):
    await client.add_cog(translateText(client))