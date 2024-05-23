class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
students = [Student("Joe", 0.48), Student("Amy", 0.78), Student("Penny", 0.88), Student("Sheldon", 0.97),
            Student("Raj", 0.78), Student("Leonard", 0.98), Student("Harold", 0.68), Student("Missy", 0.77)]


student_results = []
for student in students:
    if student.score >= 0.7:
        student_results.append(f"{student.name} Passed")
    else:
        student_results.append(f"{student.name} Failed")
        
        

print(student_results)