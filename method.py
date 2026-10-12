class phone:
  brand = "Samsung"
  color = "Blue"
  price = 120000
  features = ["camera", "speaker"]

  def call(self):
    print("calling one person")

  def send_sms(self, phone, sms):
    text = f'sending sms to {phone} and message: {sms}'
    return text

my_phn = phone()
print(my_phn)
my_phn.call()
res = my_phn.send_sms("Apple", "Hi apple user's")
print(res)