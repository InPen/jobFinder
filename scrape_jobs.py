import requests

URL = 'https://www.monster.com/jobs/search/?q=Javascript-Engineer&where=Massachusetts'
page = requests.get(URL)
