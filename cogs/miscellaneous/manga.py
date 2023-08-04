#cogs / funCommands / memes.py

from discord.ext import commands
from libraries.manga_lookup import searchmanga

class searchManga(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def manga(self, ctx, manga: str):
        """
        Search for a manga.
        """

        await ctx.send(embed= await searchmanga(manga))

async def setup(client):
    await client.add_cog(searchManga(client))