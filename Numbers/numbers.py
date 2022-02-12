n = input()
num_1 = input()
num_2 = input()
num_3 = input()

k = [num_1, num_2, num_3]

if n[:2] != '+7' and n[0] != '8':
    n = '8' + n

n = n.replace('(', '').replace(')', '').replace('-', '').replace('+7', '8')

if len(n) < 11:
    n = n[0] + '495' + n[1:]

for i in range(len((k))):
    if k[i][:2] != '+7' and k[i][0] != '8':
        k[i] = '8' + k[i]

    k[i] = k[i].replace('(', '').replace(')', '').replace('-', '').replace('+7', '8')

    if len(k[i]) < 11:
        k[i] = k[i][0] + '495' + k[i][1:]

    if k[i] == n:
        print('YES')

    else:
        print('NO')