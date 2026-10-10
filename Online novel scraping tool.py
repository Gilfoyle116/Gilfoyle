import requests
from lxml import etree
from urllib.parse import urljoin


url = "https://www.qute.cc"


def get_content(url, headers):
    data = requests.get(url, headers=headers)
    data.encoding = data.apparent_encoding or data.encoding
    all_content = etree.HTML(data.text)

    all_content_text = all_content.xpath("//*[@class='listmain']/dl/dd/a/text()")
    all_content_link = all_content.xpath("//*[@class='listmain']/dl/dd/a/@href")

    for chapter, link in zip(all_content_text, all_content_link):
        chapter = chapter.strip()
        chapter_url = urljoin(url, link)

        if chapter_url.startswith("javascript"):
            continue

        print(chapter)
        print(chapter_url)


        figure = requests.get(chapter_url, headers=headers)
        figure.encoding = figure.apparent_encoding or figure.encoding
        all_novel_content = etree.HTML(figure.text)

        all_novel_content_text = all_novel_content.xpath("//*[@id='title']/div/id/text()")
        content = '\n'.join(c.strip() for c in all_novel_content_text if c and c.strip())
        print(content)



def get_name(url, headers):
    data = requests.get(url, headers=headers)
    data.encoding = data.apparent_encoding or data.encoding
    all_name = etree.HTML(data.text)

    all_name_text = all_name.xpath("//*[@class='item']/dl/dt/a/text()")
    all_name_text = [name.strip() for name in all_name_text if name and name.strip()]

    if not all_name_text:
        all_name_text = all_name.xpath(
            "//[@class='item']//a[contains(@href, '/shu/')]/text()"
        )
        all_name_text = [name.strip() for name in all_name_text if name and name.strip()]

    for i, name in enumerate(all_name_text):
        print(i + 1, name)

    all_name_dict = {}
    all_name_link = all_name.xpath("//*[@class='item']/dl/dt/a/@href")
    for name, link in zip(all_name_text, all_name_link):
        all_name_dict[name] = link
    name = input("Please enter the novel which you want to load: ").strip()
    name_link = all_name_dict[name]
    name_url = urljoin(url, name_link)
    print(name_url)
    get_content(name_url, headers)



def get_type(url, headers):
    data = requests.get(url, headers=headers)
    data.encoding = data.apparent_encoding or data.encoding
    all_type = etree.HTML(data.text)

    all_type_text = all_type.xpath("//*[@class='nav']/ul/li/a/text()")[1:8]
    all_type_link = all_type.xpath("//*[@class='nav']/ul/li/a/@href")[1:8]

    all_type_dict = {}
    for type, link in zip(all_type_text, all_type_link):
        type = type.strip()
        link = urljoin(url, link)
        all_type_dict[type] = link
        print(type, link)
    type_name = input("Please enter the type you want to load: ")
    if type_name not in all_type_dict:
        print("Please choose the type from the dict")
        return

    type_url = all_type_dict[type_name]
    print(type_url)
    get_name(type_url, headers)



if __name__ == "__main__":
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/154.0.0.0 Safari/537.36"
    }

    get_type(url, headers)