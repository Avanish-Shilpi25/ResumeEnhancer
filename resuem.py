import requests
from bs4 import BeautifulSoup
import cloudscraper


skill =input('Enter your Skill: ').strip()
place =input('Enter your Location: ').strip()
url = 'https://www.indeed.com/viewjob?jk=575cd1f765ec90ae&q=' + skill + '&l=' + place
hdr = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
 
scraper = cloudscraper.create_scraper()

response = scraper.get(url, headers=hdr)

soup = BeautifulSoup(response.content, 'html.parser')


jobDescription = soup.find_all('div', 'jobsearch-jobDescriptionText')
for p in soup.find_all('p'):
    print (p.text)
