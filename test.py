import requests
import csv
import json
from bs4 import BeautifulSoup

 

response = requests.get("https://finance.naver.com/sise/")

 

soup = BeautifulSoup(response.text, 'lxml')

a = soup.select('.lst_pop > li')[0].text
b = soup.select('.lst_pop > li')[1].text
c = soup.select('.lst_pop > li')[2].text
d = soup.select('.lst_pop > li')[3].text
e = soup.select('.lst_pop > li')[4].text

l = []
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
    json.dump(l, f_write, ensure_ascii=False, indent=4)

data = ""
with open('data.js', "r", encoding="UTF-8-sig") as f:
    line = f.readline()
    while line:
        data += line
        line = f.readline()

final_data = f"var data = {data};"
final_data = f"var 1등 = '{a}';\n\
var 2등 = '{b}';\n\
var 3등 = '{c}';\n\
var 4등 = '{d}';\n\
var 5등 = '{e}';\n\
" + final_data
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
    f_write.write(final_data)
