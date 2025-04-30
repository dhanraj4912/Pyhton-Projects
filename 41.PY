data=[]

def addstud():
    print("\n")
    id=input("Enter Student ID : ")
    name=input("Enter Name : ")
    age=input("Enter Age : ")
    course=input("Enter Course : ")
    print("\n")
    details=[id,name,age,course]
    data.append(details)

def disstud():
    print("\n")
    print("Student List : ")
    for i in data:
        print("Student ID : ",i[0])
        print("Name : ",i[1])
        print("Age : ",i[2])
        print("Course : ",i[3])
        print("\n")

def updstud():
    id=input("Enter Student ID to Update Information : ")
    print('''
1. Name
2. Age
3. Course ''')
    qty=int(input("Select the Information to update : "))
    if qty==1:
        val=input("Enter the new Name : ")
        for i in data:
            if i[0]==id:
                i[1]=val
                print("\n")
                print("Student information updated successfully.")
                print("\n")
            else:
                pass
    elif qty==2:
        val=input("Enter the new Age : ")
        for i in data:
            if i[0]==id:
                i[2]=val
                print("\n")
                print("Student information updated successfully.")
                print("\n")
            else:
                pass
    elif qty==3:
        val=input("Enter the new Course : ")
        for i in data:
            if i[0]==id:
                i[3]=val
                print("\n")
                print("Student information updated successfully.")
                print("\n")
            else:
                pass
    else:
        pass

def search():
    id=input("Enter Student ID to Search : ")
    print("Student Details : ")
    for i in data:
        if i[0]==id:
            print("Student ID : ",id)
            print("Name : ",i[1])
            print("Age : ",i[2])
            print("Course : $",i[3])
            print("\n")
            
def avgstud():
    avg=[]
    for i in data:
        avg.append(int(i[2]))
    print("Average Age of Students : ",sum(avg)/len(avg))
    print("\n")

def remstud():
    id=input("Enter Student ID to Remove : ")
    for i in data:
        if i[0]==id:
            data.remove(i)
            print("Student removed from the list.")
    print("\n")

    
def menu():
    print('''
1. Admit Student
2. Display Student List
3. Update Student Information
4. Search Student by ID
5. Calculate Average Age
6. Remove Student by ID
7. Exit''')
status=True
menu()
while status==True:
    x=int(input("Enter your choice : "))
    if x==1:
        addstud()
    elif x==2:
        disstud()
    elif x==3:
        updstud()
    elif x==4:
        search()
    elif x==5:
        avgstud()
    elif x==6:
        remstud()
    elif x==7:
        status=False
    else:
        print("Enter valid choice....")
