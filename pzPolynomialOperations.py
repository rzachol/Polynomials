# Działania na wielomianach
# Wielomian jest słownikiem, którego klucze (n) to wykładniki,
# a elementy (xn_factor) to czynniki, np. {3:3.5, 0:3} to 3.5x3 + 3

def calculate_poly(w, x):
    '''Wylicza wartość wielomianu "w" dla wartości "x"'''
    w_x = 0
    for i in set(w.keys()):
        w_x += x**i * w[i]
    return w_x

def negate_poly(w):
    '''zwraca -w'''
    result = {}
    for i in w.keys():
        result[i] = -w[i]
    return result

def multi_poly(w1, w2):
    '''mnoży przez siebie wielomiany "w1" i "w2"'''
    w3 = {}
    for i in w1.keys():
        for j in w2.keys():
            exponent = i + j
            factor = w1[i] * w2[j]
            if exponent in w3:
                w3[exponent] += factor
            else:
                w3[exponent] = factor
            if w3[exponent] == 0: del w3[exponent]
    return w3

def add_poly(w1, w2):
    '''dodaje wielomiany "w1" i "w2"'''
    w3 = w1
    w1_exponents = set(w1.keys())
    w2_exponents = set(w2.keys())
    for i in w2_exponents.difference(w1_exponents):
        w3[i] = w2[i]
    for i in w1_exponents.intersection(w2_exponents):
        w3[i] += w2[i]
        if w3[i] == 0: del w3[i]
    return w3

def subt_poly(w1, w2):
    '''odejmuje wielomiany "w1" i "w2"'''
    w3 = w1
    w1_exponents = set(w1.keys())
    w2_exponents = set(w2.keys())
    for i in w2_exponents.difference(w1_exponents):
        w3[i] = -w2[i]
    for i in w1_exponents.intersection(w2_exponents):
        w3[i] -= w2[i]
        if w3[i] == 0: del w3[i]
    return w3

def div_poly(w1, w2):
    '''zwraca wynik dzielenia "w1" przez "w2"'''
    w1_exponents = sorted(w1.keys(), reverse=True)
    w2_exponents = sorted(w2.keys(), reverse=True)
    if w2_exponents == []:
        raise ZeroDivisionError
    if w1_exponents < w2_exponents:     # e.g. (x2 + ...)/(x3 - ...)
        return {}
    else:                               # w1_exponents[0] >= w2_exponents[0]:
        result_highest_term = {w1_exponents[0] - w2_exponents[0] : w1[w1_exponents[0]] / w2[w2_exponents[0]]}
        return add_poly(result_highest_term, div_poly(subt_poly(w1, multi_poly(result_highest_term, w2)),w2))

def mod_poly(w1, w2):
    '''zwraca resztę z dzielenia "w1" przez "w2"'''
    if w2 == {}:
        raise ZeroDivisionError
    if w1 == {}:
        return w1
    w1_exponents = sorted(w1.keys(), reverse=True)
    w2_exponents = sorted(w2.keys(), reverse=True)
    if w1_exponents[0] < w2_exponents[0]:     # e.g. (x2 + ...)/(x3 - ...)
        return w1
    else:                               # w1_exponents[0] >= w2_exponents[0]:
        result_highest_term = {w1_exponents[0] - w2_exponents[0] : w1[w1_exponents[0]] / w2[w2_exponents[0]]}
        return mod_poly(subt_poly(w1, multi_poly(result_highest_term, w2)),w2)



def poly_term2string(n, xn_factor): # xn_factor*x^n
    '''zamienia składnik wielomianu na postać tekstową'''
    if xn_factor == 0:
        return ''
    if int(n) == n: n = int(n)      # get rid of trailing .0
    if int(xn_factor) == xn_factor: xn_factor = int(xn_factor)  # get rid of trailing .0
    str_xn_factor = str(xn_factor)
    if n != 0:
        if abs(xn_factor) != 1:
            string = str_xn_factor + 'x'
        elif xn_factor == -1:
            string = "-x"
        else:
            string = "x"
        if n != 1:
            string = string + str(n)
    else:
        string = str_xn_factor
    return string

def sign_spaced(x):
    if x < 0: return ' - '
    else: return ' + '

def print_poly(w):
    '''drukuje wielomian "w"'''
    if w == {}:
        print("0")
        return
    first_term = True
    for i in sorted(set(w.keys()), reverse=True):
        if first_term:
            print(poly_term2string(i, w[i]), sep='', end='')
            first_term = False
        else:
            print(sign_spaced(w[i]), poly_term2string(i, abs(w[i])),
                  sep='', end='')
    print()


class Wielomian:
    def __init__(self):
        self = {}
