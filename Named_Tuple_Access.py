#Given a list of tuples students where each tuple is (name, grade), return the name of the student with
#the highest grade
def student_nums(students):
    highest = students[0]

    for student in students:       
        if student[1] > highest[1]:   
            highest = student

    return highest[0]

print(student_nums([('Ali',90),('Sara',95),('Tom',80)]))

            
 
           
             