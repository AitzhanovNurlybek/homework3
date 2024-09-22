
def count_students_passed(file_name):
    passed_count = 0  

   
    with open(file_name, 'r') as file:
        for line in file:
            
            parts = line.split()
            username = parts[0]  
            scores = list(map(int, parts[1:])) 
            
        
            if all(score >= 50 for score in scores):
                passed_count += 1

    return passed_count


file_name = 'grades.txt'
result = count_students_passed(file_name)
print(f"Number of students who passed all three tests: {result}")
