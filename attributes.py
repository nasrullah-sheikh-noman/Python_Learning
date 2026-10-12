class shop:
  cart = []  # cart is a class attribute

  def __init__(self, buyer):
    self.buyer = buyer

  def add_to_cart(self, item):
    self.cart.append(item)

mehu = shop("mehjabin")
mehu.add_to_cart("shoes")
mehu.add_to_cart("Iphone")

print(mehu.cart)

sakib = shop("Sakib khan")
sakib.add_to_cart("Baggy Pant")
sakib.add_to_cart("Sunglass")

print(sakib.cart)
