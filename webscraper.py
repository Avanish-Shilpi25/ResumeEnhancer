import urllib.request import urlopen
from bs4 import BeautifulSoup

 
url = 'https://www.indeed.com/jobs?q=teacher%20assistant&l=Cypress%2C%20TX&from=searchOnHP&vjk=01b6740156fbdcd1'
 
request_page = urlopen(url_to_scrape)
page_html =  request_page.read()
request_page.close()

html_soap = BeautifulSoup(page_html, 'html.parser')

job_description = html_soup.find_all('div', class_="jobsearch-jobDescriptionText" ')

for cactu


response = requests.get(url)
text = response.text
data = BeautifulSoup(text, 'html.parser')
 
# since, headings are the first row of the table
headings = data.find_all('tr')[0]
headings_list = [] # list to store all headings
 
for x in headings:
    headings_list.append(x.text)
# since, we require only the first ten columns
headings_list = headings_list[:10]
 
print('Headings are: ')
for column in headings_list:
    print(column)
 
 
