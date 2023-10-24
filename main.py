from notification_manager import NotificationManager
from web_scraper import Web_Scraper

URL = ("https://www.emag.ro/cana-termica-de-cafea-idepetr-din-inox-cu-pereti-dubli-"
       "si-capac-510-ml-negru-6450222124178/pd/DKS7CBYBM/?ref=sponsored_products_"
       "search_r_k_ra_1_12&recid=recads_1_"
       "e7cb6848bc54881b8e61327e802d4b40c027387f0c6be19fa3a154e622d74bb8_1698075789&aid=8d0a907e"
       "-3746-11ee-bb1a-0a7fcd8863b2&oid=127545075&scenario_ID=1")

def write_price():
    with open("price.txt", "w") as file:
        file.write(str(new_price))

def read_price():
    try:
        with open("price.txt", "r") as file:
            return float(file.read())
    except FileNotFoundError:
        write_price()
        print("New file created")
        return read_price()


new_price = Web_Scraper(URL).price
old_price = read_price()

# Compare prices:
if new_price < old_price:
    # Save the price
    write_price()
    # Send SMS
    msg = f"Discount!\nProduct price 🔽 from {old_price} to {new_price}.\nLink:{URL}"
    notification_manager = NotificationManager(msg)
    print("Sending notification...")
else:
    print("Still expensive...")