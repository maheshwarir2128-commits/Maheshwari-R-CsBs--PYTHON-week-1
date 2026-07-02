import random
n1 = random.randint(1, 10)
print("Come on, let's play a game^^")
n2=int(input("Guess a number(1-10):"))
if n2==n1:
    print("CONGRATULATION YOU GOT IT!")
else:
    print("OOPS!you missed it")