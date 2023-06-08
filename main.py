import requests
from bs4 import BeautifulSoup
import csv
import re

website_url = "https://www.washingtonpost.com/world/ukraine-russia/"

class WebsiteScrapper: 
    def __init__(self) -> None:
        self.washingtonposts = []
    
    def _get_website_content(self,url):
        response = requests.get(url)
        self._content = response.content
        self._soup = BeautifulSoup(self._content, 'html.parser')
        return self._soup


    def get_washingtonposts(self):
        articles=""
        images = ""
        title=""
        mainsite = self._get_website_content(website_url)
        alldivs  = mainsite.find_all('div')

        for alldiv in alldivs:
            # print(href.get("href"))
            datafeature = alldiv.get("data-feature-id")
            if datafeature=='homepage/story':
                href = alldiv.find('div',class_='headline relative gray-darkest pb-xs').find('a').get('href')
                title = alldiv.find('div',class_='headline relative gray-darkest pb-xs').find('a').text
                # print(title)
                # print(href)
                self._contenteachpost = self._get_website_content(href)
               
                article  = self._contenteachpost.find('article')
                allarticle = article.find_all('div',class_='article-body')
                for eacharticle in allarticle:
                    # print(eacharticle.text.strip())
                    each = eacharticle.text.strip()
                    articles += each
                
                allimagediv=self._contenteachpost.find_all('img') 
                for imagediv in allimagediv:
                    imagesrc = imagediv.get('src')
                    imagesrcset = imagediv.get('srcset')
                    if imagesrcset:
                        imagesrcfinal = imagesrcset.split(',')[0]
                        images += imagesrcfinal + ','*1
                        # print(imagesrcfinal)
                    if imagesrc:
                        images += imagesrc + ','*1
                        # print(imagesrc)
                     
                post_dict={
                    "title": title,
                    "content": articles,
                    "images": images
                }

                self.washingtonposts.append(post_dict)
        return self.washingtonposts
            

scrapper = WebsiteScrapper()
allposts = scrapper.get_washingtonposts()
print(allposts)
# books = scrapper.get_books()
# print(books)

header =['title', 'content', 'images']

csv_file = "washingtonpost.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for data in allposts:
            writer.writerow(data)
except IOError:
    print("I/O error")

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