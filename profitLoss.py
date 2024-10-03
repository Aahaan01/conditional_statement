purchased_price=float(input("purchased price: "))
selling_price=float(input("sold price: "))
if selling_price>purchased_price:
    profit=selling_price-purchased_price
    print("profit is: ", profit)
else:
    print("loss")