Program „pzWielomian.py” wykonuje działania na wielomianach, np.:

Wprowadz wyrażenie wielomianowe: (x2 + 3x +1)*(x-5)*(x2 - 4x +5)
Postać kanoniczna tego wielomianu: x5 - 6x4 - x3 + 41x2 - 50x - 25

Jeśli wprowadzony wielomian jest trójmianem kwadratowym, to program wylicza jego pierwiastki, np.:

	Wprowadz wyrażenie wielomianowe: x2 + 3x +1
	Postać kanoniczna tego wielomianu: x2 + 3x + 1
	Delta =  5.0
	Równanie ma dwa pierwiastki:  -2.62 oraz  -0.38

Program wykonuje także dzielenie wielomianów (operator „div”) oraz wyliczanie reszty z dzielenia (operator „mod”), np.:

Wprowadz wyrażenie wielomianowe: (x2 - 3x + 2) div (x -1)
Postać kanoniczna tego wielomianu: x - 2

Wprowadz wyrażenie wielomianowe: (x3 - 3x + 3) mod (x2 - 1)
Postać kanoniczna tego wielomianu: -2x + 3

Oprócz pliku „pzWielomian.py” program składa się także z analizatora składniowego i leksykalnego (plik „pzParseWielomian.py”) oraz modułu definiującego operacje na wielomianach (plik „pzPolinomialOperations”), a także standardowych modułów do tworzenia analizatorów leksykalnych i składniowych (ply - Python Lex Yacc) znajdujących się w katalogu „ply”.