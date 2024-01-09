import requests as r 
from selectolax.parser import HTMLParser

resp = r.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
tree = HTMLParser(resp.content)

def get_item_name():
    name = [i.attrs["title"] for i in tree.css("div div h4 > a")]
    return name

def get_item_price():
    price = [i.text() for i in tree.css("div div > h4:first-child")]
    return price

def get_item_rating():
    rating = [i.attrs["data-rating"] for i in tree.css("div.ratings p + p")]
    return rating

