a = int(input())
b = int(input())
c = int(input())

num = [a, b, c]
max = max(num)
one = []


if sum(num) != 0:
    if a == b == c:
        print('YES')
    else:
        for i in num:
            if i != max:
                one.append(i)
            else:
                max = i

        if sum(one) > max:
            print('YES')
        else:
            print('NO')
else:
    print('NO')