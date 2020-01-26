import requests
from bs4 import BeautifulSoup

#https://www.alza.sk/hracky/jenga-natur-d4321311.htm#popis
#<span class="bigPrice price_withVat">8,99&nbsp;€</span>

#request = requests.get("https://networkreload.com/contact/", verify=False)
request = requests.get("https://networkreload.com/contact/")
content = request.content
print(content)
soup = BeautifulSoup(content, 'html.parser')
element = soup.findAll("p", {"class" : "has-medium-font-size"})

print(element)

print("\nStatus code: {}".format(request.status_code))
