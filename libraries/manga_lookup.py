import aiohttp
import discord
import random, asyncio




async def searchmanga(manga):
    try:
        base_lookup = 'https://kitsu.io/api/edge/manga?filter[text]=' + manga

        async with aiohttp.ClientSession() as cs:
            async with cs.get(base_lookup) as r:
                res = await r.json()
                var=res['data'][0]
                
                # Attributes about the manga
                description = var['attributes']['description']
                chapterCount = var['attributes']['chapterCount']
                volumeCount = var['attributes']['volumeCount']
                link = var['links']['self']
                new_link = str(link).strip('/api/edge')
                poster_image = var['attributes']['posterImage']['small']
                rank = str(var['attributes']['ratingRank'])
                title = var['attributes']['canonicalTitle']
                status = var['attributes']['status']
                subtype = var['attributes']['subtype']
                average_rating = var['attributes']['averageRating']
                nrank = 'N/A'
                naverage_rating = 'N/A'

                
                if average_rating is not None:
                    naverage_rating = average_rating
                if average_rating is not None:
                    average_rating = average_rating + "/100"
                if rank is not None:
                    nrank = rank

                if status == "current":
                    date_airing = var['attributes']['startDate'] + ' - ' + 'Now'
                    chapterCount = '???'
                    volumeCount = '???'
                else:
                    date_airing = var['attributes']['startDate'] + ' - ' + var['attributes']['endDate']

                new_link = str(link).split('/api/edge')
                new_link = new_link[0] + new_link[1]
                #url=new_link,
                pyanime = discord.Embed(title="**" + title + "**", description = description + '\n\n' + '⏳ Status:\n' + status + '\n\n🗂 Type:\n**' + subtype + '**\n\n' + '🗓 Running: \n**' + date_airing + '**\n\n⭐ Average Rating: \n**' + naverage_rating + '**\n\n' + '📰 Chapters:\n**' + str(chapterCount) + '**\n\n' + '📚 Volumes:\n**' + str(volumeCount) + ' volumes**\n\n🏆 Rank:\n** TOP ' + str(nrank) + '**', color=0x3f51b5)
                pyanime.set_thumbnail(url=poster_image)
                return pyanime
            await searchmanga(manga)
    except Exception as err:
        pymangaf = discord.Embed(title='**Manga could not be found.**', color=0x3f51b5)
        return pymangaf

# print(asyncio.run(searchanime('Sazae-San')))
# exit(1)