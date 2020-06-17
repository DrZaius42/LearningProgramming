#this a basic webscrapper to download pdf files from a webpage
import re, os
from pathlib import Path
from urllib.request import urlopen as uReq
from bs4 import  BeautifulSoup as soup
from bs4 import Tag

#openning connection, grabbing the page
uClient = uReq("https://hnarayanan.github.io/springer-books/#Computer%20Science")
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

#separates by categories and gets links
#and stores them in dict of the form category : list of links
categories = {}
for header in page_soup('h2'):
    if 'Categories' in header:
        continue
    nextNode = header
    links = []
    while True:
        nextNode = nextNode.nextSibling
        if nextNode is None:
            break
        if isinstance(nextNode, Tag):
            if nextNode.name == 'h2':
                break
            if nextNode.name == 'div':
                links = list(nextNode.find_all(href=re.compile("springer")))
                linksRegex = re.compile(r'href="(.*)"')
                for i in range(len(links)):
                    mo = linksRegex.findall(str(links[i]))
                    mo[0] = mo[0].replace('&amp;', '&')
                    links[i] = mo[0]
    idRegex = re.compile(r'id="(.*)"')
    categoryName = idRegex.findall(str(header))[0]
    categories[categoryName] = links

#creates a folder for each category and downloads the pdf's to it
mainFolder = Path.home() / 'Documents/BooksWebScrapper'
while True:
    try:
        os.chdir(mainFolder) 
    except:
        os.mkdir(mainFolder) 
        continue
    break
for entry, listLinks in categories.items():
    while True:
        try:
            os.chdir(Path.cwd() / entry)
        except:
            os.mkdir(Path.cwd() / entry)
            continue
        break
    for link in listLinks:
        uClient = uReq(link)
        download_html = uClient.read()
        uClient.close()
        download_soup = soup(download_html, "html.parser")
        for i in download_soup.find_all('a'):
            pdfLink = i.get('href')
            if pdfLink.endswith('.pdf'):
                namePdf = i.attrs['href']
                uClient = uReq('https://link.springer.com' + pdfLink)
                pdf = open(Path.cwd() / namePdf, 'wb')
                pdf.write(uClient.read())
                pdf.close()
                uClient.close()
                break
    os.chdir(mainFolder)

    


