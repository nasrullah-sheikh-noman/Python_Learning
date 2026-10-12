class calculator:
  brand = "CASIO"
  def add(self, num1, num2):
    return num1 + num2
  def sub(self, num1, num2):
    return num1 - num2
  def mul(self, num1, nums2):
    return num1 * nums2
  def div(self, num1, num2):
    return num1/num2

cal = calculator()
print(cal.add(32, 45))
print(cal.sub(43, 12))
print(cal.mul(3, 5))
print(cal.div(88, 6))