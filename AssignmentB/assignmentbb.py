import csv
import sys

class Academy:
    def course_of_content(self):
            
        li = ["HTML Basics", "CSS Basics", "JS Basics", "PHP Basics", "python Basics"]
        print("Course of Content")
        sn = 1
        for i in li:
            print(f"{sn} {i}")
            sn += 1

        k = int(input("Enter S.N. for regestering or press 0 for back: \n"))
        if k == 0:
            self.opening_page()
        elif k > 0 and k < 6:
            self.register_student(li[k-1])
        else:
            print("Terminating")
            sys.exit()




    def register_student(self, course):
        print("_" * 50)
        print("Note: Students are allowed to pay in two installments with Rs. 10000 each")
        print("You have select {}".format(course))
        name = input("Enter your Name: ")
        age = int(input("Enter your age: "))
        contact=int(input("Enter your contact number: "))
        deposit = int(input("Enter S.N. for Deposit \n1: For full \n2: In installment\n>"))
        if deposit == 1: 
            deposite = 20000 
        else:
            deposite = 10000
        print(deposite)
        print(f"{name} {age} {contact} {deposite} {course}")

        with open("studentdata.csv", 'a+', newline='') as student_file:
            fieldnames = ['Student_Name', 'Age', 'Contact', 'Deposit', 'Course']
            writer = csv.DictWriter(student_file, fieldnames=fieldnames)
            writer.writerow({'Student_Name': name, 'Age': age, 'Contact': contact, 'Deposit': deposite, 'Course': course})


        print("Thank you for registering")
        k = input("0 for back: \n")
        if k == '0':
            self.opening_page()
        else:
            print("Terminating")
            sys.exit()

    def display_students(self):
        with open('studentdata.csv', mode='r') as read_student_data:
             csv_reader = csv.DictReader(read_student_data)
             line_count = 0
             for row in csv_reader:
                if line_count == 0:
                    print(f'{", ".join(row)}')
                    line_count += 1
                print(f"{row['Student_Name']} || {row['Age']} || {row['Age']} || {row['Contact']} || {row['Deposit']} || {row['Course']}")
        line_count += 1
                    





    def update_students(self, contact):
        print(contact)




    def delete_students(self, contact):
        print(contact)
        

    def opening_page(self):
        print("Welcome to Academy")
        print("_" *50)
        print("S.N.      Detail")
        print("1: Enquiry about course of study")
        print("2: Register for course")
        print("3: Display all students information")
        print("4: Update Information")
        print('5: Delete Information')
        print("_" *50)
        
        takeinput = int(input("Enter S.N. \n"))
        if takeinput == 1:
            self.course_of_content()
        elif takeinput == 2:
            print("Select Course First: \n")
            self.course_of_content()
        elif takeinput == 3:
            print("Displaying Student Datas.........")
            print("_" *50)
            self.display_students()
        elif takeinput == 4:
            print("Updating Data require some inputs....")
            contact = int(input("Enter the student contact number for updating details: \n"))
            print("_" *50)
            self.update_students(contact)
        elif takeinput == 5:
            




if __name__ == "__main__":
    obj = Academy()
    obj.opening_page()
    
        

