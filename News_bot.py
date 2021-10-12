import discord
import json
import requests


client = discord.Client()

with open('Keys.txt') as f:
    lines = f.readlines()

token = lines[0]
api_id = lines[1]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:  # to ignore the msg sent by the bot itself.
        return

    if message.content.startswith('!getnews'):
        await message.channel.send("I'm fetching the latest news for you just hang on! :)")

        for i in range(5):
            await message.channel.send(get_news(i))


def get_news(i):
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey={}'.format(api_id)
    response = requests.get(url)

    json_data = json.loads(response.text)
    value = str(i + 1) + ('\n' + (json_data["articles"][i]["title"]) + '\nSource : ' + (
        json_data["articles"][i]["source"]["name"]) + '\nRead at : ' + (
                              json_data["articles"][i]["url"]) + '\nPublished At : ' + (
                          json_data["articles"][i]["publishedAt"]))
    return value


client.run(token)