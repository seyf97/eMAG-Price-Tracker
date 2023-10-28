# eMAG Price Tracker
 Receive an SMS alert when the product drops in price!

 The script makes a request to the specified URL, parses the HTML, and scrapes the price of the product. 
 Then, it reads the last updated price of the product from a .txt file and compares the two.
 If the new price is lower, it sends an SMS to the customer via the twilio API.
 The script runs hourly (using cron scheduling) on AWS EC2. 

 Example of a price drop:
 ![image](https://github.com/seyf97/eMAG-Price-Tracker/assets/111386377/69cc2e02-3602-4647-8896-3a28ea963dfc)
