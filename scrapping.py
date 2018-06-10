import bs4 as bs
import urllib.request


# getting the source code
sauce = urllib.request.urlopen('https://www.booking.com/').read()


# turn the source code into bsoup object
soup = bs.BeautifulSoup(sauce, 'lxml')


# Booking´s promotions
def get_promotions():
    for div in soup.find_all('div', class_='promotion-postcards-list'):
        a = div.find_all('a')
        print(a)


get_promotions()




# Booking's accommodations on the home page
def get_accommodations():
    for div in soup.find_all('div', class_='d-bh-promotion--overflow '):
        a = div.find_all('a')
        print(a)


#get_accommodations()

# popular destinations
def get_popular_destinations():
    for ul in soup.find_all('ul', class_='b-popular_list lp_endorsements_popular_destinations_container'):
        li = ul.find_all('a')
        print(li)



# get_popular_destinations()


# Discover with booking
def discover_destinations():
    for p in soup.find_all('div', class_='dcbi-country__container'):
        a = p.find_all('p')
        print(a)


# discover_destinations()

