import requests
from bs4 import BeautifulSoup
import re
import pprint

request_object = requests.get("https://www.greentribunal.gov.in/western-zone-cause-list", verify=False)
page_source = request_object._content

# print(page_source)

soup = BeautifulSoup(page_source, features="html.parser")
# print(soup)

table = soup.find_all("table", attrs={"class":"views-table cols-2 table custm-tbl table-bordered"})

links = []

for i in table:
    links.append(i.find_all("a",href=True, attrs={"target":"_blank"}))

# pprint.pprint(links[0])
links = links[0]
# pprint.pprint(links)
print(dir(links[0]))


for link in links:
    