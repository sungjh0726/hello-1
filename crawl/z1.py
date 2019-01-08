from bs4 import BeautifulSoup
import requests

res = requests.get(
    "https://search.daum.net/search?w=tot&q=%EB%A7%B9%EC%9C%A0%EB%82%98&DA=ATG&rtmaxcoll=1TH")
soup = BeautifulSoup(res.text, 'html.parser')

sel = "#profMainThumb_img_0 > a > img"

imgs = soup.select(sel)
print(imgs, len(imgs))

if len(imgs) < 1:
    exit()

img = imgs[0]
src = img.get('src')
print("img>>", src)


# for link in links:
#     if "http" in link.get('src'):
#         lnk = link.get('src')
#         with open(basename(lnk), "wb") as f:
#             f.write(requests.get(lnk).content)
