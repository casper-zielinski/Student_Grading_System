import statistics
from typing import List, Optional

class Exercise:
      """Represents an exercise with an ID and name."""
      def __init__(self, id, name):
            """
            Initialize an exercise.

            Args:
                id: Unique identifier for the exercise
                name: Name of the exercise
            """
            self.id = id
            self.name = name

      def ViewExercise(self):
            """Print the exercise ID and name."""
            return  print(f"{self.id}: {self.name}")

class Student:
      """Represents a student with name, age, and their exercise grades."""
      def __init__(self, name, alter,  exercise_grading: List[int]):
            """
            Initialize a student.

            Args:
                name: Student's name
                alter: Student's age
                exercise_grading: List of dictionaries containing exerciseID and grade
            """
            self.name = name
            self.alter = alter
            self.exercise_grading: List[dict] = exercise_grading

      def ViewStudent(self):
            """Return formatted string with student information."""
            return f"{self.name} ist ein Schüler der {self.alter} alt ist und hat {len(self.exercise_grading)} übungen zugeteilt"

      def AvarageGrade(self):
            """Calculate and return the average grade across all exercises."""
            if not self.exercise_grading:
                  return 0
            grades = [g["grade"] for g in self.exercise_grading]
            return statistics.mean(grades)

      def AddExerciseGrade(self, exerciseID, exerciseGrade):
            """
            Add a new exercise grade or update existing one.

            Args:
                exerciseID: The ID of the exercise
                exerciseGrade: The grade to add or update
            """

            for ex in self.exercise_grading:
                  if ex["exerciseID"] == exerciseID:
                        print("Diese Exercise exisitiert bereits. Überschreibe nun die Note...")
                        ex["grade"] = float(exerciseGrade)
                        print("Note wurde überschrieben!")
                        return
               
            self.exercise_grading.append({"exerciseID": exerciseID, "grade": exerciseGrade})
            print("Note wurde eingetragen!")
            

class Students:
      """Container class for managing multiple students."""
      def __init__(self, Students: List[Student]):
            """
            Initialize the students container.

            Args:
                Students: List of Student objects
            """
            self.students: List[Student] = Students

      def addStudent(self, Student):
            """
            Add a new student to the collection.

            Args:
                Student: Student object to add
            """
            self.students.append(Student)
            return self.students

      def countStudents(self):
            """Return the total number of students."""
            return len(self.students)

      def FindStudent(self, name: Optional[str], alter: Optional[int]):
            """
            Find a student by name or age.

            Args:
                name: Student's name (optional)
                alter: Student's age (optional)

            Returns:
                Student object if found, None otherwise
            """
            if name is None and alter is None:
                  return "Bitte name oder alter angeben"
            #  Search by age
            elif name is None:
                  Schüleralter = list(map(lambda x: x.alter, self.students))
                  # docs: https://www.w3schools.com/python/python_try_except.asp
                  try:
                        index = Schüleralter.index(alter)
                        return self.students[index]

                  except ValueError:
                        print("Student not found")
            # Search by name
            else:
                  Schüleralter = list(map(lambda x: x.name, self.students))
                  try:
                        index = Schüleralter.index(name)
                        return self.students[index]
                  except ValueError:
                        print("Student not found")
                  
