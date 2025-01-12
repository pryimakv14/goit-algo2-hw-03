import csv
from BTrees.OOBTree import OOBTree
from timeit import timeit

def load_data(file_path):
    items = []
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            item = {
                "ID": int(row["ID"]),
                "Name": row["Name"],
                "Category": row["Category"],
                "Price": float(row["Price"]),
            }
            items.append(item)
    return items

def add_item(str, item):
    str[item["ID"]] = item

def range_query_tree(tree, min_price, max_price):
    return [value for _, value in tree.items(min_price, max_price)]

def range_query_dict(dictionary, min_price, max_price):
    return [item for item in dictionary.values() if min_price <= item["Price"] <= max_price]

def main():
    file_path = "generated_items_data.csv"
    items = load_data(file_path)

    tree = OOBTree()
    dictionary = {}

    for item in items:
        add_item(tree, item)
        add_item(dictionary, item)

    min_price = 10.0
    max_price = 50.0

    tree_time = timeit(lambda: range_query_tree(tree, min_price, max_price), number=100)
    dict_time = timeit(lambda: range_query_dict(dictionary, min_price, max_price), number=100)

    print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")

if __name__ == "__main__":
    main()

