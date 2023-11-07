from bs4 import BeautifulSoup
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache"
}


class Web_Scraper:

    def __init__(self, URL):
        resp = requests.get(url=URL)
        soup = BeautifulSoup(resp.text, "html.parser")
        el = soup.find(name="div", attrs={"class": "highlight-content"}).find_next(name="p",attrs={"class": "product-new-price"})
        self.price = float(el.text.replace(",", ".").replace("Lei", "").strip())


