"""
Напишите программу, получающую на вход несколько векторов одной размерности и
строящую ортогональный базис подпространства, натянутого на данную систему векторов,
используя алгоритм Грама-Шмидта. Окончанием ввода будет считаться пустая строка.
"""


def main():
    vectors = pool()
    basis = magic(vectors)
    output(basis)


def if_numbers(s):
    for ltr in s:
        if not (ltr == '(' or ltr == ')' or ltr == ',' or ltr == ' ' or ltr.isdigit() or ltr == '-' or ltr == '/'):
            return 0
    return 1


def extending(x):
    divisors = []
    x_coordinates = x[1:-1].split(',')
    for coordinate in x_coordinates:
        if coordinate.find('/') != -1:
            divisor = int(coordinate[coordinate.find('/')+1:])
            divisors.append(divisor)
    max_divisor = max(divisors)
    while True:
        i = 0
        for divisor in divisors:
            if max_divisor % divisor != 0:
                break
            least_common_multiple = max_divisor
            i = 1
        if i == 1:
            break
        max_divisor += 1
    new_x_coordinates = []
    for coordinate in x_coordinates:
        if coordinate.find('/') != -1:
            new_coordinate = int(float(coordinate[:coordinate.find('/')])/float(coordinate[coordinate.find('/')+1:]))
            new_x_coordinates.append(new_coordinate*least_common_multiple)
        else:
            new_x_coordinates.append(coordinate*least_common_multiple)
    y = '('
    for coordinate in new_x_coordinates:
        y += str(coordinate) + ','
    return y[:-1] + ')'


def pool():
    vectors = []
    s = input('Введите первый вектор системы, его размерность будет определяющей:\n')
    dimension_s = s.count(',') + 1
    while True:
        if s == '':
            break
        elif s.count(',') + 1 != dimension_s:
            print('Повторите попытку: векторы не могут иметь разную размерность.')
        elif if_numbers(s) == 0:
            print('Повторите попытку: вектор содержит нечисленные значения.')
        elif s[0] != '(' or s[-1] != ')':
            print('Повторите попытку: ошибка в вводе')
        else:
            if s.find('/') != -1:
                s = extending(s)
            vector = s.replace(' ', '')
            check = vector[:-1] + ','
            if check.count('0,') == dimension_s:
                print('Повторите попытку: введен нулевой вектор.')
            else:
                vectors.append(vector)
        s = input()
    return vectors


def vector_difference(x, y):
    result = '('
    x_coordinates = x[1:-1].split(',')
    y_coordinates = y[1:-1].split(',')
    for n in range(len(x_coordinates)):
        result += str(int(x_coordinates[n]) - int(y_coordinates[n])) + ','
    return result[:-1] + ')'


def multiplication(scalar, vector):
    coordinates = vector[1:-1].split(',')
    out = '('
    for coordinate in coordinates:
        out += str(int(scalar) * int(coordinate)) + ','
    return out[:-1] + ')'


def scalar_multiplication(x, y):
    result = 0
    x_coordinates = x[1:-1].split(',')
    y_coordinates = y[1:-1].split(',')
    for n in range(len(x_coordinates)):
        result += int(x_coordinates[n]) * int(y_coordinates[n])
    return result


def projection(x, y):
    return multiplication((scalar_multiplication(x, y)/scalar_multiplication(y, y)), y)


def process(x, basis):
    in_work = x
    for second_layer in range(len(basis)):
        in_work = vector_difference(in_work, projection(x, basis[second_layer]))
    return in_work


def magic(vectors):
    basis = [vectors[0]]
    for first_layer in range(1, len(vectors)):
        x = vectors[first_layer]
        y = process(x, basis)
        check = y[:-1] + ','
        if check.count('0,') != check.count(','):
            basis.append(y)
    return basis


def output(basis):
    print('Ортогональный базис подпространства:')
    for item in basis:
        item = item.replace(',', ', ')
        print(item)


print(extending(input()))