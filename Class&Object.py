class Student:
    roll=""
    gpa=""

rahim=Student()
print(isinstance(rahim,Student))#check is rahim object of Student class
rahim.roll=101
rahim.gpa=3.70
print(f"Roll : {rahim.roll},GPA : {rahim.gpa}")

karim=Student()
karim.roll=102
karim.gpa=3.40
print(f"Roll : {karim.roll},GPA : {karim.gpa}")