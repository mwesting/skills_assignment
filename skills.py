
# MITCH WESTING
# BASIC PYTHON SKILLS PROGRAM
# THIS PROGRAM SHOWS DATA FOR A DICTIONARY OF STUDENTS AND THEIR GRADES
namesList = []
gradesList=[]
studentDict = {}
# START OF MAIN
def main():
   
    displayMenu()
    #[1] ADD STUDENT
    #[2] CHANGE STUDENT'S GRADE
    #[3] SEE ALL STUDENTS' GRADES
    #[4] SEE ONE STUDENT'S GRADE
    #[5] SEE CLASS STATS
    #[6] END PROGRAM
    try:
        choice = int(raw_input("Enter Choice:"))
    except:
        print("Something went wrong")
    while(choice !=6 ):
        if choice == 1: #[1] ADD STUDENT
            inputNewStudent()
        elif choice == 2: #[2] CHANGE STUDENT'S GRADE

            inputStudentsGrade()
        elif choice == 3: #[3] SEE ALL STUDENTS' GRADES
            if(len(studentDict)>0):
                for x in studentDict:
                    print(str(x) + ": " + str(studentDict.get(x)))
            else:
                print("No students")
        elif choice == 4: #[4] SEE ONE STUDENT'S GRADE
            y=findStudentGrade()
            print(y)
        elif choice == 5: #[5] SEE CLASS STATS
            if(len(studentDict)>0):
                y=findAverageGrade()
                print("Class Average:")
                print(y)
                #min = findMinGrade()
                min2 = findMinGradeBetter()
                #max = findMaxGrade()
                max2 = findMaxGradeBetter()
                print("Min grade:")
                #print(min)
                print(min2)
                print("Max grade:")
                #print(max)
                print(max2)
                print("Student with min grade:")
                findStudentWithGrade(min2)
                print("Student with max grade:")
                findStudentWithGrade(max2)
            else:
                print("No students")

        elif choice == 6:
            break
        else:
            print("Please enter a valid choice")
            print("your choice was:")
            print(choice)
        try:
            choice = int(raw_input("Enter Choice:"))
        except:
            print("Something went wrong")
    #return

    #end of main

#namesList = studentDict.keys()
#gradesList = studentDict.values()


def inputNewStudent():
    name= raw_input("Enter Student Name:")
    if(name in studentDict):
        print("Student already in Dictionary")
    else:
        addStudent(name)
    return
    #end of inputNewStudent

def inputStudentsGrade():
    name= raw_input("Enter Student Name:")
    if name in studentDict:
        grade = int(raw_input("Enter Student's Grade:"))
        updateGrade(name,grade)
    else:
        print("Student does not exist")
    return
    #end of inputNewStudent

def addStudent(name,grade=0): #add a student with a name and a grade. default grade is zero, and can be changed later
    studentDict[name]=grade
    namesList = studentDict.keys()
    gradesList = studentDict.values()
    return
    #end of addStudent

def updateGrade(name,grade):
    studentDict[name] = grade
    namesList = studentDict.keys()
    gradesList = studentDict.values()

    pass
    #end of updateGrade

def findStudentGrade():
    name= raw_input("Enter Student Name:")
    if name in studentDict:
        return studentDict[name]
    else:
        print("Student does not exist")
    #end of findStudentGrade

def findAverageGrade():
    gradesList = studentDict.values()
    sum=0
    average=0
    if(len(gradesList)>0):
        for x in gradesList:
            sum += x
        average = sum/len(gradesList)

            
    return average
    #end of findAverageGrade()

def findMaxGrade():
    max =0
    gradesList = studentDict.values()
    if(len(gradesList)>0):
        for x in gradesList:
            if(x>max):
                max = x
        return max
    #end of findMaxGrade

def findMaxGradeBetter():
    gradesList = studentDict.values()
    gradesList.sort()
    return gradesList[-1]
    
    #end of findMaxGradeBetter

def findMinGrade():
    gradesList = studentDict.values()
    min =100
    if(len(gradesList)>0):
        for x in gradesList:
            if(x<min):
                min = x
        return min
    else:
        pass
    #end of findMinGrade


def findMinGradeBetter():
    gradesList = studentDict.values()
    gradesList.sort()
    return gradesList[0]
    #end of findMaxGradeBetter

def findStudentWithGrade(grade):

    if(len(studentDict)>0):
        for x in studentDict:
            if(studentDict.get(x) == grade):
                print(x)
    else:
          pass

    return
    #end of findStudentWithGrade

def displayMenu():
    print(''' 
    THIS PROGRAM SHOWS DATA FOR A DICTIONARY OF STUDENTS AND THEIR GRADES
    CHOOSE WHAT YOU WANT TO DO
    [1] ADD STUDENT
    [2] CHANGE STUDENT'S GRADE
    [3] SEE ALL STUDENTS' GRADES
    [4] SEE ONE STUDENT'S GRADE
    [5] SEE CLASS STATS
    [6] END PROGRAM
    ENTER A NUMBER:
    ''')

    #end of displayMenu

main()
