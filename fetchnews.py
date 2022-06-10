import json
import requests

from Summarizer import ret_summary

def get_news(i):
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey= YOUR_API_KEY'
    response = requests.get(url)

    json_data = json.loads(response.text)
    value = str(i+1) + ('\n' + (json_data["articles"][i]["title"]) + '\nSource : ' + (
        json_data["articles"][i]["source"]["name"]) + '\nRead at : ' + (
                 json_data["articles"][i]["url"]) + '\nPublished At : ' + (
                 json_data["articles"][i]["publishedAt"]))

    URL = json_data["articles"][i]["url"]

    source = json_data["articles"][i]["source"]["name"]

    a = 19
    if i >= a:
        return "THANK U " + ("\U0001F600")

    elif source == "YouTube" or source == "Google News" or source == "Investing.com":
        return str(i + 1) + " Hold On " + ("\U0001F642")

    else:
        summary = ret_summary(URL)
        to_return = value + ('\n' + "Here is the summary of this article: " + ("\U0001F601") + '\n' + summary + '\n' + '\n')

        c = 2000
        if(len(to_return) >= c):
            return str(i + 1) + " Hold On " + ("\U0001F642")

        return to_return