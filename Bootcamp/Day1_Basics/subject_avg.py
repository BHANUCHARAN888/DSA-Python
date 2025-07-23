marks = {'maths':80, 'physics': 85, 'chemistry': 90}
print(marks)
print(marks.keys())
print(marks.values())
T_marks=sum(marks.values())
print(f'Total marks: {T_marks}')
Avg=sum(marks.values())/len(marks)
print(f'Average marks: {Avg}')
