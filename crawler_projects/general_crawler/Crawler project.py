import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"
}
url = "https://movie.douban.com/top250"

data = requests.get(url, headers=headers)
# html.parser resolver
soup = BeautifulSoup(data.text, "html.parser")

movies = soup.find_all("div", class_="info")
with open("movies.txt", "w", encoding='utf-8') as f:
    for movie in movies:
        title = movie.find("span", class_='title').text.strip()

        basic_information = movie.find("div", class_='bd').text.strip()

        quote_tag = movie.find("p", class_='quote')
        quote = quote_tag.text.strip() if quote_tag else 'No'

        rating = movie.find("span", class_='rating_num').text.strip()

        line = f"{'title':<20}\t{'rating':<8}\t{'quote':<22}\t{'basic_information'}\n"
        line += f"{title:<20}\t{rating:<8}\t{quote:<22}\t{basic_information}\n"
        line += "-" * 100 + "\n"
        f.write(line)
        print(line, end="")
