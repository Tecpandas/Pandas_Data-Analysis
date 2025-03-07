# requests module
import requests as r
from bs4 import BeautifulSoup
from selenium import webdriver 
from lxml import html
r = r.get('https://www.geeksforgeeks.org/python-programming-language/')
print(r)
print(r.content)
#parsing using html
soup=BeautifulSoup(r.content,'html.parser')
print(soup.prettify)
s = soup.find('div', class_='entry-content')
content = soup.find_all('p')
# import webdriver 


# create webdriver object 
driver = webdriver.Firefox() 

# get google.co.in 
driver.get("https://google.co.in / search?q =geeksforgeeks") 
url="https://google.co.in / search?q =geeksforgeeks"
response=r.get(url)
tree = html.fromstring(response.content)
link_titles = tree.xpath('//a/text()')

# Print the extracted link titles
for title in link_titles:
    print(title)