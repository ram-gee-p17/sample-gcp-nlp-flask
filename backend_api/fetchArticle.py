import urllib.request
from bs4 import BeautifulSoup
import re

def getSubstring(ch1,ch2,str):
    m = re.search(ch1+'(.+?)'+ch2, str)
    if m:
        s2 = m.group(1)
    return s2

def fetchArticleDeatils(url):
    response = urllib.request.urlopen(url)
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    return (re.compile(r'<[^>]+>')).sub('',str(soup.find("div",{"class":"rich-text"})))
    

def pushArticleToDataStore(linkfile):
    file1 = open(linkfile, 'r')
    Lines = file1.readlines()
    
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        response=fetchArticleDeatils(line)
        filename=(line.split("/")[-1]).split("?")[-2]+".txt"
        #print("Link will be "+line+" \n & filename - ",filename)
        file2 = open(filename, 'w')
        file2.write(str(response))
        file2.close()

if __name__ == "__main__":
    pushArticleToDataStore('articlelinks.txt')
