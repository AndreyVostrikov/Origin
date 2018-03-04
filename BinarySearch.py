lst = [0, 3, 5, 7, 10, 20, 28, 30, 45, 56]
n = 56
i = 0
j = len(lst) - 1
m = int(j / 2)
while lst[m] != n and i < j:
    if n > lst[m]:
        i = m + 1
    else:
        j = m - 1
    m = int((i + j) / 2)
if i > j:
    print('Элемент не найден')
else:
    print(m)