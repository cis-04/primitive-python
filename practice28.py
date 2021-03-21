def create_student(name, korean, math, english, science):
    return {
            "name":name,
            "korean":korean,
            "math":math,
            "english":english,
            "science":science
           }

def sum_score(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def average(student):
    return sum_score(student) / 4

def claculating(student):
    print("{}\t{}\t{}".format(student["name"], sum_score(student), average(student)))



students = [
                create_student("염성현", 93, 83, 78, 67),
                create_student("임성현", 93, 83, 78, 67),
                create_student("암성현", 93, 83, 78, 67),
                create_student("엄성현", 93, 83, 78, 67)
            ]


print("이름", "총점", "평균",sep='\t')
for student in students:
    print(claculating(student))