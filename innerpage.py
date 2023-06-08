import requests
from bs4 import BeautifulSoup
import csv

website_url = "https://www.washingtonpost.com/world/2023/06/05/belgorod-russia-ukraine-counteroffensive-militias/"

class WebsiteScrapper: 
    def __init__(self) -> None:
        self.washingtonposts = []
        self._content = self._get_website_content(website_url)
        self._soup = BeautifulSoup(self._content, 'html.parser')
    
    def _get_website_content(self,url):
        response = requests.get(url)
        return response.content


    def get_washingtonposts(self):
        newslink = []
        all_hrefs = []
        titles=[]
        alldivs  = self._soup.find_all('article')
        # print(alldivs)

        for alldiv in alldivs:
            print(alldiv.find_all('img'))
            # if alldiv.find('div',class_='article-body'):
            #     articlebody = alldiv.find('div',class_='article-body').text
            # datafeature = alldiv.get("data-feature-id")
            # if datafeature=='homepage/story':
            #     href = alldiv.find('div',class_='headline relative gray-darkest pb-xs').find('a').get('href')
            #     print(href)
            #     self._contenteachpost = self._get_website_content(href)
            #     self._soupeachpost = BeautifulSoup(self._content, 'html.parser')
            #     article=self._soupeachpost.find('div', class_='grid-layout')
                # print(articlebody)
                # if singlenewslink=='web_headline':
                #     title = alldiv.find('a').text
                #     links = alldiv.find('a').get("href")
                #     newslink.append(links)
                #     titles.append(title)

        # print(titles)
    #     div = section.find_all("div")[1]
    #     ol = div.find("ol")
    #     all_li = ol.find_all("li")

    #     for li in all_li:
    #         article = li.find("article")
    #         src = article.find("div", class_="image_container").find("a").find("img").get("src")
    #         title = article.find("h3").find("a").get("title")
    #         product_price_div = article.find("div",class_="product_price")
    #         price = product_price_div.find("p",class_="price_color").text
    #         availability = product_price_div.find("p", class_="instock").text.strip()
    #         book_dict={
    #             "book_title": title,
    #             "image_url": f"http://books.toscrape.com/{src}",
    #             "book_price": price,
    #             "is_available": availability
    #         }
             

    #         self.books.append(book_dict)
        
    #     return self.books
    
    # def get_books_bytitle(self, topic):
    #     print(f"Your entered {topic} is found in website topic list")

scrapper = WebsiteScrapper()
allposts = scrapper.get_washingtonposts()
# print(allposts)
# books = scrapper.get_books()
# print(books)

# header =['book_title', 'image_url', 'book_price', 'is_available']

# csv_file = "booklist.csv"
# try:
#     with open(csv_file, 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=header)
#         writer.writeheader()
#         for data in books:
#             writer.writerow(data)
# except IOError:
#     print("I/O error")

# print("--------------------- Topics--------------------------")
# print(topics)
# print("--------------------- Books--------------------------")
# print(books)

# topic = input("Enter a topic: ")
# scrapper = WebsiteScrapper()
# topics = scrapper.get_books_topics()

# if topic in topics:
#     scrapper.get_books_bytitle(topic)
# else: 
#     print("Your entered topic is not found in website topic list")