text = input()
k=0
b=0
for i in text:
    if i.islower():
        k += 1
    else:
        b += 1
if k>=b :
    print(text.lower())
else:
    print(text.upper())