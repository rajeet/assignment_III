import csv


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
            print("Input Out of Bound")





    def register_student(self, course):
        print("_" * 50)
        print("Note: Students are allowed to pay in two installments with Rs. 10000 each")
        print("You have select {}".format(course))
        name = input("Enter Your Name: ")
        age = input("Enter your age: ")
        deposit = input("Enter S.N. for Deposit \n1: For full \n2: In installment\n>")

        print(f"{name} {age} {deposit} {course}")

        with open("studentdata.csv", mode='w') as student_file:
             fieldnames = ['Student_Name', 'Age', 'Deposit', 'Course']
             writer = csv.DictWriter(student_file, fieldnames=fieldnames)
             writer.writeheader()
             writer.writerow({'Student_Name': 'John Smith', 'Age': 'Accounting', 'Deposit': 'November', 'Course': 'Html'})







    def display_students(self):
        pass




    def update_students(self, id):
        pass



    def delete_students(self, id):
        pass

    def opening_page(self):
        print("Welcome to Academy")
        print("_" *50)
        print("S.N.      Detail")
        print("1: Enquiry about course of study")
        print("2: Register for course")
        print("3: Display all students information")
        print("4: Update Information")
        print("_" *50)
        
        takeinput = int(input("Enter S.N. \n"))
        if takeinput == 1:
            self.course_of_content()



if __name__ == "__main__":
    obj = Academy()
    obj.opening_page()
    
        

