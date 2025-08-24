# cook your dish here
students=[]

def add_students():
    rollno=input("Enter student roll no:")
    Name=input("Enter your name:")
    age=int(input("enter your age:"))
    Branch=input("enter your branch:")
    student={"Rollno:":rollno,"Name:":Name,"age:":age,"Branch:":Branch}
    students.append(student)
    print("student details added successfully.\n")
    
def view_students():
    if not students:
        print("no student records found")
        return
    print("students record")
    for i,student in enumerate(students,1):
        print(f"{i}. Rollno:{student['Rollno']},Name:{student['Name']}, age:{student['age']},Branch:{student[Branch]}")
    print()
    
def update_students():
    roll_no=input("enter student roll no")
    for student in students:
        if student["Rollno"]==roll_no:
            print("current details:",student)
            student['Name']=input("enter updated name:")
            student['age']=input("enter updated age:")
            student["Branch"]=input('enter updated Branch')
            print("students details updated")
            return
    print("students details not found \n")
            
def delete_student():
    roll_no=input("enter student roll_no ")
    for student in students:
        if student['Rollno']==roll_no:
            students.remove(student)
            print("student record deleted successfully")
            return
    print("Student details not found \n")
        
            
def main():
    
    while True:
        print("***Student Management System****")
        print("1. add_students")
        print("2. view_students")
        print("3. update_students")
        print("4. delete_student")
        print("5. exit")
        
        choice=input("enter your choice:")
        if choice == '1':
            add_students()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_students()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("exiting... Goodbye")
            exit()
        else:
            print("Invalid choice")
        
if __name__=="__main__":
    main()