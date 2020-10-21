import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Javascript-Engineer&where=Massachusetts'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
# print(results.prettify())

job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    print(job_elem, end='\n'*2)
