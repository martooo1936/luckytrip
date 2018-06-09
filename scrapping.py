import bs4 as bs
import urllib.request


# getting the source code
sauce = urllib.request.urlopen('https://www.booking.com/').read()


# turn the source code into bsoup object
soup = bs.BeautifulSoup(sauce, 'lxml')


# printing the html
# print(soup.title.string)

# print(soup.find_all('p'))

# for p in soup.find_all('p'):
#   print(p.string)

""" scrapping for links
# for ulr in soup.find_all('a'):
#   print(ulr.get('href'))
"""


