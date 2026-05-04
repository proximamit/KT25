def order(item, quantity, *args, discount=0, **kwargs):
    print(item, quantity)
    print("Extras:", args)
    print("Discount:", discount)
    print("Metadata:", kwargs)

order("Laptop", 1, "bag", "mouse", discount=10, delivery="fast")
