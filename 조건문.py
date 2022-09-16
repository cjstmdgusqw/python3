def get_grade(score):
    if score > 91:
       return "A"
    elif score > 81 and score < 90:
       return "B"
    elif score > 71 and score < 80:
       return "C"
    elif score <71:
       return "F"         
    
    

    

score = int(input())
grade = get_grade(score)
print(grade) # A ~ F