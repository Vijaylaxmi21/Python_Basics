
item = input("Enter item name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount percentage: "))

subtotal = price * quantity
discount_amount = subtotal * discount / 100
final_bill = subtotal - discount_amount

print("Item:", item)
print("Subtotal:", round(subtotal, 2))
print("Discount:", round(discount_amount, 2))
print("Final Bill:", round(final_bill, 2))
  
