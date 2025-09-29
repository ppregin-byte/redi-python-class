# Grade Calculator
# ```
# Ask for student names and their test scores
def ask_user():
    name = input("Enter student name (or 'done' to finish): ")
    if name.lower() == "done":
        return None, None
    else:
        while True:
            sc = input("Enter test scores separated by spaces: ").split() 
            scores = []
            valid = True
            # Check if all inputs are valid numbers (integers or floats)
            for x in sc:
                check = x.replace(".", "", 1) 
                if check.isdigit():
                    scores.append(float(x)) 
                else:
                    print("Invalid input. Please enter numbers only.")
                    valid = False
                    break
            if valid:
                return name, scores 
# Calculate the average of multiple test scores 
def calculate_average(scores):
    if scores is None:
        return None
    else:
        return sum(scores) / len(scores)   

# Apply a curve (add points to boost grades)
def applying_curves(aver):
    if aver is None:
        return None
    else:
        return aver + 5  

# Convert numerical grades to letter grades
def converting_letter(curve):
    if curve is None:
        return None
    else:
        if curve >= 97:         
            return "A+"
        elif curve >= 93:
            return "A"        
        elif curve >= 90:
            return "A-"
        elif curve >= 87:
            return "B+"
        elif curve >= 83:
            return "B"
        elif curve >= 80:
            return "B-"
        elif curve >= 77:
            return "C+"
        elif curve >= 73:
            return "C"
        elif curve >= 70:
            return "C-"                
        elif curve >= 67:
            return "D+"
        elif curve >= 63:
            return "D"
        elif curve >= 60:
            return "D-" 
        else:
            return "F"        
# Format the output nicely
def formatting_output(name, average, curves, letter):
    print(f"Student: {name}")
    print(f"Original Average: {average:.2f}")
    print(f"Curved Average: {curves:.2f} (+5 curve)")
    print(f"Letter Grade: {letter}")

def main():
    while True:
        name_score = ask_user()   
        if name_score[0] is None:
            break
        average = calculate_average(name_score[1])
        curves = applying_curves(average)
        letter = converting_letter(curves)
        formatting_output(name_score[0], average, curves, letter)

main()