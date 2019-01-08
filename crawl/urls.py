import urllib.parse as parse
import os.path as path

def getFilename(url):
    return path.basename(parse.urlparse(url).path)

def getHostname(url, withProtocol = False):
    p = parse.urlparse(url)
    if withProtocol:
        return "{}://{}".format(p.scheme, p.hostname)
    else:
        return p.hostname

if __name__ == '__main__':
    URL = "https://postfiles.pstatic.net/MjAxOTAxMDNfMjYw/MDAxNTQ2NTA4NzYwNjQ3.fVyIE3nPM6zmvVZuaJG9tSAqzopYNzUGUpPHR9v86hMg.Hyq_lVTVWz-pnaSC3TZ8ue4iJOfJMgkOFVSQozQdYqUg.PNG.korea_diary/천안_호두과자.png?type=w966"
    print("URL>>", URL)
    print("fileName>>", getFilename(URL))
    print("hostName>>", getHostname(URL))
    print("hostName>>", getHostname(URL, True))
