from bs4 import BeautifulSoup
import requests

url = 'http://commencal-russia.ru/product-category/bikes/2020/enduro-2020/'
r = requests.get(url)
with open('test.html', 'wb') as out:
    out.write(r.text.encode('cp1251'))

with open('test.html') as input_file:
    text = input_file.read() 

soup = BeautifulSoup(text)
bike_list = soup.find('ul', {'class': 'products columns-3'})
bikes = bike_list.find_all('a', {'class': 'woocommerce-LoopProduct-link woocommerce-loop-product__link'})
for bike in bikes:
    bikeName = bike.find('h2').text
    bikePrice = bike.find('span').text
    print(bikeName + ": " + bikePrice)