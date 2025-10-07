# Student Grading System

A simple Python-based grading system for managing students and their exercise grades.

## Features

- **Exercise Management**: Track individual exercises with descriptions and grades
- **Student Management**: Store student information including name, age, and grades
- **Grade Calculation**: Automatically calculate average grades for each student
- **Student Search**: Find students by name or age
- **Collection Management**: Manage multiple students in a single container

## Classes

### Exercise
Represents an individual exercise with a description and grade.

### Student
Represents a student with:
- Name
- Age (alter)
- List of exercise grades
- Methods to view student info and calculate average grade

### Students
Container class for managing multiple students with methods to:
- Add new students
- Count total students
- Find students by name or age

## Usage Example

```python
from GradingSystem import Student, Students

# Create students
max = Student("Max", 12, [4, 2, 4, 1])
lena = Student("Lena", 14, [2, 5, 2])

# Create students collection
students = Students([max, lena])

# Get student information
print(max.ViewStudent())
print(f"Average grade: {max.AvarageGrade()}")

# Add a new grade
max.AddExerciseGrade(3)

# Find a student
found = students.FindStudent(name="Max", alter=None)
```

## Requirements

- Python 3.6+
- Standard library only (no external dependencies)
