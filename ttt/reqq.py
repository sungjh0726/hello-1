import requests
from bs4 import BeautifulSoup

class TC:
    pass

url = "https://play.google.com/store/apps/category/GAME/collection/topselling_paid"
res = requests.get(url)

# print(req.text)
# print(req.content)

soup = BeautifulSoup(res.text, 'html.parser')

card_list = soup.select('div.card-list')
print("-----------------------------------------")
for i in card_list:
    # print(i.get('class'))
    cards = i.select('.card')
    for c in cards:
        print(">>", c.get('class'))


print("status>>", res.status_code)
# print("QQQ>>", res.cookies['1P_JAR'])
