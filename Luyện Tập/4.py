s = input('Nhap chuoi')

upper = 0
lower = 0
digit = 0
special = 0
space = 0
vowel = 0
consonant = 0

vowels = "aeiouAEIOU"

for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

    if i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    elif not i.isalnum(): #Kí tự đặc biệt - Gen code ( đoạn này em không nhớ ạ...)
        special += 1

    if i.isalpha(): #Gen code ( đoạn này em không nhớ ạ ...)
        if i in vowels:
            vowel += 1
        else:
            consonant += 1

print("Chữ in hoa:", upper)
print("Chữ in thường:", lower)
print("Chữ số:", digit)
print("Ký tự đặc biệt:", special)
print("Khoảng trắng:", space)
print("Nguyên âm:", vowel)
print("Phụ âm:", consonant)