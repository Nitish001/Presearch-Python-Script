import time
import requests
from bs4 import BeautifulSoup
import random

email = "Enter your email"
password = "Enter your password"

r = requests.Session()
content = r.get("https://www.presearch.org").content

soup = BeautifulSoup(content, 'html.parser')
token = soup.find("input", {
  "name": "_token"
})["value"]

payload = "_token={}&login_form=1&email={}&password={}".format(token, email, password)
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

login = r.post("https://www.presearch.org/api/auth/login", data = payload, headers = headers)

for x in range(0, 10):
    words = random.choice(["apple", "life", "hacker", "facebook", "abeyancies", "abeyancy", "abeyant", "abfarad", "abfarads", "abhenries", "abhenry", "abhenrys", "abhominable", "abhor", "abhorred", "abhorrence", "abhorrences", "abhorrencies", "abhorrency", "abhorrent", "abhorrently", "abhorrer", "abhorrers", "abhorring", "abhorrings", "abhors", "abid", "abidance", "abidances", "abidden", "abide", "abided", "abider", "abiders", "abides", "abiding", "abidingly", "abidings", "abies", "abietic", "abigail", "abigails", "abilities", "ability", "abiogeneses", "abiogenesis", "abiogenetic", "abiogenetically", "abiogenic", "abiogenically", "abiogenist", "abiogenists", "abiological", "abioses", "abiosis", "abiotic", "abiotically", "abiotrophic", "abiotrophies", "abiotrophy"])
    payload = "term={}&provider_id=98&_token={}".format(words, token)
    r.post("https://www.presearch.org/search", data = payload, headers = headers)
    print("Term:{} Search done!".format(words))
    time.sleep(10)
r = r.get("https://www.presearch.org/")
soup = BeautifulSoup(r.content, 'html.parser')
balance = soup.find("span", {
  "class": "number ajax balance"
})
print("Your Balance: {} PRE".format(balance.text))
