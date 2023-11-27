#Shipping Charge Calculation
weight = float(input("Enter the weight of the package: "))

if weight <= 2:
    shipping_charge = 1.10
elif weight <= 6:
    shipping_charge = 2.20
elif weight <= 10:
    shipping_charge = 3.70
else:
    shipping_charge = 3.80

print(f"Shipping charge: ${shipping_charge:.2f}")

#Currency Conversion
exchange_rate = float(input("Enter the exchange rate from U.S. dollars to Canadian dollars: "))
conversion_type = int(input("Enter 0 to convert U.S. dollars to Canadian dollars and 1 vice versa: "))

if conversion_type != 0 and conversion_type != 1:
    print("Invalid Conversion Type")
else:
    amount = float(input("Enter the amount: "))

    if conversion_type == 0:
        converted_amount = amount * exchange_rate
        print(f"{amount:.2f} U.S dollars is {converted_amount:.2f} Canadian dollars")
    else:
        converted_amount = amount / exchange_rate
        print(f"{amount:.2f} Canadian dollars is {converted_amount:.2f} U.S. dollars")