import string
import secrets
print("You are here with Kadavusol creator^^")
print("Let's create yours")
length=int(input("Length:"))
s1=list(string.ascii_letters)
s2=list(string.digits)
s3=list(string.punctuation)
all=s1+s2+s3
password=[]
for i in range(length):
    randomchar=secrets.choice(all)
    password.append(randomchar)
print("password:","".join (password))
