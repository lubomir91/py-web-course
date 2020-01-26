import requests
from bs4 import BeautifulSoup

#https://www.johnlewis.com/magimix-power-blender/satin/p3336949
#<p class="price price--large">£199.99</p>

request = requests.get("https://www.johnlewis.com/magimix-power-blender/satin/p3336949")
content = request.content
print(content)
soup = BeautifulSoup(content, 'html.parser')
element = soup.findAll("p", {"class" : "price price--large"})

print(element)

print("\nStatus code: {}".format(request.status_code))
