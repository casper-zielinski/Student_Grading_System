import GradingSystem

print("---------------Wilkommen------------------")
print("1. Add Students")
print("2. Add Exercise")
print("3. Show Student")
print("4. View Student")
print("5. Cancel")

Students = GradingSystem.Students([])


def Menu(run):
      while run:
            Eingabe = input("Gebe deine Option ein:   ")
            match Eingabe:
                  case "1":
                        Vorname = input("Gib Vornamen ein:  ")
                        Nachname = input("Gib Nachnamen ein:    ")
                        Alter = int(input("Gib alter ein:     "))
                        Name = Vorname + " " + Nachname

                        Student = GradingSystem.Student(Name,Alter,[]) 
                        Students.addStudent(Student)    
                        print(f"Schüler Eingefügt, Schülerinfo: {Student.ViewStudent()}")             
                  case "2":
                        print(2)
                  case "3":
                        print(3)
                  case "4":
                        print(4)
                  case "5":
                        print("Canceling App")
                        run = False
                  case _:
                        print("----------------")
                        print("Keine solche Option, wähle eines der angegebenen Optionen")
                        print("----------------")
                        Menu()


Menu(True)





