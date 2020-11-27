from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
strings = ["Name: ","Favorite Color: "]
for string in strings:
    start_index = html.find(string)
    actual_text_index = start_index + len(string)
    html_tag_index = html[actual_text_index:].find('<')
    text_end_index = actual_text_index + html_tag_index
    raw_text = html[actual_text_index:text_end_index]
    print(raw_text)
