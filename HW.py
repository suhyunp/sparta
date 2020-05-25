import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')



music_numbers = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for music in music_numbers:
    n_tag = music.select_one('td.number')
    n = n_tag.text.split()
    rank = n[0]


    c_tag = music.select_one('td.info > a.title.ellipsis')
    c = c_tag.text.lstrip()
    
    artist_tag = music.select_one('td.info > a.artist.ellipsis')
    artist = artist_tag.text
    print(rank, c, artist)
