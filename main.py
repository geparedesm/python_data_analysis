# DONE: Display the data in a table(or table-like)format.
# DONE: Calculate the average rating for each menu item.
# DONE: Calculate the total sales for each day of the week.
# DONE: Determine the most popular menu item based on customer ratings
# DONE: Show details of customers_rating

import csv
from tabulate import tabulate
import itertools


def get_data():
    """
    Reads the menu.csv file and returns the data in a list of lists format.

    The data is modified to include a row number, the average rating and the total number of customer ratings.

    Returns:
        list: A list of lists where each inner list represents a row in the menu.csv file.
    """
    with open('menu.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
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

        row[4] = round(avg_rating, 2)
        # Calculate total of customer ratings
        data = [headers] + rows

    return data


def show_data(data):
    """
    Displays the data in a tabular format with the total number of customer ratings.

    Args:
        data (list): A list of lists containing menu data. The first element is the header, 
                     and subsequent elements are rows containing menu item information.

    Modifies:
        Replaces the 'customer_rating' column with the count of customer ratings 
        and updates the header to 'total_customer_ratings'.

    Prints:
        The formatted table with updated customer ratings count.
    """

    headers = data[0]
    rows = data[1:]

    for row in data[1:]:
        customer_rating = row[6]
        rating_length = len(eval(customer_rating))
        row[6] = rating_length
    headers[5] = "total_customer_ratings"
    data = [headers] + rows
    print(tabulate(data, headers='firstrow', tablefmt='grid'))


def cal_sales_day(data):
    """
    Calculate the total sales for each day of the week and display the data in a table format.

    Args:
        data (list): A list of lists containing menu data. The first element is the header, 
                     and subsequent elements are rows containing menu item information.

    Modifies:
        None

    Prints:
        The formatted table with the total sales for each day of the week.
    """
    data = data[1:]
    # Sort data by date
    data.sort(key=lambda x: x[7])

    # Group data by date
    grouped_data = itertools.groupby(data, key=lambda x: x[7])
    table = [['Dates', 'Sales']]
    # Print grouped data
    for date, group in grouped_data:
        sales_per_day = 0
        for item in group:

            try:
                sales_per_day = sales_per_day + float(item[2])
            except ValueError:
                pass
        table.append([date, f'{round(sales_per_day,2)} AUD']
                     )
    print(tabulate(table, headers='firstrow', tablefmt='grid'))


def get_most_popular_item(data):
    """
    Finds the most popular item in the menu based on customer ratings and displays its name and rating.

    Args:
        data (list): A list of lists containing menu data. The first element is the header, 
                     and subsequent elements are rows containing menu item information.

    Modifies:
        None

    Prints:
        The formatted table with the name and rating of the most popular item.
    """
    data = data[1:]
    most_popular_item = max(data, key=lambda x: x[4])
    table = [['Name', 'Rating']]
    table.append([most_popular_item[0], most_popular_item[4]])
    print(tabulate(table, headers='firstrow', tablefmt='grid'))


def get_customers_ratings(data):
    """
    Displays the customer ratings for a given menu item based on user input.

    Args:
        data (list): A list of lists containing menu data. The first element is the header, 
                     and subsequent elements are rows containing menu item information.

    Modifies:
        None

    Prints:
        The formatted table with the customer name and rating for the given item.
    """
    try:
        show_data(data)
        data = get_data()
        data = data[1:]
        id_item = input("Enter the id of the item: ")
        id_item = int(id_item) - 1
        header = ['customer_name', 'rating']
        rows = []
        # convert string to object

        for item in eval(data[int(id_item)][6]):

            rows.append([item['name'], item['rating']])
        print(tabulate(rows, headers=header, tablefmt='grid'))
    except:
        print("Invalid input")


if __name__ == '__main__':
    user_input = ''
    while user_input != '0':
        user_input = input("""
Please select an option: \n
1) Display data
2) Calculate the total sales for each day of the week
3) Most popular menu item based on customer ratings
4) Show details of customers rating
0) Exit\n
Select an option: """)
        data = get_data()
        if user_input == "1":
            show_data(data)
        elif user_input == "2":
            cal_sales_day(data)
        elif user_input == "3":
            get_most_popular_item(data)
        elif user_input == "4":
            get_customers_ratings(data)
        else:
            print("Option not available")
        input("Press enter to continue")
