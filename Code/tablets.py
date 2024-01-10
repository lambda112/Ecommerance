import requests as r 
import pandas as pd
from selectolax.parser import HTMLParser

resp = r.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets")
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

def get_amount_reviews():
    review_amount = [i.text() for i in tree.css("div.ratings p:first-child")]
    return review_amount

def table():
    item_info = {
        "Item": get_item_name(),
        "Price": get_item_price(),
        "Rating": get_item_rating(),
        "AmountOfReviews": get_amount_reviews()
    }

    table = pd.DataFrame(item_info).set_index("Item")
    return table.to_excel("Tablets.xlsx")

table()
