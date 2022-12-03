import math


def discriminant(a, b, c):
    D = b**2 - 4*a*c
    try:
        x1 = (-b + math.sqrt(D)) / 2*a
        x2 = (-b - math.sqrt(D)) / 2 * a
        return x1, x2
    except ValueError:
        return 'Корней нет!'


if __name__ == '__main__':



    while True:
        try:
            
            a = int(input("Введите x^2 "))
            b = int(input("Введите x "))
            c = int(input("Введите число "))
            try:
                x1, x2 = discriminant(a, b, c)
                print(f'{x1}, {x2}')
            except ValueError:
                print('Отрицательный дискриминант')
        except ValueError:
            print('Ошибка ввода') 


        while True:
            try:
                continue_1 = int(input("Хотите ли вы продолжить. Если да, введите 0, если нет введите 1 "))
                if continue_1 == 0 or continue_1 == 1:
                    break
                else:
                    continue

            except ValueError:
                    print('Нельзя писать слова. Только цифры 0 или 1!')

        if continue_1 == 1:
            break
        if continue_1 == 0:
            continue


'''   formula = "x^2+x-1"
    if formula[0] != '-':
        formula = '+' + formula
    if formula[1] == 'x':
        formula = formula[0] + '1' + formula[1:]
    split_minus = formula.split('-')

    if split_minus[1] == 'x':
        split_minus[1] = '1' + split_minus[1]
    split_2 = formula.split('+')
    if split_2[0] == '+':
        split_2[0] = '1' + split_2[0]
    formula = '-'.join(split_minus)
    print(formula)
    print(split_minus)
    if '+' in formula:
        split_formula = formula.split('+')
    elif '+' in formula and '-' in formula:
        pass
    elif '-' in formula:
        split_formula = formula.split('-')
        split_formula[1].append('-')

    print(split_formula)
    # a = split_plus[0]
    # b = split_plus[1] '''
