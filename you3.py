import requests
from bs4 import BeautifulSoup


url = "https://www.youtube.com/channel/UCcVi5j9v6LPNBwkl7tsyuBQ/videos"

content = requests.get(url)
soup = BeautifulSoup(content.text, 'html.parser')
row = soup.findAll('a')

print(row)
for i in row:
    print(i)



# import urllib.request
# import re

# html = urllib.request.urlopen("https://www.youtube.com/c/fl0m/videos?app=desktop")
# text = html.read()
# plaintext = text.decode('utf8')
# links = re.findall("href=[\"\'](.*?)[\"\']", plaintext)
# print(links)



# from urllib.request import urlopen
# from bs4 import BeautifulSoup as soup

# my_url="https://www.youtube.com/channel/UCVlMUh4WsDQvOxCJJXmWwdw/videos"
# uClient=urlopen(my_url)
# page_html=uClient.read()
# uClient.close()
# page=soup(page_html,"html.parser")
# containers=page.findAll("div",{"class":"yt-lockup-dismissable"})
# vids = page.findAll('a',attrs={'class':'yt-uix-tile-link'})
# print(len(vids))