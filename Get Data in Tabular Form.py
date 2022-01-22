# Required Module:- pip install tabulate

from tabulate import tabulate

# input the data
data = [["Arun", 18, 95],
        ["Rahul", 19, 88],
        ["Shiva", 21, 90]]

# arrange the data in table form
table = tabulate(data, headers=["Name", "Age", "Percent"])

# print the data in Tabular form
print(table)