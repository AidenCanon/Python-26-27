""" 
Goal is to create a bug and fix it by tracing it.
"""
Amazon_Cart = [
    {"item": "Laptop", "price": 999.99, "quantity": 1},
    {"item": "Mouse", "price": 49.99, "quantity": 2},
    {"item": "Keyboard", "price": 79.99, "quantity": 1}
]

def calculate_total_with_tax(items, discount, tax_rate):
    subtotal = 0

    for item in items:
        line_total = item["price"] * item["quantity"]
        subtotal += line_total
        #Debugging check 1:
        # print("Line total for", item["item"], "is", line_total)

    discounted_subtotal = subtotal - discount
    # tax = discounted_subtotal + tax_rate
    # total = discounted_subtotal - tax
    tax = discounted_subtotal * tax_rate
    total = discounted_subtotal + tax
    #Debugging check 2:
    # print("Subtotal after discount is", discounted_subtotal)
    # print("Tax is", tax)
    # print("Total is", total)
    return total


print("Total price of items in Amazon Cart with tax:", calculate_total_with_tax(Amazon_Cart, discount=50, tax_rate=0.07))

print("Expected total price of items in Amazon Cart with tax:", 1209.0572)
