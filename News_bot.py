import discord

from fetchnews import get_news
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:  # to ignore the msg sent by the bot itself.
        return

    if message.content.startswith('!summary'):
        await message.channel.send("I'm fetching the latest news articles and summarizing them for you just hang on! " + ("\U0001F600"))

        for i in range(20):
            await message.channel.send(get_news(i))


client.run('OTg0MzQyMzAyMjIwNzc5NTYw.GX1TtB.VKBJ8C8KdwydXFdw-dKP0iO9v2hlNHr2m4N4Es')
