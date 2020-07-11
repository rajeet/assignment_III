import csv
import os
import sys
from tabulate import tabulate



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
            # edit here 
            if os.path.getsize("studentdata.csv") > 0:
                print("not empty")
                writer.writerow({'Student_Name': name, 'Age': age, 'Contact': contact, 'Deposit': deposite, 'Course': course})     
            else:
                print("empty")
                writer.writeheader()
                writer.writerow({'Student_Name': name, 'Age': age, 'Contact': contact, 'Deposit': deposite, 'Course': course})


        print("Thank you for registering")
        self.ifelse()


    def display_students(self):
        
        # edit here
        table = []

        # edit ends here 
        # if os.path.isfile("studentdata.csv"):
        #     with open('studentdata.csv', mode='r') as read_student_data:
        #         csv_reader = csv.DictReader(read_student_data)
        #         line_count = 0
        #         for row in csv_reader:
        #             if line_count == 0:
        #                 table.append(list(row))
        #                 line_count += 1
        #             dat = [row['Student_Name'], row['Age'], row['Contact'], row['Deposit'], row['Course']]
        #             table.append(dat)
        #     line_count += 1
        #     print(tabulate(table))
            
        # else:
        #     print("Fild doesnot exists")

        # self.ifelse()

        try:
            with open('studentdata.csv', mode='r') as read_student_data:
                csv_reader = csv.DictReader(read_student_data)
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        table.append(list(row))
                        line_count += 1
                    dat = [row['Student_Name'], row['Age'], row['Contact'], row['Deposit'], row['Course']]
                    table.append(dat)
            line_count += 1
            print(tabulate(table))
        except (FileNotFoundError, IOError):
            print("File doesnot exists")
        
        self.ifelse()

    def update_students(self, contact):
        print(contact)

        data = dict()
        fake = []
        input_file = csv.DictReader(open("studentdata.csv"))
        for row in input_file:
            fake.append(row)

        for i in fake:
            if int(i["Contact"]) == contact:
                print(f"Name: {i['Student_Name']}")
                print(f"Age: {i['Age']}")
                print(f"Contact: {i['Contact']}")
                print(f"Deposit: {i['Deposit']}")
                print(f"Course: {i['Course']}")

                fake.remove(i)
                print("_"*50)
                name = input("Update your Name: ")
                age = input("Update your age: ")
                contact= int(input("Update your contact number: "))
                deposit = int(input("Update S.N. for Deposit \n1: For full \n2: In installment\n>"))
                if deposit == 1: 
                    deposite = 20000 
                else:
                    deposite = 10000
                course = input("HTML Basics \nCSS Basics \nJS Basics\nPHP Basics \npython Basics\n")
                print(f"{name} {age} {contact} {deposite} {course}")
                print("_"*50)

                fake.append({'Student_Name': name, 'Age': age, 'Contact': contact, 'Deposit': deposite, 'Course': course})
                break
            else: 
                print("False")

    # edits start here
        with open("newstudentdata.csv", 'a+', newline='') as student_file:
            fieldnames = ['Student_Name', 'Age', 'Contact', 'Deposit', 'Course']
            writer = csv.DictWriter(student_file, fieldnames=fieldnames)
            # edit here 
            writer.writeheader()
            for i in fake:
                    writer.writerow({'Student_Name': i['Student_Name'], 'Age': i['Age'], 'Contact': i["Contact"], 'Deposit': i['Deposit'], 'Course': i['Course']})     


        print("Thank you for Updating")
        old = "studentdata.csv"
        new = "newstudentdata.csv"
        os.remove("studentdata.csv")
        os.rename(new, old)

        self.ifelse()




    def delete_students(self, contact):
        deletedata = []
        print(contact)
        input_file = csv.DictReader(open("studentdata.csv"))
        for row in input_file:
            deletedata.append(row)
        
        for i in deletedata:
            print (i)
            if int(i["Contact"]) == contact:
                deletedata.remove(i)
        print(deletedata)
        with open("newstudentdata.csv", 'w', newline='') as student_file:
            fieldnames = ['Student_Name', 'Age', 'Contact', 'Deposit', 'Course']
            writer = csv.DictWriter(student_file, fieldnames=fieldnames)
            # edit here 
            writer.writeheader()
            for i in deletedata:
                    writer.writerow({'Student_Name': i['Student_Name'], 'Age': i['Age'], 'Contact': i["Contact"], 'Deposit': i['Deposit'], 'Course': i['Course']})     
            
        print("Data Deleted")
        old = "studentdata.csv"
        new = "newstudentdata.csv"
        os.remove("studentdata.csv")
        os.rename(new, old)        

        
        self.ifelse()
    
    def ifelse(self):
        print("_" * 50)
        k = input("0 for back: \n")
        if k == '0':
            self.opening_page()
        else:
            print("Terminating")
            sys.exit()

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
            print("Deleting Data require some inputs....")
            contact = int(input("Enter the student contact number for deleting details: \n"))
            print("_"*50)
            self.delete_students(contact)
        else:
            print("Invalid input entered \nTerminating program.......")
            sys.exit()

if __name__ == "__main__":
    obj = Academy()
    obj.opening_page()
    
        

