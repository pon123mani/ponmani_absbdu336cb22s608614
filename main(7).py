
class student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa;
  def sort_student(student_list):
    sort_student=sorted(student_list,
                        key=lamda student=student.cgpa,reverse=true)
    return sorted_students
students=[
  student("hari","a123",7.8),
  student("srikanth,""a124",8.9),
  student("mahidhar","a125",9.9)
]    
sorted_students=sort_student(student)
   for student in sorted_student:
     print("name:{},rollnumber:{},cgpa:{}".format(stud)".format(student.name,student.roll_number,student.cgpa))

    