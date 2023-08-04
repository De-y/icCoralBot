#cogs / funCommands / memes.py

from discord.ext import commands
from libraries.anime_lookup import searchanime

class searchAnime(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def anime(self, ctx, anime: str):
        """
        Search for an anime.
        """

        await ctx.send(embed= await searchanime(anime))

async def setup(client):
    await client.add_cog(searchAnime(client))