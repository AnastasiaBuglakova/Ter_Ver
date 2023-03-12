# 1 Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.

def fact(num):
    if num == 0 or num == 1: return 1
    return fact(num-1) * num
def sochetanie(num1, num2):
    return fact(num1) / (fact(num2) * fact(num1 - num2))

# b = 52
# c = b/4
# hand = 4
# m = sochetanie(c,hand)
# print(m)
#
# n = sochetanie(b,hand)
# print(n)
# p_vse_kresty = m/n
# print(p_vse_kresty)

# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
# b = 52
# c = b/4
# hand = 4
# # один туз и 3 не туза
# m1 = sochetanie(4, 1)*sochetanie(4, 3)
# print(m1)
# # два туза и 2 не туза
# m2 = sochetanie(4, 2)*sochetanie(4, 2)
# print(m2)
# # три туза и 1 не туз
# m3 = sochetanie(4, 3)*sochetanie(4, 1)
# print(m3)
# # 4 туза
# m4 = sochetanie(4, 4)
# print(m4)
# m = m1+m2+m3+m4
# print(m)
#
# n = sochetanie(b,hand)
# print(n)
# p_vse_kresty = m/n
# print(p_vse_kresty)





# 2 На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
# Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек, не знающий код,
# откроет дверь с первой попытки?
# m = 1
# n = sochetanie(10,3)
# p = m/n
# print(p)




# 3 В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?
# parts =15
# painted = 9
# hand = 3
# m = sochetanie(9,3)
# n=sochetanie(15,3)
# p = m/n
# print(p)






# 4 В лотерее 100 билетов. Из них 2 выигрышных.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
loto = 100
win = 2
hand = 2
m = sochetanie(win, hand)
print(m)
n = sochetanie(loto, win)
print(n)
p = m / n
print(p)

