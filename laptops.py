import requests as r 
from selectolax.parser import HTMLParser

resp = r.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
tree = HTMLParser(resp.content)