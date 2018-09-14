import urllib.request
from bs4 import BeautifulSoup
import re
import time


def get_linked_page(link_content):
    link_container = link_content.find("a")
    next_url = link_container["href"]
    request = urllib.request.Request(next_url)
    response = urllib.request.urlopen(request)
    page_text = response.read().decode('utf-8')
    soup = BeautifulSoup(page_text, "html.parser")
    page_content = soup.find(class_='body')
    filename = next_url.split("/")[-2]
    page_text = page_content.text
    if len(page_text) > 250:
        dataout = open("./data/" +  filename, "w", encoding='utf-8')
        dataout.write(page_text)
        dataout.close()



def get_links(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    page_text = response.read().decode('utf-8')
    soup = BeautifulSoup(page_text, "html.parser")
    # data = soup.findAll(text=True)
    link_item = soup.findAll(class_='item')
    for item in link_item:
        get_linked_page(item)
        time.sleep(1)


base_search = "http://www.dodig.mil/reports.html/Category/15304/Year/2018/?Page="

for page_num in list(range(1, 11)):
    search_page = base_search + str(page_num)
    get_links(search_page)