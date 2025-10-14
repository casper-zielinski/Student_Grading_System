"""
Interactive menu system for the Student Grading System.
Allows users to add students, manage exercises, and view student information.
"""

import GradingSystem

# Display welcome menu
print("---------------Wilkommen------------------")
print("1. Add Students")
print("2. Add Exercise")
print("3. View Exercise")
print("4. View Student")
print("5. Cancel")

# Initialize the students collection
Students = GradingSystem.Students([])

Exercises = []
exerciseCount = 0

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
                        global exerciseCount
                        exerciseCount += 1  
                        ExerciseName = input("Gib einen Namen für die neue Übung ein: ")

                        newExercise = GradingSystem.Exercise(exerciseCount, ExerciseName)
                        Exercises.append(newExercise)
                        print(f"Neue Übung hinzugefügt: {newExercise.id} - {newExercise.name}")

                        # Punkte für jeden Schüler erfassen
                        if Students.countStudents() == 0:
                              print("Es gibt noch keine Schüler. Bitte zuerst Schüler hinzufügen.")
                        else:
                              for student in Students.students:
                                    try:
                                          grade = float(input(f"Gib die Punkte für {student.name} ein: "))
                                    except ValueError:
                                          print("Ungültige Eingabe, setze Note auf 0.")
                                          grade = 0.0

                                    student.AddExerciseGrade(newExercise.id, grade)
                                    print(f"Punkte gespeichert für {student.name}: {grade}")
                  case "3":
                        if len(Exercises) == 0:
                              print("Keine Übungen vorhanden!")
                              break

                         # docs: https://www.w3schools.com/python/python_try_except.asp
                        try:
                              exerciseID = int(input("Gib die ID der Übung ein: "))
                        except ValueError:
                              print("Ungültige Eingabe!")
                              break

                        # Prüfen, ob die ID existiert
                        foundExercise = None
                        for ex in Exercises:
                              if ex.id == exerciseID:
                                    foundExercise = ex
                                    break

                        if foundExercise is None:
                              print("Diese Übung gibt es nicht!")
                              break

                        print(f"\n--- Ergebnisse für Übung '{foundExercise.name}' ---")
                        if Students.countStudents() == 0:
                              print("Es gibt keine Schüler.")
                        else:
                              for student in Students.students:
                                    foundGrade = None
                                    for g in student.exercise_grading:
                                          if g["exerciseID"] == exerciseID:
                                                foundGrade = g["grade"]
                                                break

                                    if foundGrade is not None:
                                          print(f"{student.name}: {foundGrade} Punkte")
                                    else:
                                          print(f"{student.name}: keine Note eingetragen")
                  
                  case "4":
                         # Schüler anzeigen
                        name = input("Gib den Namen des Schülers ein: ")

                        # Schüler suchen
                        student = Students.FindStudent(name, None)
                        if student is None:
                              print("Schüler wurde nicht gefunden!")
                              break

                        # Schülerinformationen anzeigen
                        print(f"\n--- Schülerinfo ---")
                        print(student.ViewStudent())

                        if not student.exercise_grading:
                              print("Keine Übungen vorhanden.")
                        else:
                              print("\n--- Notenübersicht ---")
                              for grade_entry in student.exercise_grading:
                                    exerciseID = grade_entry["exerciseID"]
                                    grade = grade_entry["grade"]

                                    
                                    exercise = next((ex for ex in Exercises if ex.id == exerciseID), None)
                                    exercise_name = exercise.name if exercise else "(unbekannte Übung)"

                                    print(f"Übung {exerciseID} ({exercise_name}): {grade} Punkte")

                              print(f"\nDurchschnittsnote: {student.AvarageGrade():.2f}")
                        
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
