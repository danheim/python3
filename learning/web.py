import bs4
import requests

res = requests.get("https://www.example.com")
soup = bs4.BeautifulSoup(res.text, "lxml")

print(soup)
