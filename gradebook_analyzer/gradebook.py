print ("Welcome")
print("------------------------------------------")

num=int(input("Enter the number of students : "))
stu=[]
marks=[]
for i in range (num):
    Name=str(input("Enter the student name : "))
    Marks=int(input("Enter the marks obtained : "))
    stu.append(Name)
    marks.append(Marks)


result = {key: value for key, value in zip(stu, marks)}

def calculate_average():#calculating average 
    s=0
    n=len(marks)
    for i in marks:
        s=s+i
    
    av = s / n
    print(f"The average is {av}")

calculate_average()

def calculate_median():#calculating median
    marks.sort()
    n = len(marks)
    if n % 2 == 0: # Even-length list
        median = (marks[n//2 - 1] + marks[n//2]) / 2
    else: # Odd-length list
        median = marks[n//2]
    print(f"The median is {median}")

calculate_median()

def find_max_score():#finding max score
    max_score = max(marks)
    print(f"The maximum score is {max_score}")

find_max_score()

def find_min_score():#finding min score
    min_score = min(marks)
    print(f"The minimum score is {min_score}")

find_min_score()

grade=[]
for j in marks:#giving grades based on marks
    if j >= 90 and j <=100:
        print("Your garde is A")
        grade.append("A")
    elif j>=80 and j<=89 :
        print("your garde is B")
        grade.append("B")
    elif j>=70 and j<=79 :
        print("your garde is C")
        grade.append("C")
    elif j>=60 and j<=69 :
        print("your garde is D")
        grade.append("D")
    elif j <60 :
        print("your garde is E")
        grade.append("E")
'''
passed_students =[x for x , grade in grade.items() if grade!="E"]
failed_students =[x for x , grade in grade.items() if grade=="E"]'''

passed_students = [s for s, g in zip(stu, grade) if g != "E"]
failed_students = [s for s, g in zip(stu, grade) if g == "E"]

print(passed_students)

n=len(stu)#printing the detailed answer
print(f"name\t\tmarks\t\tgrade")
for b in range(n):
    print(f"{stu[b]}\t\t{marks[b]}\t\t{grade[b]}")
