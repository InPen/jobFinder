import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Javascript-Engineer&where=Massachusetts'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
