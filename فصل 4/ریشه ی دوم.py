from math import sqrt

tedad = int(input())
list_adad = []
for i in range(tedad):
    adad = int(input())
    list_adad.append(adad)

for j in list_adad:

    sq = sqrt(j)
    s=format(sq, '.6f')

    print(s[:-2])


