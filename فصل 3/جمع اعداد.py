text = input()
yek = text.count('1')
do = text.count('2')
se = text.count('3')
yeks=''
dos=''
ses=''
for i in range(yek):
    yeks += "1+"
for j in range(do):
    dos += "2+"
for z in range(se):
    ses += "3+"
final=(yeks + dos + ses)
print(final[:-1])