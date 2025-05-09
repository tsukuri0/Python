# 1. Lucrul cu liste
lista = [1, 2, 3, 4, 5]  # 80
print("Lista originală:", lista)

# Afisarea primei și a treia valori
print("Prima valoare:", lista[0])
print("A treia valoare:", lista[2])

# inlocuirea unei valori
# lista[1] = 6
# print("Lista după înlocuire:", lista)

# Extractie  de la 1 la 3
sub_lista = lista[1:4]  # 90   [2,3,4]
sub_lista[0] = -1    # [-1,3,4]     80: [1,2,3,4,5]
print("Sub-lista extrasă:", sub_lista)


# Aplicare de 1 metoda 2 functii si 3 operatori:
lista.append(60)  # Metoda adauga un element la finalul listei
lungime = len(lista)  #  calculează lungime
suma = sum(lista)     # calculează suma elem

# Operatorii aritmetici
x = 10 + 20      #  adunare
y = 50 - 20      # scadere
z = 5 * 4      # inmultire
a = 10 / 3

print("Lista după append:", lista)
print("Lungimea listei:", lungime)
print("Suma elementelor din lista:", suma)
print(" operatori: adunare =", x, ", scadere =", y, ", inmultire =", z)

# 2. Lucrul cu tupluri
tuplu = (1, 2, 3, 4, 5)
print("\nTuplul definit:", tuplu)

# Afișarea tipului de date al tuplului
print("Tipul tuplului:", type(tuplu))

# Afisarea primei si ultimei valori
print("Prima valoare a tuplului:", tuplu[0])
print("Ultima valoare a tuplului:", tuplu[-1])

# Taietura (extractie): elementele de la indexul 1 la 3 (ultimul index exclus)
tuplu_slice = tuplu[1:4]
print("Sub-tuplul extras:", tuplu_slice)

# Aplicarea a 3 functii asupra elementelor tuplului
lungime_tuplu = len(tuplu)   # lungimea
valoare_max = max(tuplu)     # valoarea maxima
valoare_min = min(tuplu)     # valoarea minima
print("Lungimea tuplului:", lungime_tuplu)
print("Valoarea maxima din tuplu:", valoare_max)
print("Valoarea minima din tuplu:", valoare_min)

# 3. Lucrul cu multimi
# Valorile repetate vor fi eliminate automat intrun set.
set_elemente = {1, 2, 2, 3, 4, 4, 5, 10, 125, 1566}
print("\nSetul creat (elementele repetate sunt eliminate):", set_elemente)

# Aplicare de 1 metodă: adaugarea unui element nou in set
set_elemente.add(6)

# funcție: len() pentru a afla numărul de elemente
set_lungime = len(set_elemente)
print("Setul după adaugare:", set_elemente)
print("Numărul de elemente in set:", set_lungime)

# 4. Lucrul cu dictionare
# Dictionar tip text
dict_text = {"name" : "Alex", "age" : "21" , "height" : "175"}
# Dictionar cu chei numerice
dict_num = {1: "unu", 2: "doi", 3: "trei"}


# Aplicare de 2 metode:
chei = dict_text.keys()        # metoda keys returneaza toate cheile
valori = dict_text.values()     # metoda values returneaza toate valorile
print("Cheile din dict_text:", list(chei))
print("Valorile din dict_text:", list(valori))

# Aplicare de 2 funcții:
lungime_dict = len(dict_text)   # funcția len() pentru numarul de elemente
reprezentare_dict = str(dict_text)  # str pentru a converti dictionarul in sir
print("Lungimea dicționarului este", lungime_dict)
print("Reprezentarea dicționarului ca string:", reprezentare_dict)



# Sarcina 2: Lucrul cu input, format și operatorul "in"


# 1. Lista cu 3 elemente numerice si listă cu 3 denumiri de produse
l_preturi = [100, 200, 300]
l_produse = ["Produs A", "Produs B", "Produs C"]


print("\nInformații produse și prețuri:")
t = zip(l_produse, l_preturi)
l_preturi.append(400)
l_produse.append('hjbhj')
for produs, pret in t:
    mesaj = "Produsul {} costă {} lei.".format(produs, pret)
    print(mesaj)

# 2. Solicitarea vârstei utilizatorului, conversia și operații aritmetice
varsta_input = input("Introduceți vârsta dvs.: ")
varsta_int = int(varsta_input)
# Calcul: în 5 ani
varsta_viitoare = varsta_int + 5
# Folosind concatenarea și operatorii aritmetici
mesaj_varsta = "În 5 ani vei avea " + str(varsta_viitoare) + " ani."
print(mesaj_varsta)

# 3. Utilizarea operatorilor "in" și "not in"
lista_numere = [1, 2, 3, 4, 5]
if 3 in lista_numere:
    print("\nNumarul 3 este în lista", lista_numere)
else:
    print("Numarul 3 nu este în listă.")

if 10 not in lista_numere:
    print("Numarul 10 nu este în lista", lista_numere)
else:
    print("Numarul 10 este în listă.")