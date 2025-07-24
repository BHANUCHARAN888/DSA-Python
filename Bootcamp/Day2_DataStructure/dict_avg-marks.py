dict1 = {
    "maths": 95,
    "physics": 94,
    "chemistry": 92
}
print(dict1.keys())
print(dict1.values())
total_marks=sum(dict1.values())
print(total_marks)
avg=total_marks/len(dict1)
print(avg)