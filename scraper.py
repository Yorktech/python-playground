import requests
from bs4 import BeautifulSoup
import asyncio
from pyppeteer import launch
import csv


# get page data
async def extract_page_html():
    # Launch the browser
    browser = await launch()

    # Create a new page
    page = await browser.newPage()
    dropdown_selector = '#perpage'

    # Navigate to the desired URL
    await page.goto('"https://www.scotchwhiskyauctions.com/auctions/188-the-143rd-auction/?page=1')
    option_value = 500
    # Wait for any necessary page loading or rendering
    await page.waitForSelector(dropdown_selector)
    await page.waitForSelector(dropdown_selector, option_value)
    # Get the HTML content of the page
    content = await page.content()

    # Close the browser
    await browser.close()

    return content


def parse_html(html_content):
    
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <a> tags with class "lot" within the <div id="lots"> element
    lots = soup.select('div#lots a.lot')

    # Create a CSV file and write the headers
    with open('page3.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Image URL', 'Lot Number',
                    'Sale Status', 'Auction Link'])

        # Iterate over each lot and extract the information
        for lot in lots:
            title = lot.select_one('h4').text
            image_url = lot.select_one('div.aucimg')[
                'style'].split("('")[1].split("')")[0]
            lot_number = lot.select_one('h6').text.split()[-1]
            sale_status = lot.select_one('div[id^="info_"]').text.strip()
            auction_link = lot['href']

            # Write the extracted information to the CSV file
            writer.writerow([title, image_url, lot_number,
                        sale_status, auction_link])

    print('Data has been written to lots_data.csv')

async def extract_and_parse():
    html_content = await extract_page_html()
    parse_html(html_content)
    


loop = asyncio.get_event_loop()
loop.run_until_complete(extract_and_parse())
print("Finished")
