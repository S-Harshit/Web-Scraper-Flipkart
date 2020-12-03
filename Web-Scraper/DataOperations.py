flag: bool = True
flag1: bool = True


def analyzingData():
    import main
    import pandas as pd
    df = pd.read_csv("FlipkartScraped.csv")
    dict = pd.Series(df.PRICE.values, index=df.ITEMS).to_dict()  ## Creating A Dict of PRICE As Values and ITEMS As Keys
    Ratio = []
    dict2 = {}
    dict3 = {}
    count = 0
    global flag1
    global flag

    while flag:
        while flag1:
            print("{:^30}".format(
                "\n\n||||||||||||||||||||||||||||||||||||||| FLIPKART SCRAPER ||||||||||||||||||||||||||||||||||||||||||||||||\n"))
            print("Press '1' To See Highest And Lowest Priced Items:")
            print("Press '2' To See The Best Budget Choice:")
            print("Press '3' To Search For A Particular Brand or Specification:")
            print("Press '4' To See Number of Items of Each brand:")
            print("Press '5' To See All Items:")
            print("Press '0' To Exit:")

            try:
                choice = int(input("\n"))
                if (choice > 5 or choice < 0):
                    print("{:^50}\n".format("'Please Enter Number Between 0-5!'"))
                else:
                    print("\n")
                    break
            except ValueError:
                print("\n{:^50}\n".format("'Wrong Input Please Enter Integer Between 0-5!'"))

        if choice == 1:
            ## Most Expensive And Least Expensive
            try:
                most_expensive = max(dict, key=dict.get)
                least_expensive = min(dict, key=dict.get)
                print("Most Expensive : {}  Priced At : {}".format(most_expensive, dict[most_expensive]))
                print("Least Expensive : {}  Priced At : {}\n".format(least_expensive, dict[least_expensive]))
            except:
                print("Not Found!")

        elif choice == 2:
            try:
                ## Best budget Choice
                # Rating To Price Ratio
                for Price, Rating, Item in zip(df.PRICE, df.Ratings, df.ITEMS):
                    Ratio.append((Rating / Price) * (1 / 5))
                    dict2[Item] = Ratio[count]
                    count += 1

                best_choice = max(dict2, key=dict2.get)
                print("\nBest Choice : {}  Priced At : {}\n".format(best_choice, dict[best_choice]))
            except:
                print("Not Found!")

        elif choice == 3:
            ## Specification Search
            try:
                flag2 = True
                searchword = input("Enter The Brand or Specification To Search\n")
                for item_name in df.ITEMS:
                    if searchword.lower() in item_name.lower():
                        print("\n" + item_name + " Priced At : {}".format(dict[item_name]))
                        flag2 = False
                if (flag2):
                    print("Specification Not Found!")
            except:
                print("Not Found!")

        elif choice == 4:
            # Number of Items Of Each brand
            try:
                for item_name in df.ITEMS:
                    list3 = item_name.split()
                    if (list3[0] in dict3):
                        dict3[list3[0]] += 1
                    else:
                        dict3[list3[0]] = 1

                # Printing items sold by each brand
                for item in dict3:
                    print("{:<45}".format("Number of Product(s) Sold By \'" + item + "\': ") + str(dict3[item]))
                print("\n")
            except:
                print("Not Found!")

        elif choice == 5:
            try:
                # Print All
                print(df)
                print("\n")
            except:
                print("Not Found!")

        elif choice == 0:
            print("Program Exited Successfully!")
            flag = False
        else:
            print("Wrong Input Please Try Again")
