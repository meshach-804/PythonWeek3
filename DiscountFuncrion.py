def calculate_discount(price, discount_percent):
  if (discount_percent > 20):
    price = price - (price * discount_percent / 100)
  else:
    price = price
  return price

price = int(input("Enter the price: "))
discount_percent = int(input("Enter the discount percent: "))
print(calculate_discount(price, discount_percent))