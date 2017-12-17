# Działania na wielomianach
# Wielomian jest słownikiem, którego klucze (n) to wykładniki,
# a elementy (xn_factor) to czynniki, np. {3:3.5, 0:3} to 3.5x3 + 3
# wielomian jest wprowadzany w postaci tekstowej (np. x2 - 3x + 4)*(x2 - 2)
# i jest zamieniany na postać wewnętrzną przez analizator składniowy
# zbudowany przy użyciu modułu ply (Python Lex Yacc)

from pzParseWielomian import *
from math import sqrt

while True:
    try:
        s = input("Wprowadź wyrażenie wielomianowe: ") # np. 5x2 - 6x + 5*(2x - 3x2)
        if not s: continue
        w = parse_wielomian(s)
        w_exponents = set(w.keys())
        if (2 not in w_exponents) or not (w_exponents <= {2, 1, 0}):
            print("To nie jest trójmian kwadratowy")
            continue

        a = w.get(2, 0)
        b = w.get(1, 0)
        c = w.get(0, 0)

        delta = b*b - 4*a*c
        print("Delta = ", delta)
        if delta == 0:
            x1 = -b / (2*a)
            print("Równanie ma jeden pierwiastek równy ", x1)
        elif delta > 0:
            deltaRoot = sqrt(delta)
            x1 = round((-b - deltaRoot)/(2*a), 2)
            x2 = round((-b + deltaRoot)/(2*a), 2)
            print("Równanie ma dwa pierwiastki: ", x1, "oraz ", x2)
        else:
            print("Delta mniejsza od 0, równanie nie ma pierwiastków")
    except ZeroDivisionError:
        print("Nie wolno dzielić przez zero!")
    except EOFError:
        break
    except ValueError:
        print("Ops... spróbuj jeszcze raz")
    except KeyboardInterrupt:
        print("Przerwano działanie programu")
        break
    

