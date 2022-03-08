sen = int(input())
bozogtarin_sen = 0
bozogtarin_sen_2 = 0

while sen != -1:
    if sen > bozogtarin_sen:
        bozogtarin_sen_2 = bozogtarin_sen
        bozogtarin_sen = sen
    elif sen < bozogtarin_sen and sen > bozogtarin_sen_2:
        bozogtarin_sen_2 = sen
        
    sen = int(input())

print(bozogtarin_sen ," " ,bozogtarin_sen_2)
