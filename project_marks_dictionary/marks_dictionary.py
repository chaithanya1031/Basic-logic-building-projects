#marks dictionary
marks={'venu':10,
       'prabha':10,
       'seetha':9,
       'renu':8}
total=0
for value in marks:
    total=total+marks[value]
print(f'the total marks is: {total}')
top_student=[]
highest=0
for value in marks.values():#10
    if value>highest:#10>0
        highest=value#highest=10
        print(f'the highest mark is: {value}')
for key, value in marks.items():
    if value==highest:
        top_student.append(key)
print(f'the top students are {top_student}')