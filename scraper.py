import requests
from bs4 import BeautifulSoup
import re
import pdb
import pprint
from datetime import datetime


def get_page_source():
    request_object = requests.get("https://www.greentribunal.gov.in/western-zone-cause-list", verify=False)
    return request_object._content



def get_soup(page_source):
    soup = BeautifulSoup(page_source, features="html.parser")
    return soup


def get_all_links(soup):
    table = soup.find_all("table", attrs={"class":"views-table cols-2 table custm-tbl table-bordered"})
    links = []

    for i in table:
        links.append(i.find_all("a",href=True, attrs={"target":"_blank"}))
    return links[0]


def get_cause_list_links(links):
    cause_list_links = []

    for link in links:
        content = str(link.contents[0])
        if not (re.search("Advance+", content) or re.search("Supplementary+", content)):
            date = content[22:content.index(",")]
            if "1st" in date:
                date = datetime.strptime(date, "%dst %B %Y")
            elif "rd" in date:
                date = datetime.strptime(date, "%drd %B %Y")
            elif "nd" in date:
                date = datetime.strptime(date, "%dnd %B %Y")
            else:
                date = datetime.strptime(date, "%dth %B %Y")

            if(date>=datetime.now()):
                cause_list_links.append(link.get('href'))
    print(cause_list_links)
    return cause_list_links

def run():
    source = get_page_source()
    soup = get_soup(source)
    links = get_all_links(soup)
    cause_lists = get_cause_list_links(links)
    return cause_lists

if __name__ == '__main__':
    run()