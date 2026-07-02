print("come on...Let's see how old are you!")
d, m, y=input("Enter your birth(separated by space)date: month: year:").split()
d2, m2, y2=input("Enter the current date: month: year:").split()

d, m, y=int(d), int(m),int(y)
d2, m2, y2=int(d2), int(m2), int(y2)
if d>=d2:
    m2=m2-1
    if m2==0:
        m2=12
        y2=y2-1
if m2 in[1,3,5,7,8,10,12]:
    d2=d2+31
elif m2 in[2,4,6,7,9,11]:
    d2=d2+30
else:
    if y2%400==0 or (y2%4==0 and y2%100!=0 ):
        d2=d2+29
    else:
        d2=d2+28
if m2<m:
    y2=y2-1
    m2=m2+12

day=d2-d
mon=m2-m
year=y2-y
print("You are",year,"years",mon,"months and",day,"days old")