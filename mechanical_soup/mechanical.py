import mechanicalsoup

browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
page = browser.get(url)
print(page)
content = page.soup
print(content)




# 1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# 2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3
profiles_page = browser.submit(form, login_page.url)
print(profiles_page.url)

print(profiles_page.soup.title)# show title tag


links = profiles_page.soup.select("a")
base_url = "http://olympus.realpython.org"

for link in links:
    address = base_url + link["href"]
    text = link.text
    print(f"{text}: {address}")
