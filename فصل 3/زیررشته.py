text=input()
if len(text)>3:
    if text.startswith('AB') and text.endswith('BA'):
        print('YES')
    elif text.startswith('BA') and text.endswith('AB'):
        print('YES')
    else:
        print('NO')
else:
    print('NO')