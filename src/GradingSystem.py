import statistics
from typing import List, Optional

class Exercise:
      """
      Represents an exercise with a description and grade.
      """
      def __init__(self, desc, grade):
            """
            Initialize an exercise.

            Args:
                desc: Description of the exercise
                grade: Grade received for the exercise
            """
            self.desc = desc
            self.grade = grade

      def ViewExercise(self):
            """Return the exercise description."""
            return self.desc

      def ViewGrade(self):
            """Return the exercise grade."""
            return self.grade

class Student:
      """
      Represents a student with name, age, and their exercise grades.
      """
      def __init__(self, name, alter, exercise_grading: List[int]):
            """
            Initialize a student.

            Args:
                name: Student's name
                alter: Student's age
                exercise_grading: List of grades for completed exercises
            """
            self.name = name
            self.alter = alter
            self.exercise_grading: List[int] = exercise_grading

      def ViewStudent(self):
            """Return formatted string with student information."""
            return f"{self.name} ist ein Schüler der {self.alter} alt ist und hat {len(self.exercise_grading)} übungen zugeteilt"

      def AvarageGrade(self):
            """Calculate and return the average grade across all exercises."""
            return statistics.mean(self.exercise_grading)

      def AddExerciseGrade(self, exercise_grade):
            """
            Add a new exercise grade to the student's record.

            Args:
                exercise_grade: The grade to add
            """
            self.exercise_grading.append(exercise_grade)


class Students:
      """
      Container class for managing multiple students.
      """
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

            Returns:
                Updated list of students
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
                Student object if found, error message otherwise
            """
            # Check if both parameters are None
            if name is None and alter is None:
                  return "Bitte name oder alter angeben"
            # Search by age if name is not provided
            elif name is None:
                  Schüleralter = list(map(lambda x: x.alter, self.students))
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
                  


Max = Student("Max",12,[4,2,4,1])
Lena = Student("Lena",14,[2,5,2])

