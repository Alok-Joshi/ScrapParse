from selenium import webdriver
from bs4 import BeautifulSoup


options = webdriver.FirefoxOptions()
options.add_argument("--headless")

browser_instance = webdriver.Firefox(options=options)
browser_instance.get("https://www.greentribunal.gov.in/western-zone-cause-list")
page_source = browser_instance.page_source

# print(page_source)

soup = BeautifulSoup(page_source)
# print(soup)

table = soup.find_all("table", attrs={"class":"views-table cols-2 table custm-tbl table-bordered"})

links = []
for i in table:
    links.append(i.find_all("a",href=True, attrs={"target":"_blank"}))

print(links)