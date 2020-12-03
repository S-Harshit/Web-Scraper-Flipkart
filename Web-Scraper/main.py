from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import horizontalContainersFlipkart
import verticalContainersFlipkart
import watchTypeContainer
import DataOperations


# Flipkart Scraper
# # CSV File
def main():
    print("{:^30}".format(
        "\n\n||||||||||||||||||||||||||||||||||||||| FLIPKART SCRAPER ||||||||||||||||||||||||||||||||||||||||||||||||\n"))

    file = open("FlipkartScraped.csv", "w+", encoding='utf-8')
    headers = "ITEMS,PRICE,Ratings\n"
    file.write(headers)

    query = input("Enter What you Want To Search on Flipkart\n").replace(" ", "%20")

    # URL of Website
    my_url = "https://www.flipkart.com/search?q=" + query + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

    while True:
        try:
            pages = int(input("How Many Pages Do You Want To search\n"))
            break
        except:
            print("Please Enter Correct Input")

    #Requesting Webpage
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")  # Using HTML Parser

    # These Are the Three Different Type Of Html Containers present on Flipkart
    vertical_containers = page_soup.find_all("div", {"style": "width:25%"})
    horizontal_containers = page_soup.find_all("div", {"class": "_3pLy-c row"})
    special_type = page_soup.find_all("div", {"class": "_2B099V"})


    for n in range(1, pages + 1):
        if special_type:
            watchTypeContainer.watchContainer(special_type, query, file, n)
        elif horizontal_containers:
            horizontalContainersFlipkart.horizontalContainer(horizontal_containers, query, file, n)
        elif vertical_containers:
            verticalContainersFlipkart.verticalContainer(vertical_containers, query, file, n)
    file.close()


if __name__ == '__main__':
    main()

DataOperations.analyzingData()
