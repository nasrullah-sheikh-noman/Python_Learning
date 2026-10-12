class shop:
  shopping_mall = "Basundhara Shopping Mall"

  def __init__(self, buyer):
    self.buyer = buyer
    self.cart = []  # cart is an instance attribute
  def add_to_cart(self, item):
    self.cart.append(item)

puja = shop("Puja Cherry")
puja.add_to_cart("Tops")
puja.add_to_cart("Shoes")

print(puja.cart)

siam = shop("Siam Ahmed")
siam.add_to_cart("Panjabi")
siam.add_to_cart("T-shirt")

print(siam.cart)

