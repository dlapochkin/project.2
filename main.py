"""
Project 2
Developer: Lapochkin D.
"""
import fractions


def main():
    """
    Main function
    :return: None
    """
    vectors = pool()
    basis = magic(vectors)
    output(basis)


def if_numbers(x):
    """
    Checks whether vector's coordinates are numbers
    :param x: vector
    :return: 1 as True and 0 as False
    """
    for ltr in x:
        if not (ltr == '(' or ltr == ')' or ltr == ',' or ltr == ' ' or ltr.isdigit() or ltr == '-' or ltr == '/' or ltr == '.'):
            return 0
    return 1


def fraction_extending(x):
    """
    Extends a vector with rational fractions coordinates in order to gain integer numbers
    :param x: extendable vector
    :return: extended vector
    """
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
            if max_divisor % divisor == 0:
                i += 1
        if i == len(divisors):
            sup = max_divisor
            break
        max_divisor += 1
    new_x_coordinates = []
    for coordinate in x_coordinates:
        c_find = coordinate.find('/')
        if c_find != -1:
            new_coordinate = int((float(coordinate[:c_find])/float(coordinate[c_find+1:]))*sup)
            new_x_coordinates.append(new_coordinate)
        else:
            new_x_coordinates.append(int(coordinate)*sup)
    y = '('
    for coordinate in new_x_coordinates:
        y += str(coordinate) + ','
    return y[:-1] + ')'


def decimal_extending(x):
    """
    Extends a vector with decimal fractions coordinates in order to gain integer numbers
    :param x: extendable vector
    :return: extended vector
    """
    quantity = []
    x_coordinates = x[1:-1].split(',')
    for coordinate in x_coordinates:
        if coordinate.find('.') != -1:
            n = len(coordinate[coordinate.find('.')+1:])
            quantity.append(n)
    n = max(quantity)
    y = '('
    for coordinate in x_coordinates:
        y += str(int(float(coordinate) * (10 ** n))) + ','
    return y[:-1] + ')'


def pool():
    """
    Creates vector pool
    :return: vector pool
    """
    vectors = []
    x = input('Введите первый вектор системы, его размерность будет определяющей:\n')
    dimension_x = x.count(',') + 1
    while True:
        if x == '':
            break
        elif if_numbers(x) == 0 or x[0] != '(' or x[-1] != ')':
            print('Повторите попытку: ошибка ввода')
        elif x.count(',') + 1 != dimension_x:
            print('Повторите попытку: векторы не могут иметь разную размерность.')
        else:
            if x.find('/') != -1:
                x = fraction_extending(x)
            if x.find('.') != -1:
                x = decimal_extending(x)
            vector = x.replace(' ', '')
            check = vector[:-1] + ','
            if check.count('0,') == dimension_x:
                print('Повторите попытку: введен нулевой вектор.')
            else:
                vectors.append(vector)
        x = input()
    return vectors


def vector_difference(x, y):
    """
    Vector subtraction operation
    :param x: decreasing vector
    :param y: subtracted vector
    :return: result of a subtraction
    """
    result = '('
    x_coordinates = x[1:-1].split(',')
    y_coordinates = y[1:-1].split(',')
    for n in range(len(x_coordinates)):
        result += str(fractions.Fraction(x_coordinates[n]) - fractions.Fraction(y_coordinates[n])) + ','
    return result[:-1] + ')'


def multiplication(scalar, x):
    """
    Operation of multiplication of a vector by a scalar number
    :param scalar: scalar number
    :param x: vector being multiplied
    :return: multiplied vector
    """
    coordinates = x[1:-1].split(',')
    out = '('
    for coordinate in coordinates:
        out += str(fractions.Fraction(scalar) * fractions.Fraction(coordinate)) + ','
    return out[:-1] + ')'


def scalar_multiplication(x, y):
    """
    Scalar multiplication operation (between vectors)
    :param x: first vector
    :param y: second vector
    :return: result
    """
    result = 0
    x_coordinates = x[1:-1].split(',')
    y_coordinates = y[1:-1].split(',')
    for n in range(len(x_coordinates)):
        result += fractions.Fraction(x_coordinates[n]) * fractions.Fraction(y_coordinates[n])
    return result


def projection(x, y):
    """
    The operator of the projection of a vector x onto a vector y
    :param x: vector x
    :param y: vector y
    :return: projection of a vector x onto a vector y
    """
    return multiplication(str(fractions.Fraction(scalar_multiplication(x, y), scalar_multiplication(y, y))), y)


def process(x, basis):
    """
    Gram–Schmidt process
    :param x: vector being orthogonalized
    :param basis: orthogonal vector system
    :return: orthogonalized vector
    """
    in_work = x
    for second_layer in range(len(basis)):
        in_work = vector_difference(in_work, projection(x, basis[second_layer]))
    return in_work


def magic(vectors):
    """
    Orthogonalizes vectors
    Hogwarts' strongest spell (•◡•)
    :param vectors: vectors being orthogonalized
    :return: orthogonalized basis
    """
    basis = [vectors[0]]
    for first_layer in range(1, len(vectors)):
        x = vectors[first_layer]
        y = process(x, basis)
        check = y[:-1] + ','
        if check.count('0,') != check.count(','):
            if y.find('/') != -1:
                basis.append(fraction_extending(y))
            else:
                basis.append(y)
    return basis


def output(basis):
    """
    Prints orthogonalized basis
    :param basis: basis
    :return: None
    """
    print('Ортогональный базис подпространства:')
    for item in basis:
        item = item.replace(',', ', ')
        print(item)


main()
