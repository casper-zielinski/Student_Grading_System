"""
Interactive menu system for the Student Grading System.
Allows users to add students, manage exercises, and view student information.
"""

import GradingSystem

# Display welcome menu
print("---------------Wilkommen------------------")
print("1. Add Students")
print("2. Add Exercise")
print("3. Show Student")
print("4. View Student")
print("5. Cancel")

# Initialize the students collection
Students = GradingSystem.Students([])


def Menu(run):
      """
      Main menu loop for the grading system.

      Args:
            run: Boolean to control the menu loop
      """
      while run:
            Eingabe = input("Gebe deine Option ein:   ")
            match Eingabe:
                  case "1":
                        # Add a new student
                        Vorname = input("Gib Vornamen ein:  ")
                        Nachname = input("Gib Nachnamen ein:    ")
                        Alter = int(input("Gib alter ein:     "))
                        Name = Vorname + " " + Nachname

                        Student = GradingSystem.Student(Name,Alter,[])
                        Students.addStudent(Student)
                        print(f"Schüler Eingefügt, Schülerinfo: {Student.ViewStudent()}")
                  case "2":
                        # TODO: Implement add exercise functionality
                        print(2)
                  case "3":
                        # TODO: Implement show student functionality
                        print(3)
                  case "4":
                        # TODO: Implement view student functionality
                        print(4)
                  case "5":
                        # Exit the application
                        print("Canceling App")
                        run = False
                  case _:
                        # Handle invalid input
                        print("----------------")
                        print("Keine solche Option, wähle eines der angegebenen Optionen")
                        print("----------------")
                        Menu()

Menu(True)
