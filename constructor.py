# constructor = __init__
class Phone:
  manufactured = "China"

  def __init__(self, owner, brand, price):
    self.owner = owner
    self.brand = brand
    self.price = price

  def send_sms(self, phone, sms):
    return f'sending to: {phone} message: {sms}'

phn = Phone("John wick", "Oppo", 32000)
print(phn.owner, phn.brand, phn.price)

her_phn = Phone("Miss: Jorina", "Iphone", 200000)
print(her_phn.owner, her_phn.brand, her_phn.price)

print(phn.send_sms())
print(her_phn.send_sms())