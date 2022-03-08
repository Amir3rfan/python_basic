text = input()
a1 = text.find('h')
a2 = text.find('e',a1+1)
a3 = text.find('l',a2+1)
a4 = text.find('l',a3+1)
a5 = text.find('o',a4+1)

if a1<a2<a3<a4<a5:
    print('YES')
else:
    print('NO')