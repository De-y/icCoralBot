import aiohttp
import discord
import random, asyncio




async def searchanime(anime):
    try:
        base_lookup = 'https://kitsu.io/api/edge/anime?filter[text]=' + anime

        async with aiohttp.ClientSession() as cs:
            async with cs.get(base_lookup) as r:
                res = await r.json()
                var=res['data'][0]
                
                # Attributes about the anime
                description = var['attributes']['description']
                link = var['links']['self']
                poster_image = var['attributes']['posterImage']['small']
                rank = str(var['attributes']['ratingRank'])
                title = var['attributes']['canonicalTitle']
                status = var['attributes']['status']
                subtype = var['attributes']['subtype']


                if status == "current":
                    date_airing = var['attributes']['startDate'] + ' - ' + 'Now'
                    episodeCount = '???'
                else:
                    date_airing = var['attributes']['startDate'] + ' - ' + var['attributes']['endDate']
                    episodeCount = var['attributes']['episodeCount']


                average_rating = var['attributes']['averageRating'] + "/100"
                new_link = str(link).split('/api/edge')
                new_link = new_link[0] + new_link[1]
                #url=new_link, 
                pyanime = discord.Embed(title="**" + title + "**", description = description + '\n\n' + '⏳ Status:\n' + status + '\n\n🗂 Type:\n**' + subtype + '**\n\n' + '🗓 Aired: \n**' + date_airing + '**\n\n⭐ Average Rating: \n**' + average_rating + '**\n\n' + '💽 Total Episodes:\n**' + str(episodeCount) + ' episodes**\n\n🏆 Rank:\n** TOP ' + str(rank) + '**', color=0x3f51b5)
                pyanime.set_thumbnail(url=poster_image)
                return pyanime
            await searchanime(anime)
    except Exception as err:
        pyanimenf = discord.Embed(title='**Anime could not be found.**', color=0x3f51b5)
        return pyanimenf

# print(asyncio.run(searchanime('Sazae-San')))
# exit(1)