def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [2]