import requests
from bs4 import BeautifulSoup

m = "https://www.thespike.gg"
url = "https://www.thespike.gg/events/"

req = requests.get(url)
soup = BeautifulSoup(req.content,"html.parser")

f = soup.find_all("ul",{"class":"events-overview-lists"})

a = []
for i in f:
    l = i.find("a")
    a.append(l.get("href"))


main_url = m + a[0]

print(main_url)

r = requests.get(main_url)
s = BeautifulSoup(r.content,"html.parser")


ss = s.find_all("div",{"class":"first-team"})


with open('game.txt','w+') as f:
    for j in ss:
        print(j.text.strip())
        f.write(j.text.strip() + "\n")

# print(aq)