def watchContainer(watch_containers, query, file, n):
    for watch_container in watch_containers:

        item = watch_container.find("a", {"class": "IRpwTa"})
        item_price = watch_container.find("div", {"class": "_30jeq3"})

        try:
            file.write(item.text.replace(",", "|") + "," + ((item_price.text).replace(",", "")).replace("₹", "") + "\n")
        except:
            file.write(item.text.replace(",", "|") + "\n")

    my_url = "https://www.flipkart.com/search?q=" + query + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(
        n)
