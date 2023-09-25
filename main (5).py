class Student:
  def __init__(self, name, roll_number, cgpa):
     self. name = name
     self. roll_number = roll_number
     self. cgpa = cgpa 
def sort_students(student_list): 
# sort the list of the student in the decending order of CGPA
    sorted_students = sorted(student_list, key=lambda student:student.cgpa, reverse=True)
    return sorted_students

# Example usage:
students = [Student("MohanaHarini","A124",7.8),Student("Pooja","A125",8.9),Student("Mani","A126",9.1),Student("Logeshwari","A126",9.9),]  

sorted_students = sort_students (students)
# print the sorted list of students
for student in sorted_students: 
  print("Name:{}, Roll Number:{}, CGPA:{}". format(student.name,student.roll_number,student.cgpa))
  