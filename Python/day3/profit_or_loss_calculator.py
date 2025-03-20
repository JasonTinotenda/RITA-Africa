buying_price = float(input("Enter the buying price: "))
selling_price = float(input("Enter the selling price: "))
price_difference = (selling_price-buying_price)
if price_difference > 0:
    print(
        f"Profit: ${price_difference}"
        )
else:
    print(
        f"Loss: ${abs(price_difference)}"
        )
