'''
web scrapng often involces making numerous network request to fetch web 
pages. These tasks are I/O bound because they spend a lot of time waiting 
from responses from servers. Multi threading can significantly improve 
the prformance by allowing multiple web pages to be fetched concurrently

https://python.langchain.com/v0.2/docs/introduction/
https://python.langchain.com/v0.2/docs/concepts
https://python.langchain.com/v0.2/docs/tutorials/
'''

import threading
import requests
from bs4 import BeautifulSoup # bs4 library is used for web scrapping

urls=[
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://python.langchain.com/v0.2/docs/concepts',
    'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_cotent(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser') # scraping the content present inside html
    print(f"Fetched {len(soup.text)} characters from {url}")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_cotent, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All webpages fetched")