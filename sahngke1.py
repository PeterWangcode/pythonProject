tensu = []
number = 0

while True:
    s = input(f'第{number + 1}名学生的成绩：')
    if s == 'End': break
    tensu.append(int(s))
    number += 1

minimum = maximum = tensu[0]
for i in range(1, number):
    if minimum < tensu[i]: minimum = tensu[i]
    if maximum > tensu[i]: minimum = tensu[i]

total = sum(tensu)

print(f'总分为：{total}')
print(f'平均分：{total / number}')

print(f'最高分：{maximum}')
print(f'最低分：{minimum}')
