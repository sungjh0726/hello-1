import urllib.parse as parse
import os.path as path

def getFilename(url):
    p = parse.urlparse(url).path
    return path.basename(p)

def getHostname(url, withProtocol=False):
    p = parse.urlparse(url)
    if withProtocol:
        return "{}://{}".format(p.scheme, p.hostname)
    else:
        return p.hostname

def urljoin(url, p):
    return parse.urljoin(url, p)

def q2j(s):
    ps = s.split('&')
    for p in ps:
        pp = p.split('=')
        print("'{}':'{}',".format(pp[0], pp[1]))

if __name__ == '__main__':
    str = "Email=shjeon77&Password=x8whq7Kjq5wPNpD&Action=1&ReturnUrl=&ReturnUrl_pop=&SecureLogin=false&snsUserId=0&snsType=0&snsAppId=1"
    q2j(str)


    # url = "https://blog.naver.com/jeonseongho/1212.jpg"
    # print("filename=", getFilename(url))
    # print("hostname=", getHostname(url))
    # print("URL=", getHostname(url, True))
    # print("QQ>>", urljoin("https://nave.com", "bbb.jpg?aaaa=1"))
