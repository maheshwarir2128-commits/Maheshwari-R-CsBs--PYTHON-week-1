print(">>>Student's Marks Manager<<<")
stud=[{'name':'Mozhi', 'dept':'CsBs'}, {'name':'Yazh', 'dept':'Cse'}]
stud1_marks={'sci':83,'Mat':92,'Eng':90}
stud2_marks={'sci' :75,'Mat':99,'Eng':89}
t1=sum(stud1_marks.values())
t2=sum(stud2_marks.values())
avg1=t1/3
avg2=t2/3
per1=(t1/300)*100
per2=(t2/300)*100
grp={}
for student in stud:
    dept = student['dept']
    grp.setdefault(dept,[]).append(student['name'])
print(grp)
print(f"Mozhi's total:{t1},Average:{avg1:.2f},Percentage:{per1:.2f}")
print("Yazh's total:",t2,"Average:",round(avg2,2),"Percentage:",round(per2,2),)