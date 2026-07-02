print(">>>Stdent Class<<<")
class Stud:
 def __init__(self, name, dept,cgpa):
    self.name = name
    self.dept=dept
    self.cgpa=cgpa
stud1=Stud ("Chandha.R,","CsBs,","9.76")
stud2=Stud ("Chozhan.D,","IT,","9.83")
print("Student1:",stud1.name,"Department:",stud1.dept,"CGPA:",stud1.cgpa,)
print("Student2:",stud2.name,"Department:",stud2.dept,"CGPA:",stud2.cgpa,)
print("---END---")