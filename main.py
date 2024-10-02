def averageGrade(value1, value2, value3, value4, value5):
    grade = (value1 + value2 + value3 + value4 + value5) / 5
    return grade

jermiahList = [47, 59, 93, 70, 89]
torranceList = [94, 72, 91, 67, 100]
maryList = [92, 44, 94, 83, 79]
bethList = [77, 32, 27, 100, 92]
johnList = [100, 100, 100, 99, 82]

student = input("Please enter the student's name: ")
if student == "Jeremiah":
    print(averageGrade(jermiahList[0], jermiahList[1], jermiahList[2], jermiahList[3], jermiahList[4]))
    if averageGrade(jermiahList[0], jermiahList[1], jermiahList[2], jermiahList[3], jermiahList[4]) < 60:
        print("Letter grade: F")
    elif averageGrade(jermiahList[0], jermiahList[1], jermiahList[2], jermiahList[3], jermiahList[4]) < 70:
        print("Letter grade: D")
    elif averageGrade(jermiahList[0], jermiahList[1], jermiahList[2], jermiahList[3], jermiahList[4]) < 80:
        print("Letter grade: C")
    elif averageGrade(jermiahList[0], jermiahList[1], jermiahList[2], jermiahList[3], jermiahList[4]) < 90:
        print("Letter grade: B")
    elif averageGrade(jermiahList[0], jermiahList[1], jermiahList[2], jermiahList[3], jermiahList[4]) < 100:
        print("Letter grade: A")

student2 = input("Please enter the student's name: ")
if student2 == "Torrance":
    print(averageGrade(torranceList[0], torranceList[1], torranceList[2], torranceList[3], torranceList[4]))
    if averageGrade(torranceList[0], torranceList[1], torranceList[2], torranceList[3], torranceList[4]) < 60:
        print("Letter grade: F")
    elif averageGrade(torranceList[0], torranceList[1], torranceList[2], torranceList[3], torranceList[4]) < 70:
        print("Letter grade: D")
    elif averageGrade(torranceList[0], torranceList[1], torranceList[2], torranceList[3], torranceList[4]) < 80:
        print("Letter grade: C")
    elif averageGrade(torranceList[0], torranceList[1], torranceList[2], torranceList[3], torranceList[4]) < 90:
        print("Letter grade: B")
    elif averageGrade(torranceList[0], torranceList[1], torranceList[2], torranceList[3], torranceList[4]) < 100:
        print("Letter grade: A")

student3 = input("Please enter the student's name: ")
if student3 == "Mary":
    print(averageGrade(maryList[0], maryList[1], maryList[2], maryList[3], maryList[4]))
    if averageGrade(maryList[0], maryList[1], maryList[2], maryList[3], maryList[4]) < 60:
        print("Letter grade: F")
    elif averageGrade(maryList[0], maryList[1], maryList[2], maryList[3], maryList[4]) < 70:
        print("Letter grade: D")
    elif averageGrade(maryList[0], maryList[1], maryList[2], maryList[3], maryList[4]) < 80:
        print("Letter grade: C")
    elif averageGrade(maryList[0], maryList[1], maryList[2], maryList[3], maryList[4]) < 90:
        print("Letter grade: B")
    elif averageGrade(maryList[0], maryList[1], maryList[2], maryList[3], maryList[4]) < 100:
        print("Letter grade: A")

student4 = input("Please enter the student's name: ")
if student4 == "Beth":
    print(averageGrade(bethList[0], bethList[1], bethList[2], bethList[3], bethList[4]))
    if averageGrade(bethList[0], bethList[1], bethList[2], bethList[3], bethList[4]) < 60:
        print("Letter grade: F")
    elif averageGrade(bethList[0], bethList[1], bethList[2], bethList[3], bethList[4]) < 70:
        print("Letter grade: D")
    elif averageGrade(bethList[0], bethList[1], bethList[2], bethList[3], bethList[4]) < 80:
        print("Letter grade: C")
    elif averageGrade(bethList[0], bethList[1], bethList[2], bethList[3], bethList[4]) < 90:
        print("Letter grade: B")
    elif averageGrade(bethList[0], bethList[1], bethList[2], bethList[3], bethList[4]) < 100:
        print("Letter grade: A")

student5 = input("Please enter the student's name: ")
if student5 == "John":
    print(averageGrade(johnList[0], johnList[1], johnList[2], johnList[3], johnList[4]))
    if averageGrade(johnList[0], johnList[1], johnList[2], johnList[3], johnList[4]) < 60:
        print("Letter grade: F")
    elif averageGrade(johnList[0], johnList[1], johnList[2], johnList[3], johnList[4]) < 70:
        print("Letter grade: D")
    elif averageGrade(johnList[0], johnList[1], johnList[2], johnList[3], johnList[4]) < 80:
        print("Letter grade: C")
    elif averageGrade(johnList[0], johnList[1], johnList[2], johnList[3], johnList[4]) < 90:
        print("Letter grade: B")
    elif averageGrade(johnList[0], johnList[1], johnList[2], johnList[3], johnList[4]) < 100:
        print("Letter grade: A")








