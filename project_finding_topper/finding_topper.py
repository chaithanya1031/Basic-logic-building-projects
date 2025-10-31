#nested dictionary
students = {
    'John': {'math': 80, 'science': 75},
    'Alice': {'math': 90, 'science': 82},
    'Bob': {'math': 70, 'science': 65}
}
avg=0
maximum=90
for student in students:
    for key, value in students[student].items():
        avg=(avg+ value)/len(student)
        if value>=maximum:
            print(f'{student} is topper has scored {value} in {key}')
    print(f'Student {student} has average {avg:.2f}')