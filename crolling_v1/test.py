from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%A4%91%EA%B5%AD%EC%96%B4+%EC%9D%B4%EB%AF%B8%EC%A7%80')
soup = BeautifulSoup(response, 'html.parser')
for anchor in soup.select('a'):
    print(anchor)