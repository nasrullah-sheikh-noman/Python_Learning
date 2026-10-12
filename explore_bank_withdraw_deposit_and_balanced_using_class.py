class bank:
  def __init__(self, balance):
    self.balance = balance
    self.min_withdraw = 100
    self.max_withdraw = 100000

  def get_balance(self):
    return self.balance
  
  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f'Here is your money {self.balance}')

  def withdraw(self, amount):
    if amount > self.balance:
      print(f'You don\'t have that much money in your account, dear.')
    elif amount < self.min_withdraw:
      print(f'You won\'t be able to withdraw any less than {self.min_withdraw} money. my dear.')
    elif amount > self.max_withdraw:
      print(f'You won\'t be able to that {self.max_withdraw} much money, dear.')
    else:
      self.balance -= amount
      print(f'Your balance after withdraw {self.balance}')

brac = bank(40000)
print(brac.get_balance())
brac.deposit(-2000)
brac.withdraw(3000)
brac.withdraw(992333333333)

dbbl = bank(120000)
print(dbbl.get_balance())
dbbl.deposit(30000)
dbbl.withdraw(20000)
dbbl.withdraw(34234324444444)
dbbl.withdraw(30)