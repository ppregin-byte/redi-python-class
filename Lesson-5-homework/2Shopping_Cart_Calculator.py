# Shopping Cart Calculator
# RECEIPT
# =======
# Laptop                           $899.99
# Mouse                            $25.50
# Keyboard                         $75.00
#                                --------
# Subtotal:                      $1000.49
# Discount (10% for $1000+):      -$100.05
# Tax (8.5%):                      $76.54
# Shipping:                        $9.99
#                                --------
# TOTAL:                          $986.97


def add_items():
    items = []
    while True:
        name = input("Enter item name (or 'checkout' to finish): ")
        if name.lower() == "checkout":
            return items 
        else:
            item = {"name": name, "price": 0.0}
            # Check if all inputs are valid numbers
            while True:
                price = input("Enter price: ")
                try:
                    item["price"] = float(price)
                    break
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
            items.append(item)  

# items [{"name": "Laptop", "price": 899.99}, {"name": "Keyboard", "price": 75.00}]
def calculating_subtotals(it):
    prices = []
    for item in it:
        price = item.get("price")
        prices.append(price)
    return sum(prices) 
# Apply discounts based on different rules
def applying_discounts(subtot):
    if subtot >= 2000:
        discount = subtot * 0.15
        disc_info = "15% for $2000+"
        return discount, disc_info 
    elif subtot >= 1000:
        discount = subtot * 0.1
        disc_info = "10% for $1000+"
        return discount, disc_info
    else:
        discount = 0
        disc_info = "No discount"
        return discount, disc_info
# Calculate tax   
def calculating_tax(subtot, discount):
    tax = (subtot - discount) * 0.085
    return tax

def calculating_shipping(subtotal, discount):
    if subtotal - discount > 0:
        shipping = 9.99
    else: 
        shipping = 0
    return shipping

def final_total(subtotal, discount, tax, shipping):
    total = subtotal - discount + tax + shipping 
    return total

# Display a formatted receipt
def printing_receipt_sections(items, subtotal, discount, discount_info, tax, shipping, total):
    print("\nRECEIPT")
    print("=======")
    for item in items:
        name = item["name"]
        price = item["price"]
        print(f"{name:<30}${price:>9.2f}")
    print(f"{'-'*8:>40}")
    print (f"{'Subtotal:':<30}${subtotal:>9.2f}")
    print (f"{f'Discount ({discount_info}):':<30}${discount:>9.2f}")
    print (f"{'Tax:':<30}${tax:>9.2f}")
    print (f"{'Shipping:':<30}${shipping:>9.2f}")
    print (f"{'-'*8:>40}")
    print (f"{'TOTAL:':<30}${total:>9.2f}")

def main():
    main_items = add_items()
    subtotals = calculating_subtotals(main_items)
    app_disc = applying_discounts(subtotals)
    tax = calculating_tax(subtotals, app_disc[0])
    shipping = calculating_shipping(subtotals, app_disc[0])
    total = final_total(subtotals, app_disc[0], tax, shipping)
    printing_receipt_sections(main_items, subtotals, app_disc[0], app_disc[1], tax, shipping, total)

main()