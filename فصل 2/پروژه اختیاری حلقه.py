adad = 0
count = 0
jame_adad = 0

while adad != -1:
    adad = int(input('adad : '))
    if adad != -1:
        jame_adad = jame_adad + adad
        count += 1
        print(jame_adad , ' va ' , count)
    else: break

print(jame_adad/count)
