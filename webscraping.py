import requests
from bs4 import BeautifulSoup
#
# r = requests.get("http://testing-ground.scraping.pro/table")
# c = r.content
#
# soup = BeautifulSoup(c, "html.parser")
# # all = soup.find_all("div", {"class": "cities"})[0]
# # use the find_all method to return elements of html with a particular
# # this method returns a list. so you can refer to an index in the list.
#
# # all[0].find_all("h2")[0].text
# # .text method returns the text in the element/ tag
#
# with open("HtmlScrap.html", "w") as file:
#     file.writelines(soup.prettify() + "\n")
#
# for item in all:
#     print(item.find_all("h2")[0].text)

r=requests.get("http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/?")
c=r.content
soup = BeautifulSoup(c, "html.parser")

print(soup.prettify())