print("Hey, come on...Let's get started with Kanidham:)")
expr=input("ENTER the expression to be calculated:")
n=0
x=0
n2=0
op="+"
for char in expr + "+":
    if char.isdigit():
        n=n*10+int(char)

    elif char in "+-*/":
        if op=="+":
            x+=n2
            n2=n
        elif op=="-":
            x+=n2
            n2=-n
        elif op=="*":
            n2=n2*n
        elif op=="/":
            n2=n2/n
        elif op=="^":
            n2=n2**n
        elif op=="%":
            n2=n2/n

        op=char
        n=0
x+=n2
print("Here's your ANSWER:",x)