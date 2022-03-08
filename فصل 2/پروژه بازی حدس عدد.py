import random
a = 1
b = 99
hads = random.randint(a, b)
print(hads)
javab = input()

while javab != "d":
    if javab == "b" :
        a = hads
        hads = random.randint(a, b)
        print(hads)
        javab = input()
    else:
        b = hads
        hads = random.randint(a, b)
        print(hads)
        javab = input()

print("terekondi")