from multiprocessing import Pool
zakres = int(input("Wprowadz zakres szulania liczb pierwszych: "))
def czy_liczba_pierwsza(liczba):
	liczba = int(liczba) #zapewnieamy ze liczba zawsze bedzie naturalna

	#sprawdzamy czy nie jest parzysta true == nieparzysta false == parzysta
	warunek1 = True
	if liczba > 2:
		warunek1 = liczba % 2 
		if warunek1 > 0:
			warunek1 = True
		else:
			warunek1 = False

	#spradzamy czy jest podzielna przez cokolwiek miedzy soba a 1 bez reszty
	warunek2 = 0 #predeffiniujemy zeby zeminna byla dioczna poza scopem fora
	for	x in range(1,liczba): #domyslny krok 1 styka
		if (liczba % x) == 0:
			warunek2 += 1 
		if x < liczba and warunek2 > 1 :	#konczymy po pierwszej wtopie, nie sprawdzamy wszystkich dzielnikow do konca
			warunek2 = False
			break
		else:
			warunek2 = True

	return bool(warunek1 * warunek2)

if __name__ == '__main__':
	with Pool() as pool:				#v nie dawac _unordered bo warunki wewnatrz fora nie sprawdza w kolejnosci wtedy
		for i, wynik in enumerate(pool.imap(czy_liczba_pierwsza, range(zakres))):
			if wynik == True:
				print(str(i) + ' -> ' + str(wynik))
#sprawdzenie ze stronka https://www.numberempire.com/primenumbers.php dla 201517 