import time

start = int(input('开始：'))
end = int(input('结束：'))
step = int(input('步长：'))

for count in range(start, end, step):
    print(f'count:{count}', end=' ')
    time.sleep(1)
print()
