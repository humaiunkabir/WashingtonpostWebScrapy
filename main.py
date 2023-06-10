import requests
from bs4 import BeautifulSoup
import csv

website_url = "https://www.washingtonpost.com/world/ukraine-russia/"


class WebsiteScrapper:

    washingtonpostsdata = []

    # Function for get content by calling beautifulsoup
    def get_website_content(self, url):
        response = requests.get(url)
        self._content = response.content
        self._soup = BeautifulSoup(self._content, 'html.parser')
        return self._soup

    # To get all news post in list
    def get_washingtonposts(self):
        # Get main site content
        mainsite = self.get_website_content(website_url)
        alldivs = mainsite.find_all('div')

        for alldiv in alldivs:
            articles = ""
            images = ""
            title = ""
            datafeature = alldiv.get("data-feature-id")
            if datafeature == 'homepage/story':
                # Scrap individual url of each post.
                href = alldiv.find(
                    'div', class_='headline relative gray-darkest pb-xs').find('a').get('href')
                # Scrap individual title of each post.
                title = alldiv.find(
                    'div', class_='headline relative gray-darkest pb-xs').find('a').text

                # Get individual page content
                contenteachpost = self.get_website_content(href)

                # Scrap content and resize data start
                article = contenteachpost.find('article')
                if article is not None:
                    allarticle = article.find_all('p', class_='wpds-c-cYdRxM wpds-c-cYdRxM-iPJLV-css overrideStyles font-copy')
                    for eacharticle in allarticle:
                        each = eacharticle.text.strip()
                        articles += each
                # Scrap content and resize data end

                # Scrap images and resize images url start
                allimagediv = contenteachpost.find_all('img')

                for imagediv in allimagediv:
                    imagesrc = imagediv.get('src')
                    imagesrcset = imagediv.get('srcset')
                    if imagesrcset:
                        imagesrcfinal = imagesrcset.split(',')[0]
                        images += imagesrcfinal + ','*1
                    if imagesrc:
                        images += imagesrc + ','*1
                # Scrap images and resize images url end

                # Check title, content and images blank value
                if title and articles and images:
                    # Dictionary to get of each record.
                    post_dict = {
                        "title": title,
                        "content": articles,
                        "images": images
                    }
                # Each dictionary append in this list
                self.washingtonpostsdata.append(post_dict)
        return self.washingtonpostsdata


# Call this scrapper
scrapper = WebsiteScrapper()
# Get all post
allposts = scrapper.get_washingtonposts()

# CSV file header row
header = ['title', 'content', 'images']

# CSV file name
csv_file = "washingtonpost.csv"
try:
    # Write data in csv file
    with open(csv_file, 'w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for data in allposts:
            writer.writerow(data)
except IOError:
    print("I/O error")