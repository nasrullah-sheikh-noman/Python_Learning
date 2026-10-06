balance = 8000

def buy_things(item, price):
  global balance
  print(f'balance {balance}')
  balance -= (item*price)
  print(f'balance {balance}')


buy_things(5, 500)
print(balance)