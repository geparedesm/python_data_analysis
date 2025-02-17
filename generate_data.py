# DONE: add ratings
# DONE: add number of items sales per week
# DONE: add customer ratings for each item
# DONE: add date

# Import the required module
import csv
from faker import Faker


def fake_food():
    """
    Returns a random food option from the menu with its price and category.

    Returns:
        list: A list containing the name of the food, its price and category.
    """
    foods = [
        ['Chicken Parmigiana', 19.99, 'Main'],
        ['Fish and Chips', 18.99, 'Main'],
        ['Margherita Pizza', 15.99, 'Main'],
        ['Caesar Salad', 9.99, 'Starter'],
        ['Garlic Bread', 6.99, 'Starter'],
        ['Tiramisu', 7.99, 'Dessert'],
        ['Cheesecake', 6.99, 'Dessert']]
    index = fake.random_int(min=0, max=len(foods)-1)
    return foods[index]


def fake_customer_rating(max):
    """
    Generate a list of customer ratings with names and ratings.

    Args:
        max (int): The maximum number of customer ratings to generate.

    Returns:
        list: A list of customer ratings. Each customer rating is a dictionary 
              with keys "name" and "rating".
    """
    customers_rating = []
    for i in range(max):
        customers_rating.append(
            {"name": fake.name(), "rating": fake.random_int(min=1, max=5)})
    return customers_rating


fake = Faker()
# Define the field names
fields = ['item',
          'price',
          'category',
          'rating',
          'sales_week',
          'customer_rating',
          'date'
          ]

# Define the data rows
rows = []
for i in range(25):
    food = fake_food()
    rows.append([food[0],
                 food[1],
                 food[2],
                 0,
                 fake.random_int(min=0, max=100),
                 fake_customer_rating(fake.random_int(min=2, max=10)),
                 fake.date()
                 ])
# Create a CSV file and write the data rows
with open('menu.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fields)
    writer.writerows(rows)
