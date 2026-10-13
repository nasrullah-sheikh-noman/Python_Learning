class shopping:
  def __init__(self, name):
    self.name = name
    self.cart = []
  def add_to_cart(self, item, price, quantity):
    product = {"item": item, "price": price, "quantity": quantity}
    self.cart.append(product)
  def checkout(self, amount):
    total = 0
    for item in self.cart:
      total += item["price"] * item["quantity"]
    print("Total price: ", total)
    if total > amount:
      print(f'Please provide {total-amount} more.')
    else:
      print(f'Here is your extra money: {amount-total}')

swapan = shopping("Alan swapan")
swapan.add_to_cart("Watch", 1200, 2)
swapan.add_to_cart("Camera", 8000, 1)

print(swapan.cart)
swapan.checkout(10400)