# eMAG Price Tracker
## Overview
eMAG Price Tracker is a Python application that checks for price drops on a specific product from the eMAG.ro website and sends an SMS alert when the price decreases. This documentation covers the application's Python modules: main.py, notification_manager.py, and web_scraper.py. The project was then uploaded on an AWS EC2 instance and is scheduled to run every hour using cron.

## Modules
### main.py
This is the main driver script that utilizes the other two modules to track the price of an item and send notifications accordingly.
#### Functions
* write_price(): Saves the new price to price.txt.
* read_price(): Reads the last known price from price.txt or creates the file if it doesn't exist.
#### Execution Flow
1. The product URL is specified.
2. The Web_Scraper class from web_scraper.py is used to scrape the current price of the product.
3. The script reads the last known price from price.txt.
4. It compares the new price with the old price.
5. If the new price is lower, it writes the new price to price.txt and sends an SMS alert using the NotificationManager class from notification_manager.py.
### notification_manager.py
Contains the NotificationManager class responsible for sending SMS notifications.
Class: NotificationManager
#### Methods
__init__(self, msg): Constructor that sends an SMS with the message msg.
Environmental Variables
ACC_SID: Twilio Account SID.
AUTH_TOKEN: Twilio Auth Token.
PHONE_NUM: The phone number to which the SMS will be sent.
### web_scraper.py
Contains the Web_Scraper class that scrapes the eMAG website for the current price of the product.
Class: Web_Scraper
#### Attributes
price: The scraped price of the product.
#### Methods
__init__(self, URL): Constructor that takes the product URL and scrapes the price using BeautifulSoup and requests.
#### Constants
HEADERS: A dictionary of HTTP headers used for the web scraping request.
## Usage
To use the eMAG Price Tracker:
1. Set up environmental variables for Twilio in a .env file.
2. Run main.py either manually or set it up to run periodically, e.g., with a cron job on a server.
## Error Handling
* The read_price() function in main.py handles the FileNotFoundError by creating a price.txt file if it does not exist.
* Twilio-related errors should be handled within the NotificationManager but are not explicitly documented.
## Dependencies
* Python 3.x
* requests library for making HTTP requests.
* beautifulsoup4 library for parsing HTML.
* twilio library for sending SMS messages.
* python-dotenv library for loading environmental variables.

## Example:
 ![image](https://github.com/seyf97/eMAG-Price-Tracker/assets/111386377/69cc2e02-3602-4647-8896-3a28ea963dfc)
