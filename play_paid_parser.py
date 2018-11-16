from bs4 import BeautifulSoup
import requests

url = "https://play.google.com/store/apps/category/GAME/collection/topselling_paid"
res = requests.get(url)
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
card_list = soup.select('div.card-list')
# print(card_list)

print(">>>>>>>>>", type(card_list), type(card_list[0]))
for i in card_list:
    cards = i.select('.card')
    print("LLL>>", len(cards))
    for c in cards:
        title = c.select('a.title')[0].text.strip()
        # comp = c.select('a.subtitle')[0].text
        comp = c.select('a.subtitle')[0].get('title')
        print(">>", c.get('class'), [title, comp])

