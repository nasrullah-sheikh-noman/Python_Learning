class Gadget:
  def __init__(self, brand, price, color):
    self.brand = brand
    self.price = price
    self.color = color

  def run(self):
    return f'Running'

class Laptop(Gadget):
  def __init__(self, brand, price, color, memory):
    self.memory = memory
    super().__init__(brand, price, color)

  def coding(self):
    return f'Learing python in: {self.brand}'

  def __repr__(self) -> str:
    return f'Laptop: {self.brand}, Price: {self.price}, Color: {self.color}, Memory: {self.memory}GB'


class Phone(Gadget):
  def __init__(self, brand, price, color, ram):
    self.ram = ram
    super().__init__(brand, price, color)

  def run(self):
    return f'Running phone: {self.brand}'

  def sending_sms(self, number, sms):
    return f'Sending sms to: {number}, the message is {sms}'

  def __repr__(self) -> str:
    return f'Phone: {self.brand}, Price: {self.price}, Color: {self.color}, Ram: {self.ram}'

class Carema(Gadget):
  def __init__(self, brand, price, color, pixel):
    self.pixel = pixel
    super().__init__(brand, price, color)

  def change_lens(self):
    pass

  def __repr__(self) -> str:
    return f'Camera: {self.brand}, Price: {self.price}, Color: {self.color}, Pixel: {self.pixel}MP'


my_phn = Phone("Iphone", 180000, "Silver", "16GB")
print(my_phn)
my_cam = Carema("Canon", 40000, "Black", 500)
print(my_cam)
my_laptop = Laptop("Apple", 1000000, "Pink", 1024)
print(my_laptop)