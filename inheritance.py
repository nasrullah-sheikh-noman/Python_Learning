class Gadget:
  def __init__(self, brand, price, color):
    self.brand = brand
    self.price = price
    self.color = color

  def run(self):
    return f'Running'

class Laptop:
  def __init__(self, memory):
    self.memory = memory

  def coding(self):
    return f'Learing python in: {self.brand}'


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

class Carema:
  def __init__(self, pixel):
    self.pixel = pixel

  def change_lens(self):
    pass 


my_phn = Phone("Iphone", 180000, "Silver", "16GB")
print(my_phn)