choice = int(input("Do you wanna count price or nutritients? 1/2: "))
program = True
while program == True:
    if choice == 1:
        package_price = float(input("\nEnter the price of the package in Kc: "))
        package_weight = float(input("Enter the weight of the package in grams: "))
        portion_weight = float(input("Enter the weight of your portion in grams: "))
        shipping = 0
        include = input("Do you wanna include shipping into the price? y/n: ")
        if include == "y":
            shipping = float(input("Enter the shipping price in Kc: "))
        portion_price = (package_price + shipping) / package_weight * portion_weight
        print("Your drink costs: ", portion_price)
        again = input("\nDo you wanna count the price again? y/n: ")
        if again == "y":
            choice = 1
        elif again == "n":
            count_nutri = input("Do you wanna count nutritients? y/n: ")
            if count_nutri == "y":
                choice = 2
            else:
                print("The program is over.")
                program = False
    if choice == 2:
        kcal_per_100g = float(input("\nEnter kcal for 100g of protein: "))
        protein_per_100g = float(input("Enter proteins for 100g: "))
        portion_weight = float(input("Enter the weight of your portion in grams: "))
        kcal_per_portion = kcal_per_100g / 100 * portion_weight
        protein_per_portion = protein_per_100g / 100 * portion_weight
        print("Your portion contains: \n", kcal_per_portion, " kcal \n", protein_per_portion, "g of proteins")
        again = input("\nDo you wanna count nutritients again? y/n: ")
        if again == "y":
            choice = 2
        elif again == "n":
            count_price = input("Do you wanna count a price? y/n: ")
            if count_price == "y":
                choice = 1
            else:
                print("The program is over.")
                program = False

