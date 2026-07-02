print("HELLO you there!check this out!!!")
values=input("Enter numbers(separated by space):")
_list=[float(n) for n in values.split()]

evens=[]
odds=[]
neither=[]
for n in _list:
    if n%2.0==0.0:
        evens.append(n)
    elif n%2.0==1.0:
        odds.append(n)
    else:
        neither.append(n)
print("EVEN:",",".join(map(str,evens)))
print("ODD:",",".join(map(str,odds)))
print("NEITHER:",",".join(map(str,neither)))


