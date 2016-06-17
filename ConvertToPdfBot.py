import urllib2
import re
import pdfkit
from bs4 import BeautifulSoup
import os.path

def crawl_page(url):
    try:
      response=urllib2.urlopen(url['href'])
      content=(response.read()).decode('utf-8','ignore')
      soup = BeautifulSoup(content)
      print("Converting-"+url['href'])
      fname=''+(soup.title.string).encode("utf-8","ignore")
      fileobj=open(fname+'.html','a')
      div = soup.findAll("p")
      #fileobj.write(''.join(map(str,div)))
      fileobj.write('<head><meta charset="UTF-8"></head>')
      fileobj.write(''.join(map(str,div)))
      fileobj.close()
      pdfkit.from_file(str(fname+'.html'),'pdf/'+fname+'.pdf')
      return 1
    except Exception as e:
        print(e)
        return -1

try:
 url='http://www.insightsonindia.com/the-big-picture-debates/'
 response=urllib2.urlopen(url)
 content=response.read()
 soup = BeautifulSoup(content)
 for a in soup.find_all('a',href=re.compile('http://www.insightsonindia.com/2016')):
     crawl_page(a)
except Exception as e:
    print(e)
