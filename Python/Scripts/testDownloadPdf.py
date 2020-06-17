#this is a test file to download a pdf file from a link
#is a part of basicWebScrapper.py 
import os, re, webbrowser
from pathlib import Path
from urllib.request import urlopen as uReq
from bs4 import  BeautifulSoup as soup
from bs4 import Tag

url = 'http://link.springer.com/openurl?genre=book&isbn=978-3-319-43341-7' 
uClient = uReq(url)
download_html = uClient.read()
uClient.close()
download_soup = soup(download_html, "html.parser")
os.chdir(Path.home() / 'Documents')
for i, link in enumerate(download_soup.find_all('a')):
    pdfLink = link.get('href')
    if pdfLink.endswith('.pdf'):
        print('founded:     ' + pdfLink)
        webbrowser.get('firefox').open_new_tab('https://link.springer.com' + pdfLink)
        '''uClient = uReq('https://link.springer.com' + pdfLink)
        pdf = open(Path.cwd() / namePdf, 'wb')
        pdf.write(uClient.read())
        pdf.close()
        uClient.close()'''
        break