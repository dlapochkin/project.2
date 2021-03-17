"""
Напишите программу, получающую на вход несколько векторов одной размерности и
строящую ортогональный базис подпространства, натянутого на данную систему векторов,
используя алгоритм Грама-Шмидта. Окончанием ввода будет считаться пустая строка.
"""


def if_numbers(s):
    for ltr in s:
        if not (ltr == '(' or ltr == ')' or ltr == ',' or ltr == ' ' or ltr.isdigit()):
            return 0
    return 1


def pool():
    vectors = []
    s = input()
    dimension_s = s.count(',') + 1
    while True:
        if s == '':
            break
        elif if_numbers(s) == 0:
            print('Вектор содержит нечисленные значения, попробуйте еще раз.')
        elif s.count(',') + 1 != dimension_s:
            print('Вектор имеет другую размерность, попробуйте еще раз.')
        else:
            vector = s.replace(' ', '')
            check = vector[:-1] + ','
            if check.count('0,') == dimension_s:
                print('Введен нулевой вектор, попробуйте еще раз.')
            else:
                vectors.append(vector)
        s = input()
    return vectors


def collector(basis=[]):
    vectors = pool()
    basis.append(vectors[0])
    for repeats in range(len(vectors)):
        i = 0
        if len(basis) == 0:
            basis.append(vectors[0])
        else:
            u = 1


print(pool())