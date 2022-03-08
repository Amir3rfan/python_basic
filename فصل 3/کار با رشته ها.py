text = input()
new_text =''
for i in "aAuUiIeEoO":
    text = text.replace(i, "")
for j in text:
    new_text += "." + j
print(new_text.lower())