num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

class_average = 0

for s in range(1, num_students + 1):
    print("Student", s)
    total = 0
    
    for subj in range(1, num_subjects + 1):
        score = float(input("Enter score " + str(subj) + ": "))
        total = total + score
        
    avg = total / num_subjects
    print("Average for Student", s, "=", avg)
    class_average = class_average + avg
    
print("\nClass Average =", class_average / num_students)