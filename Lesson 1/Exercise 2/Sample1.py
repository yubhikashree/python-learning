def get_total(marks):
    return sum(marks)

def get_average(marks):
    return sum(marks)/len(marks)

def get_grade(average):
    if average <= 100 and average >= 90:
        return "A" 
    elif average < 90 and average >= 75:
        return "B"
    elif average < 75 and average >= 60:
        return "C"
    elif average < 60 and average >= 40:
        return "D"
    else:
        return "F"

def print_report(name, marks):
    print(f"Name     : {name}")
    print(f"Total    : {get_total(marks)}")
    print(f"Average  : {get_average(marks):.2f}%")
    print(f"Grade    : {get_grade(get_average(marks))}")
    print()

print_report("Yubhi", [92, 88, 95])
print_report("Arun", [55, 60, 48])

