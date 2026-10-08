import requests
from lxml import etree
import time

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"
}
url = "https://movie.douban.com/top250"

data = requests.get(url, headers=headers)

html = etree.HTML(data.text)
# find the absolute path
alt = html.xpath("//*[@class='pic']/a/img/@alt")
src = html.xpath("//*[@class='pic']/a/img/@src")

# initial the path
path = 'img'
# looping two lists at the same time
for a, s in zip(alt, src):
    print(a, s)
    file_name = a + '.jpg'
    img = requests.get(s, headers=headers).content

    time.sleep(1)

    with open(path + '/' + file_name, 'wb') as f:
        f.write(img)
