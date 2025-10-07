import statistics
from typing import List, Optional

class Exercise:
      def __init__(self, desc, grade):
            self.desc = desc
            self.grade = grade

      def ViewExercise(self):
            return self.desc
      
      def ViewGrade(self):
            return self.grade

class Student:
      def __init__(self, name, alter, exercise_grading: List[int]):
            self.name = name
            self.alter = alter
            self.exercise_grading: List[int] = exercise_grading

      def ViewStudent(self):
            return f"{self.name} ist ein Schüler der {self.alter} alt ist und hat {len(self.exercise_grading)} übungen zugeteilt"
      
      def AvarageGrade(self):
            return statistics.mean(self.exercise_grading)
      
      def AddExerciseGrade(self, exercise_grade):
            self.exercise_grading.append(exercise_grade)
      

class Students:
      def __init__(self, Students: List[Student]):
            self.students: List[Student] = Students

      def addStudent(self, Student):
            self.students.append(Student)
            return self.students
            
      def countStudents(self):
            return len(self.students)
      
      def FindStudent(self, name: Optional[str], alter: Optional[int]):
            if name is None and alter is None:
                  return "Bitte name oder alter angeben"
            elif name is None:
                  Schüleralter = list(map(lambda x: x.alter, self.students))
                  try:
                        index = Schüleralter.index(alter)
                        return self.students[index]
                  
                  except ValueError:
                        print("Student not found")
            else:
                  Schüleralter = list(map(lambda x: x.name, self.students))
                  try:
                        index = Schüleralter.index(name)
                        return self.students[index]
                  except ValueError:
                        print("Student not found")
                  


