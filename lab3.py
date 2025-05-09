# Explicația :
greet_user = lambda name: print('Salut,', name)
user_name = input("Introdu numele ")
greet_user(user_name)


#sarcina 2
lista = [(3, 11), (1, 7), (7, 8), (16, 88), (23, 15), (5, 2), (8, 10)]

# sortăm după al doilea element din fiecare tuplu
lista_sortata = sorted(lista, key=lambda x: x[1])

print(lista_sortata)



# Cu parametri:
def inmultire(a,b):
    return a * b
rezultat = inmultire(3,4)
print("Rezultatul:", rezultat)


#Cu valori predefinite:
def greet_default(name="anonim"):
    print("Bun venit,", name)

#Cu return:
def suma(a, b):
    return a + b

#Fără return (doar efect):
def produs(a, b):
    print("Produsul este:", a * b)

#Apelarea funcțiilor și explicație:
say_hello()  # apel fără parametri
greet("Sasha")  # apel cu parametru
print("Suma:", suma(4, 5))  # apel cu return
afiseaza_produs(3, 7)  # apel fără return

