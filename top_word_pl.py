#Pyta o nazwę pliku
fname = input("Enter file: ")
#Jeśli nazwa pliku nie spełnia warunku wybiera plik domyślny
if len(fname) < 1 : fname = "words.txt"
#Wczytuje plik
fhand = open(fname)

#Włączenie słownika, który służy do przechowywania wartości danych w parach klucz:wartość.
many = dict()

#Wycięcie zbędnych znaków końcowych i podział wyrazów
for line in fhand :
    line = line.rstrip()
    wds = line.split()
    
    #Zwraca wartość elementu o określonym kluczu
    for w in wds:
        many[w] = many.get(w, 0) + 1
        
#Zaczyna od stanów pustych
largest = None
bigword = None

#Znajduje najczęsciej powtarzające się słowo i wypisuje jego częstotliwość
for key, value in many.items() :
    if largest is None or value > largest :
        largest = value
        bigword = key
print(bigword, largest)