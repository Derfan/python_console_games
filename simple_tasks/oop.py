from colorama import init, Fore

init()

class Account:
    def __init__(self, owner, balance):
      self.owner = owner
      self.balance = balance

    def __str__(self):
      return f'{Fore.GREEN}Account owner: {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, amount):
      print('Deposit Accepted')
      self.balance += amount

    def withdraw(self, amount):
      if self.balance - amount < 0:
        print('Funds Unavailable!')
      else:
        print('Withdrawal Accepted')
        self.balance -= amount

account = Account('Borys', 500)

print(account)
