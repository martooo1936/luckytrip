import requests
from bs4 import BeautifulSoup


page = requests.get('https://www.booking.com/')

soup = BeautifulSoup(page.text, 'html.parser')



artist_name_list = soup.find(class_='promotion-postcards-list')
artist_name_list_items = artist_name_list.find_all('a')

# Use .contents to pull out the <a> tag’s children
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    link = 'https://www.booking.com'
    a = artist_name.get('href')
    #print(names)
    print(link,a)