# TODO: add ratings
# TODO: add number of items sales per week,
# TODO: add customer ratings for each item,

# Import the required module
import csv
# Define the field names
fields = ['item', 'price', 'category',
          'rating', 'sales_week', 'customer_rating']
# Define the data rows
rows = [
    ['Chicken Parmigiana', 19.99, 'Main', '5',
        '20', [{"name": "example", "rating": "5"}]],
    ['Fish and Chips', 18.99, 'Main', '5', '20',
        [{"name": "example", "rating": "5"}]],
    ['Margherita Pizza', 15.99, 'Main', '5', '20',
        [{"name": "example", "rating": "5"}]],
    ['Caesar Salad', 9.99, 'Starter', '5', '20',
        [{"name": "example", "rating": "5"}]],
    ['Garlic Bread', 6.99, 'Starter', '5', '20',
        [{"name": "example", "rating": "5"}]],
    ['Tiramisu', 7.99, 'Dessert', '5', '20', [
        {"name": "example", "rating": "5"}]],
    ['Cheesecake', 6.99, 'Dessert', '5', '20',
        [{"name": "example", "rating": "5"}]],
]
# Create a CSV file and write the data rows
with open('menu.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fields)
    writer.writerows(rows)
