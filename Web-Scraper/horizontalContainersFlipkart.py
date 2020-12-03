def horizontalContainer(horizontal_containers, query, file, n):
    for container in horizontal_containers:
        item_price = container.find("div", {"class": "_30jeq3 _1_WHN1"})
        item = container.find("div", "_4rR01T")
        item_rating = container.find("div", {"class": "_3LWZlK"})

        try:
            file.write(item.text.replace(",", "|") + "," + ((item_price.text).replace(",", "")).replace("₹",
                                                                                                        "") + "," + item_rating.text + "\n")
        except:
            file.write(item.text.replace(",", "|") + "\n")

        my_url = "https://www.flipkart.com/search?q=" + query + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(
            n)
