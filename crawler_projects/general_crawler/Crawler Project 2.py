import requests
from lxml import etree

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"
}

url = "https://movie.douban.com/top250?"

# initial path
path = 'img'
def get_pic(url):
    rep = requests.get(url, headers=headers).text
    html = etree.HTML(rep)

    # finding the absolute path
    alt = hteml.xpath(//*[@class='pic']/a/img/@alt)
    src = hteml.xpath(//*[@class='pic']/a/img/@src)

    # running the two lists at the same time
    for a, s in zip(alt, src):
        print(a, s)
        file_name = a + '.jpg'
        img = requests.get(s, headers=headers).content
        
        with open(path + '/' + file_name, 'wb') as f:
            f.write(img)

if __name__ == "__main__":
    url_list = ["https://movie.douban.com/top250?start={}&filter=".format(x * 25) for x in range(10)]
    for url in url_list:
        get_pic(url)
