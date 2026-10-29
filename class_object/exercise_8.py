class StudentGrades():
    def __init__(self,name):
        self.name=name
        self.grade=[]
    def add_grade(self,num):
         self.grade.append(num)
    def get_average(self):
        if len(self.grade)==0:
           return None
        return sum(self.grade)/len(self.grade)
    def get_highest(self):
        if len(self.grade)==0:
            return None
        return max(self.grade)

student = StudentGrades("Saif")
# student.add_grade(80)
# student.add_grade(90)
student.add_grade(70)
print(student.get_average())
print(student.get_highest())