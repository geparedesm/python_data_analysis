# DONE: Display the data in a table(or table-like)format.
# DONE: Calculate the average rating for each menu item.
# DONE: Calculate the total sales for each day of the week.
# TODO: Determine the most popular menu item based on customer ratings
# TODO: Show details of customers_rating

import csv
from tabulate import tabulate
import itertools


def get_data():
    """
    Reads the menu.csv file and returns its content as a list of lists.

    Returns:
        list: A list of lists, where each sublist represents a row in the CSV file.
    """
    with open('menu.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        return data


def show_data(data):
    """
    Prints the menu data in a table format, with the following calculations:
        - row numbers
        - average customer rating for each menu item
        - total of customer ratings for each menu item

    Args:
        data (list): A list of lists, where each sublist represents a row in the CSV file.
    """
    headers = data[0]
    # Insert row numbers
    rows = data[1:]
    for i, row in enumerate(rows, start=1):
        row.insert(0, i)
    # Calculate how many customers rated each menu item

    for row in data[1:]:

        customer_rating = row[6]
        rating_length = len(eval(customer_rating))

        # Calculate average rating
        avg_rating = 0
        for row_rating in eval(customer_rating):
            avg_rating += row_rating["rating"]
        if rating_length > 0:
            avg_rating = avg_rating / len(eval(customer_rating))
        else:
            avg_rating = 0

        row[4] = avg_rating
        # Calculate total of customer ratings

        row[6] = rating_length
    data = [headers] + rows
    print(tabulate(data, headers='firstrow', tablefmt='grid'))


def cal_sales_day(data):

    # Sort data by date
    data.sort(key=lambda x: x[6])

    # Group data by date
    grouped_data = itertools.groupby(data, key=lambda x: x[6])
    table = [['Dates', 'Sales']]
    # Print grouped data
    for date, group in grouped_data:
        sales_per_day = 0
        for item in group:

            try:
                sales_per_day = sales_per_day + float(item[1])
            except ValueError:
                pass
        table.append([date, f'{round(sales_per_day,2)} AUD']
                     ) if date != "date" else None
    print(tabulate(table, headers='firstrow', tablefmt='grid'))


user_input = input("""
Please select an option: \n
1) Display data
2) Calculate the total sales for each day of the week
                   """)
data = get_data()
if user_input == "1":
    show_data(data)
elif user_input == "2":
    cal_sales_day(data)
else:
    print()
