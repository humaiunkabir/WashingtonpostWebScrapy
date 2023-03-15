import requests
from bs4 import BeautifulSoup

website_url = "http://books.toscrape.com/"

class WebsiteScrapper: 
    def __init__(self) -> None:
        self.book_topics = []
        self.books = []
        self._content = self._get_website_content(website_url)
        self._soup = BeautifulSoup(self._content, 'html.parser')
    
    def _get_website_content(self,url):
        response = requests.get(url)
        return response.content


    def get_books_topics(self):
        
        topic_ul = self._soup.find_all('ul', class_="nav-list")[0]
        topic_li = topic_ul.find_all('li')[0]
        topics_li = topic_li.find('ul').find_all('li')

        for topic in topics_li:
            topic_name = topic.find('a').text
            self.book_topics.append(topic_name.strip())

        return self.book_topics

    def get_books(self):
        
        section = self._soup.find('section')
        div = section.find_all("div")[1]
        ol = div.find("ol")
        all_li = ol.find_all("li")

        for li in all_li:
            article = li.find("article")
            src = article.find("div", class_="image_container").find("a").find("img").get("src")
            title = article.find("h3").find("a").get("title")
            product_price_div = article.find("div",class_="product_price")
            price = product_price_div.find("p",class_="price_color").text
            availability = product_price_div.find("p", class_="instock").text.strip()
            book_dict={
                "book_title": title,
                "image_url": f"http://books.toscrape.com/{src}",
                "book_price": price,
                "is_available": availability
            }

            self.books.append(book_dict)
        
        return self.books

# scrapper = WebsiteScrapper()
# topics = scrapper.get_books_topics()
# books = scrapper.get_books()

# print("--------------------- Topics--------------------------")
# print(topics)
# print("--------------------- Books--------------------------")
# print(books)

topic = input("Enter a topic: ")
scrapper = WebsiteScrapper()
topics = scrapper.get_books_topics()

if topic in topics:
    print("Your entered topic is found in website topic list")
else: 
    print("Your entered topic is not found in website topic list")