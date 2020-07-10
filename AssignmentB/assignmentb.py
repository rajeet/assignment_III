class Academy:
    def __str__(self):
        print("Welcome to Academy")
        print("_" *50)
        print("S.N.      Detail")
        print("1: Enquiry about course of study")
        print("2: Register for course")
        print("3: Display all students information")
        print("4: Update Information")
        print("_" *50)
    
    def detail_about_course(self):
        html = "HTML Basics"
        css = "CSS Basics"
        js = "JS Basics"
        php = "PHP"
        python = "Python Basics"

        print("Course of Content")
        print(f"1: {html} \n2: {css}\n3: {js} \n4: {php} \n5: {python}")


class Student(Academy):
    def __init__(self, name, age, contact, deposit):
        self.name = name
        self.age = age
        self.contact = contact
        self.deposit = deposit
        

if __name__ == "__main__":
    obj = Academy()
    obj.__str__()
    takeinput = int(input("Enter S.N. \n"))
    if takeinput == 1:
        obj.detail_about_course()

        
    elif takeinput == 2:
        print("_"*50)
        print("Students are allowed to pay in two installments with Rs. 10000 each")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        contact = input("Enter Contact: ")
        deposit = input("Enter Deposit: ")

        add_student = Student(name, age, contact, deposit)

        print("Student Registered")
        


