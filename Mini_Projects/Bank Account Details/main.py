print(">>>Bank Account Details<<<")
class Account:
 def __init__(self, name, acc_no, balance):
    self.name = name
    self.acc_no=acc_no
    self.__balance=balance
def get_balance(self):
         return self.__balance
def deposit(self, amount):
         self.__balance += amount
acc1 = Account ("Agathiyar","12345","1000000")
acc2 = Account ("Lavan","67890","50000")

print("Manager:",acc1.name,"A/c.no:",acc1.acc_no,)
print("Employee:",acc2.name,"A/c.no:",acc2.acc_no)
print("Can't show account balance, it's in private.")
print("Manager balance:",acc1.get_balance())
print("Employee balance:",acc2.get_balance())