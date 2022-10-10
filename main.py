import json
import requests
from bs4 import BeautifulSoup
def get_data():
    books = []

    url = 'https://www.labirint.ru/genres/2308/'
    headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                      "user-agent": "Mozilla/5.0 (X11; Linuxx86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

        }
    count_books = 0
    response = requests.get(url = url, headers = headers)
    soup = BeautifulSoup(response.text, 'lxml')

    pages_count = int(soup.find("div", class_="pagination.numbers").find_all("a")[-1].text)
    for page in range(1, pages_count + 1):
        url = f"https://www.labirint.ru/genres/2308/&page={page}"
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        books_items = soup.find("tbody", class_="products-table__body").find_all("tr")

        for i, item in enumerate (books_items ):
           try:
                book_title = item.find('span', class_='product-title').text.replace("\n", "")
           except:
                book_title = "-"
           try:
                 author = item.find('span', class_='product-author')
           except:
            author = "-"
           try:
            sale = item.find('span', class_='card-label__text card-label__text_turned')
           except:
            sale = "-"
           try:
            page = item.find('div', class_='pagination-number')
           except:
            page = "-"
        a = item.find("td", class_ = "").find("a")["href"]
        url = f"https://www.labirint.ru{a}"
        count_books += 1

        books.append(
              {
                  "book_title" : book_title,
                  "author": author,
                  "sale": sale,
                  "url": url,
              }
                 )