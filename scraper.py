from cmath import log
import requests
from bs4 import BeautifulSoup
import re
import os
import logging
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
    #pdb.set_trace()
    for link in links:
        content = str(link.contents[0])
        if not (re.search("Advance+", content) or re.search("Supplementary+", content)):
            date = content[22:content.index(",")]
            if "1st" in date:
                date = datetime.strptime(date, "%dst %B %Y").date()
            elif "rd" in date:
                date = datetime.strptime(date, "%drd %B %Y").date()
            elif "nd" in date:
                date = datetime.strptime(date, "%dnd %B %Y").date()
            else:
                date = datetime.strptime(date, "%dth %B %Y").date()

            if(date >=datetime.now().date()):
                cause_list_links.append(link.get('href'))
    print(cause_list_links)
    return cause_list_links


def download_files(path, links):
    if links is None:
        logging.warning('No links')
        return
    try:
        os.mkdir(path)
    except:
        logging.warning('Path already exists')
    for link in links:
        if not (link.endswith('.pdf')):
            logging.error('Bad Link')
            continue
        request = requests.get(link, allow_redirects=True, verify=False)
        if request.headers.get('Content-Type') != 'application/pdf':
            logging.error('Bad file, check your link')
            continue
        content = request.content
        file_name = "CauseList "+datetime.now().strftime("%d %B")+".pdf"
        file = os.path.join(path, file_name)
        with open(file, 'wb') as f:
            f.write(content)
        

def run():
    source = get_page_source()
    soup = get_soup(source)
    links = get_all_links(soup)
    cause_lists = get_cause_list_links(links)
    return cause_lists

if __name__ == '__main__':
    links = run()
    download_files(os.path.dirname(__file__), links)
