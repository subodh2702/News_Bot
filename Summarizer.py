import requests

from transformers import pipeline
from bs4 import BeautifulSoup


summarizer = pipeline("summarization", model="t5-base")

def ret_summary(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all(['h1','h2','h3','p'])
    text = [result.text for result in results]
    article = ' '.join(text)

    max_chunk = 400
    article = article.replace('.', '.<eos>')
    article = article.replace('?', '?<eos>')
    article = article.replace('!', '!<eos>')

    sentences = article.split('<eos>')
    current_chunk = 0
    chunks = []
    for sentence in sentences:
        if len(chunks) == current_chunk + 1:
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            print(current_chunk)
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])

    res = summarizer(chunks, max_length=150, min_length=20, do_sample=False)

    s = ""
    for r in res:
        s += r['summary_text']

    return s