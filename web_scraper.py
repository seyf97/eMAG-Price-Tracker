from bs4 import BeautifulSoup
import requests

HEADERS = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0",
    "Accept" : "text/html,application/xhtml",
    "Accept-Language" : "en-US,en;q=0.9,de-DE;q=0.8,de;q=0.7,ro;q=0.6,tr;q=0.5",
    "Accept-Encoding" : "gzip, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests" : "1",
    "Sec-Fetch-Dest" : "iframe",
    "Sec-Fetch-Mode" : "navigate",
    "Sec-Fetch-Site" : "same-origin",
    "Sec-Fetch-User" : "?1",
    "Cache-Control" : "max-age=0"}

class Web_Scraper:

    def __init__(self, URL):
        resp = requests.get(url=URL)
        soup = BeautifulSoup(resp.text, "html.parser")
        el = soup.find(name="div", attrs={"class": "highlight-content"}).find_next(name="p",attrs={"class": "product-new-price"})
        self.price = float(el.text.replace(",", ".").replace("Lei", "").strip())


