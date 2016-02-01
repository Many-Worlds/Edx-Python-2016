def item_order(order):
    items=("salad", "hamburger", "water")
    counts = [order.count(item) for item in items]
    strings = ["{}:{}".format(item, count) for item, count in zip(items, counts)]
    return " ".join(strings)

order = "hamburger water hamburger"