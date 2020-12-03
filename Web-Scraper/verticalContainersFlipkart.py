def verticalContainer(vertical_containers, query, file, n):
    for vertical_container in vertical_containers:

        item = vertical_container.find("div", {"class": "_4ddWXP"})
        item_price = vertical_container.find("div", {"class": "_30jeq3"})
        item_rating = vertical_container.find("div", {"class": "_3LWZlK"})

        try:
            file.write(item.find("a", {"class": "s1Q9rs"}).text.replace(",", "|") + "," + (
                item_price.text.replace(",", "")).replace("₹", "") + "," + item_rating.text + "\n")
        except:
            file.write(item.find("a", {"class": "s1Q9rs"}).text.replace(",", "|") + "\n")

    my_url = "https://www.flipkart.com/search?q=" + query + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(
        n)
