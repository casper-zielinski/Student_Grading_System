# Student Grading System

A Python-based grading system for managing students and their exercise grades with an interactive command-line interface.

## Project Structure

- `src/GradingSystem.py` - Core classes (Exercise, Student, Students)
- `src/Shower.py` - Interactive CLI menu for managing students

## Features

- Add and manage students (name, age, grades)
- Track exercise grades and calculate averages
- Search students by name or age
- Interactive menu interface

## Running the Application

```bash
python src/Shower.py
```

The menu offers options to:
1. Add Students
2. Add Exercise (TODO)
3. Show Student (TODO)
4. View Student (TODO)
5. Exit

## Classes

### Exercise
Represents an exercise with description and grade.

### Student
Stores student data: name, age, and exercise grades.

### Students
Container for managing multiple Student objects.

## Requirements

- Python 3.10+ (uses match/case)
- Standard library only
