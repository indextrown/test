
import requests
from bs4 import BeautifulSoup
import csv
import json

response = requests.get("https://finance.naver.com/sise/")

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

oneStep = soup.select('.main')[2]
twoStep = oneStep.select('tbody > tr')[1:]



#################################
# 파일을 1개로 합친 이유 : 1번 크롤링 해서 모든 정보를 뽑아올 수 있기 때문
# 해당 서버의 부하를 줄이기 위해서 입니다.

a = soup.select('.lst_pop > li')[0].text
b = soup.select('.lst_pop > li')[1].text
c = soup.select('.lst_pop > li')[2].text
d = soup.select('.lst_pop > li')[3].text
e = soup.select('.lst_pop > li')[4].text
##################################




#파일을 한 번 쓴다.
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
    json.dump(l, f_write, ensure_ascii=False, indent=4)

#파일을 다시 읽는다.
data = ""
with open('data.js', "r", encoding="UTF-8-sig") as f:
    line = f.readline()
    while line:
        data += line
        line = f.readline()

#파일에 변수명을 추가하여 다시 쓴다.

final_data = f"var data = {data};"
final_data = f"var 1등 = '{a}';\n\
var 2등 = '{b}';\n\
var 3등 = '{c}';\n\
var 4등 = '{d}';\n\
var 5등 = '{e}';\n\
" + final_data
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
    f_write.write(final_data)
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
    f_write.write(final_data)
