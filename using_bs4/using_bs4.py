from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup)
print(soup.get_text())

images = soup.find_all("img")
print(images)
print(images[0])

Title = soup.title
print(Title)

title_string = soup.title.string
print(title_string)

find_img_with_value = soup.find_all("img", src="/static/dionysus.jpg")
print(find_img_with_value)

#Exercise1: get all the href links from the url
base_url = "http://olympus.realpython.org"
url1 = "http://olympus.realpython.org/profiles"
page1 = urlopen(url1)
html1 = page1.read().decode("utf-8")
soup1 = BeautifulSoup(html1, "html.parser")

print(soup1)
print(soup1.get_text())

anchors = soup1.find_all("a")
print(anchors)

for anchor_link in anchors:
    links = base_url + anchor_link["href"]
    print(links)
