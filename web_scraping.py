# web scraping
#accupuncture professionals in USA

import requests
from bs4 import BeautifulSoup

url = 'https://directory.nccaom.org/FAP/SearchResultWithoutMap?Radius=0&CountryCode=USA&StateCode=FL&SearchType=2&Latitude=0&Longitude=0&SortBy=DisplayName&SortDirection=DESC&SearchFormType=FAP&PageNo=1'

res = requests.get(url)
details = res.content
print(details)