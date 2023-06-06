import requests
from bs4 import BeautifulSoup
import csv

# Make a GET request to the web page
url = "https://www.scotchwhiskyauctions.com/auctions/188-the-143rd-auction/?page=1"  # Replace with the actual URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all <a> tags with class "lot" within the <div id="lots"> element
    lots = soup.select('div#lots a.lot')
    
    # Create a CSV file and write the headers
    with open('page1.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Image URL', 'Lot Number', 'Sale Status', 'Auction Link'])
        
        # Iterate over each lot and extract the information
        for lot in lots:
            title = lot.select_one('h4').text
            image_url = lot.select_one('div.aucimg')['style'].split("('")[1].split("')")[0]
            lot_number = lot.select_one('h6').text.split()[-1]
            sale_status = lot.select_one('div[id^="info_"]').text.strip()
            auction_link = lot['href']
            
            # Write the extracted information to the CSV file
            writer.writerow([title, image_url, lot_number, sale_status, auction_link])
            
    print('Data has been written to lots_data.csv')
else:
    print('Failed to retrieve the web page. Status Code:', response.status_code)
