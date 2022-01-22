from prettytable import PrettyTable

# Specify the Column Names while initializing the Table
myTable1 = PrettyTable(["No.", "Food", "Price"])

# Add rows
myTable1.add_row(["1.", "French Fries", "₹50.00"])
myTable1.add_row(["2.", "Cheese Burger", "₹100.00"])
myTable1.add_row(["3.", "Burger", "₹80.00"])
myTable1.add_row(["4.", "Pizza", "₹150.00"])
myTable1.add_row(["-----", "---------------", "---------"])
myTable1.add_row(["No.", "Drinks", "Price"])
myTable1.add_row(["-----", "---------------", "---------"])
myTable1.add_row(["1.", "Thums Up", "₹30.00"])
myTable1.add_row(["2.", "Pepsi", "₹30.00"])
myTable1.add_row(["3.", "Mazza", "₹35.00"])
myTable1.add_row(["4.", "Fanta", "₹20.00"])

print(myTable1)