students = [
                {"name":"염성현", "korean":82, "science":93, "english":76},
                {"name":"홍길동", "korean":37, "science":65, "english":97},
                {"name":"이몽룡", "korean":92, "science":96, "english":49},
                {"name":"박지성", "korean":38, "science":73, "english":96}
]

print("이름", "총점", "평균",sep='\t')
for student in students:
    score_sum = student["korean"] + student["science"] + student["english"]
    score_average = score_sum / 3
    print(student['name'], score_sum, score_average, sep='\t')