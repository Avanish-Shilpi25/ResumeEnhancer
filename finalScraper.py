import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}


def get_url(position, location):
    template = 'https://www.indeed.co.in/jobs?q={}&l={}'
    url = template.format(position, location)
    response = requests.get(url, headers=headers)
    html = response.text

    

    return url
    
url = get_url('Teacher Assitant', 'Cypress TX')

response = requests.get(url)
print(response)

soup = BeautifulSoup(response.text, 'html.parser')
cards = soup.find_all('h2', 'screen-reader-only')
print(len(cards))

