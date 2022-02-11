troom, tcond = input('Введите желаемую температуру: ').split()
rules = input('Режим работы: ')

troom = int(troom)
tcond = int(tcond)

if 'freeze' in rules:
    if troom >= tcond:
        print(tcond)
    else:
        print(troom)

if 'heat' in rules:
    if troom <= tcond:
        print(tcond)
    else:
        print(troom)


if 'auto' in rules:
    print(tcond)

if 'fan' in rules:
    print(troom)

