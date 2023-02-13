from tqdm import tqdm	#for문의 진행도를 보여준다
from bs4 import BeautifulSoup as BS
from urllib.request import Request, urlopen
import pandas as pd
import time

name = []
club = []
nation = []
league =[]
rating = []
position = []
subposi = []
version = []
price = []

header = {'User-Agent': 'Mozilla/5.0'}

for x in tqdm(range(1,72)):
    site = f'https://www.futbin.com/players?page={x}'
    url = Request(site, headers=header)
    html = urlopen(url)
    soup = BS(html, 'html.parser')
    playertr = soup.find('tbody').findAll('tr', class_ = ['player_tr_1', 'player_tr_2'])
    time.sleep(3)
    
    for y in range(0,len(playertr)):
        td = playertr[y].findAll('td')
        if int(td[2].text) < 80:	#선수 OVR이 80미만이면 종료
            print('79 over done')
            break
        name.append(td[1].text.strip())
        rating.append(td[2].text)
        position.append(td[3].findAll('div')[0].text)
        subposi.append(td[3].findAll('div')[1].text)
        version.append(td[4].findAll('div')[0].text)
        price.append(td[5].findAll('span')[0].text.strip())
        club.append(td[1].findAll('a')[1]['data-original-title'])
        nation.append(td[1].findAll('a')[2]['data-original-title'])
        league.append(td[1].findAll('a')[3]['data-original-title'])
        
data = pd.DataFrame(
    {"name" : name,
     "club" : club,
     "nation" : nation,
     "league" : league,
     "rating" : rating,
     "position" : position,
     "subposi" : subposi,
     "version" : version,
     "price" : price})

data.to_csv('futbin23over79.csv', index=False, encoding='utf-8-sig')	#엑셀 파일로 저장