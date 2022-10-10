import requests
from bs4 import BeautifulSoup

book_data = soup.find_all("div", class_="product need-watch watched")

def get_data():
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                  "user-agent": "Mozilla/5.0 (X11; Linuxx86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

    }
    url = "https://www.labirint.ru/genres/2308/"

    response = requests.get(url = url, headers = headers)
    soup = BeautifulSoup(response.text, "lxml")

    pages_count = int(soup.find("div", class_="pagination.numbers").find_all("a")[-1].text)
    for page in range (1, pages_count + 1):
        url = f"https://www.labirint.ru/genres/2308/&page={page}"


        response = requests.get( url = url, headers = headers)
        soup = BeautifulSoup(response.text, "lxml")

        books_items =soup.find("tbody", class_= "products-table__body").find_all("tr")

    book_data = soup.find_all("div", class_="product need-watch watched")

    for bi in book_data :
        book_data =bi.find_all("td")

        try:
            book_data[0].find("a").text.strip()

        except:
            book_title = "Нет названия книги"
            print(book_title)
    sale = soup.find_all('span', class_='card-label__text card-label__text_turned')

    for i in sale:
        sale =i.find_all("td")

        try:
           sale[0].find("a").text.strip()

        except:
            sale = ""
            print(book_title)

for i in book_data:
    name = i.find()

def main():
     get_data()

if __name__ == "__main__" :
    main()

