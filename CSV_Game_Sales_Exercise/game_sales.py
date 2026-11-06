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

def write_report(file_path, games):
    # Explicit names allow a header-only report when games is empty.
    fieldnames = ['Game', 'Category', 'Revenue']
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for game in games:
            writer.writerow(game)

def main():
    file_path = Path(__file__).parent/'data'/'game_sales.csv'
    output_path = Path(__file__).parent/'data'/'popular_games.csv'
    sales = read_sales(file_path)
    # None means missing file; [] means a successfully read empty file.
    if sales is None:
        return
    games = get_popular_games(sales)
    write_report(output_path, games)
    print(f"Sales records read: {len(sales)}")
    if games:
        print("\nGames earning at least $100:")
        for game in games:
            print(f"{game['Game']}: ${game['Revenue']}")
    else:
        print("\nNo games earned at least $100.")
    print(f"\nReport saved to {output_path.name}")


if __name__ == '__main__':
    main()


