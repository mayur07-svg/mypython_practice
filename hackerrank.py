records = []
s_name = []
s_grade = []
for _ in range(int(input())):
    name = input()
    grade = float(input())
    records.append([name,grade])
    s_name.append(name)
    s_grade.append(grade)

s_name.sort()
s_grade.sort()
print(s_name)
print(s_grade)

