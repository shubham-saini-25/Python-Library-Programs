# FOOD ORDERING SYSTEM USING PYTHON
# Made by:- @python_with_shubham

def food_ordering_system():
    print("\n================ FOOD ORDERING SYSTEM ================\n")
    
    # take customer details by user
    def customer_details():
        global Name, Address, Phone, Email
        Name = input("Enter Your Name: ")
        Address = input("Enter Your Address: ")
        Phone = input("Enter Your Phone Number: ")
        Email = input("Enter Your Email: ")
        print("\n---Your Menu of Foods and Drinks---")
        if Name=="" or Address=="" or Phone=="" or Email=="":
            print("Please Enter All Customer details.")
            customer_details()
    customer_details()

    # read and display the menu contents
    def read_menuFile():
        with open('D:/PYTHON MODULES/Food Ordering System without GUI/Foods and Drinks Menu List.txt') as f:
            contents = f.read()
            print(contents)
    read_menuFile()

    # save customer details in text file
    def save_customerData():
        file1 = open("D:/PYTHON MODULES/Food Ordering System without GUI/Order.txt", "w")
        file1.write("  Name      :   " + Name)
        file1.write("\n Address    :   " + Address)
        file1.write("\n  Phone     :   " + Phone)
        file1.write("\n  Email     :   " + Email)
        file1.close()
    save_customerData()

    # place order by user
    def order_placing():
        print("\n----------Place Your Order-----------")
        def foods():
            global food, item_name1, item_price1
            food = input("Select a item from Foods: ")
            if len(food) == 1:
        
                if food == "1":
                    item_name1 = "French Fries"
                    item_price1 = 50.00 
                    file1 = open("D:/PYTHON MODULES/Food Ordering System without GUI/Order.txt", "a")
                    file1.write("\nFood Item   :  " + f"{item_name1}")
                    file1.write("\nFood Price  :  " + f"Rs{item_price1}")
                    file1.close()

                elif food == "2":
                    item_name1 = "Cheese Burger"
                    item_price1 = 100.00 
                    file1 = open("D:/PYTHON MODULES/Food Ordering System without GUI/Order.txt", "a")
                    file1.write("\nFood Item   :  " + f"{item_name1}")
                    file1.write("\nFood Price  :  " + f"Rs{item_price1}")
                    file1.close()

                elif food == "3":
                    item_name1 = "Burger"
                    item_price1 = 80.00 
                    file1 = open("D:/PYTHON MODULES/Food Ordering System without GUI/Order.txt", "a")
                    file1.write("\nFood Item   :  " + f"{item_name1}")
                    file1.write("\nFood Price  :  " + f"Rs{item_price1}")
                    file1.close()

                elif food == "4":
                    item_name1 = "Pizza"
                    item_price1 = 150.00 
                    file1 = open("D:/PYTHON MODULES/Food Ordering System without GUI/Order.txt", "a")
                    file1.write("\nFood Item   :  " + f"{item_name1}")
                    file1.write("\nFood Price  :  " + f"Rs{item_price1}")
                    file1.close()
            else:
                print("Your Order not Found in Foods. Please Enter Your Order Again.\n")
                foods()
        foods()

        def drinks():
            global drink, item_name2, item_price2
            drink = input("Select a item from Drinks: ")
            if len(drink) == 1:

                if drink == "1":
                    item_name2 = "Thums Up"
                    item_price2 = 30.00
                    file1 = open("D:/PYTHON MODULES/Food Ordering System without GUI/Order.txt", "a")
                    file1.write("\nDrinks Item   :  " + f"{item_name2}")
                    file1.write("\nDrinks Price  :  " + f"Rs{item_price2}")
                    file1.close()

                elif drink == "2":
                    item_name2 = "Pepsi"
                    item_price2 = 30.00
                    file1 = open("D:/PYTHON MODULES/Food Ordering System without GUI/Order.txt", "a")
                    file1.write("\nDrinks Item   :  " + f"{item_name2}")
                    file1.write("\nDrinks Price  :  " + f"Rs{item_price2}")
                    file1.close()

                elif drink == "3":
                    item_name2 = "Mazza"
                    item_price2 = 35.00
                    file1 = open("D:/PYTHON MODULES/Food Ordering System without GUI/Order.txt", "a")
                    file1.write("\nDrinks Item   :  " + f"{item_name2}")
                    file1.write("\nDrinks Price  :  " + f"Rs{item_price2}")
                    file1.close()

                elif drink == "4":
                    item_name2 = "Fanta"
                    item_price2 = 20.00
                    file1 = open("D:/PYTHON MODULES/Food Ordering System without GUI/Order.txt", "a")
                    file1.write("\nDrinks Item   :  " + f"{item_name2}")
                    file1.write("\nDrinks Price  :  " + f"Rs{item_price2}")
                    file1.close()
            else:
                print("Your Order not Found in Drinks. Please Enter Your Order Again.\n")
                drinks()
        drinks()
    order_placing()
                
    # read Order.txt file and calculate the total payment
    def payment():
        global item_name1, item_name2, item_price1, item_price2
        with open('D:/PYTHON MODULES/Food Ordering System without GUI/Order.txt') as f:
            Customer_data = f.read()
            
            print("\n-------Customer & Order Details------")
            print(Customer_data)
            print("\n-----------Payment Receipt-----------")
        
            print(f"Price of {item_name1} = Rs{item_price1}")
            print(f"Price of {item_name2} = Rs{item_price2}")

            delivery_charges =  50.00
            print(f"Delivery Charges = Rs{delivery_charges}")

            total_price = item_price1 + item_price2 + delivery_charges
            print(f"Total Payable Amount = Rs{total_price}")

            print("-------------------------------------\n")
    payment()

food_ordering_system() # called the food_ordering_system function