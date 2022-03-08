emtiaz_kol = 0
bord = 0
for i in range(1,31):
    emtiaz = int(input())
    emtiaz_kol = emtiaz + emtiaz_kol
    if emtiaz == 3:
        bord += 1
print(emtiaz_kol, " ", bord)

