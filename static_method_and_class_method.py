class Shopping:
  items  = []  #  Static attribute
  origin = "China"
  def __init__(self, name, location):  # Instance method
    self.name = name  # Instance attribute
    self.location = location

  @classmethod
  def hudai_dekhi(self, item):  # Class method
    return f'Hudai dekhi kintu kinmu na....... item {item}'

  @staticmethod
  def multiply(a, b):  # Static method
    return a * b 

basu = Shopping("Basundhara", "Dhaka")
print(Shopping.hudai_dekhi("Shirt"))
print(Shopping.multiply(4, 5))  # Static method
print(basu.multiply(9,2))