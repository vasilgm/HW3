# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
#
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 (решить split)

a = list(input(''))
print(a)
set_1= list(set(a))
print(set_1)
for i in range(len(set_1)):
    w = 0
    for n in range(len(a)):
        if set_1[i] == a[n]:
            if w !=0:
                a[n] = f'{a[n]}_{w}'
            w += 1
print(" ".join(a))


# s = 'a a a b c a a d c d d'
# s = s.split()
# print(s)
# final_string = ''
# for i in range(len(s)):
#     if s[0:i].count(s[i]) == 0:
#         final_string += f' {s[i]}'
#     else:
#         final_string += f' {s[i]}_{s[0:i].count(s[i])}'
# print(final_string)