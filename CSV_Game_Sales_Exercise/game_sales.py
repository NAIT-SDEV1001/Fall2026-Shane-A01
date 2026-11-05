import csv
from pathlib import Path
from pprint import pprint

def read_sales(file_path):
    sales = []
    try:
        with open(file_path, 'r', encoding = 'utf-8') as file:
            reader = csv.DictReader(file)
            for sale in reader:
                sales.append(sale)
    except FileNotFoundError:
        print(f'Error: The file {file_path} does not exist')
        return None
    return sales


# •	Create a new list for qualifying games.
# •	For each sale, convert Price to a float and Quantity to an int, then calculate revenue as price multiplied by quantity.
# •	Include games with revenue greater than or equal to $100. Compare the numeric revenue before formatting it.
# •	For each qualifying game, append a dictionary containing Game, Category, and Revenue to the new list. Format Revenue to two decimal places.
# •	Return the new list. Preserve the order of games from the input file.

def get_popular_games(sales):
    popular_games=[]
    for sale in sales:
        revenue = float(sale['Price']) * int(sale['Quantity'])
        if revenue >= 100:
            popular_games.append({
                'Game':sale['Game'],
                'Category':sale['Category'],
                'Revenue':f"{revenue:.2f}"
            })
    return popular_games

file_path = Path(__file__).parent/'data'/'game_sales.csv'
pprint (read_sales(file_path))

print('Popular games')
pprint(get_popular_games(read_sales(file_path)))


