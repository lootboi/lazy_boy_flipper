from dotenv         import load_dotenv
from discord.ext    import commands, tasks

import os
import discord
import datetime

load_dotenv()

token = os.getenv('DISCORD_KEY')
channel_id = os.getenv('CHANNEL_ID')

time = datetime.datetime.now

def discord_alert(item_collection, item_price, item_rarity, item_img, item_collection_id, item_pfp):
    class MyClient(commands.Bot):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.msg_sent = False

        async def on_ready(self):
            channel = bot.get_channel(int(channel_id))
            await self.display_embed(channel)

        async def display_embed(self, channel):
            embed = discord.Embed(
                title = item_collection + ' #' + item_collection_id,
                description = item_collection + ' ' + item_collection_id + ' matches your parameters!' ,
                colour = None
            )
        
            embed.set_footer(text='@AltLoot')
            embed.set_image(url=item_img)
            embed.set_thumbnail(url=item_pfp)
            embed.add_field(name='Rank:', value=str(item_rarity), inline=True)
            embed.add_field(name='Price:', value=str(item_price) + ' AVAX', inline=True)

            await channel.send(embed=embed)
            await bot.close()

    bot = MyClient(command_prefix='!', intents=discord.Intents().all())
    bot.run(token)
