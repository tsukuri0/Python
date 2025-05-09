nume = input("Introduceți numele dvs.: ")
print("Salut, " + nume + "!")

#sarcina 2
numar_intreg = 42  # valoare int
numar_real = 3.14  # valoare  (float)
text_scurt = "Text scurt!"  # Valoare text 
text_lung = """Un text mai,
mai lung pe 
citeva rinduri
in Python"""  # text pe 3-4 rinduri

# se afiseaza valorile

print(numar_intreg)
print(numar_real)
print(text_scurt)
print(text_lung)

#sarcina 3
print(type(numar_intreg))  # tipul variabilei 
print(type(text_scurt))    
a = type(numar_intreg)
print (a) 


#sarcina 4
print(len(text_scurt))  # arata lungimea sirului de text 
print(len(text_lung))

#sarcina 5
r = text_scurt.upper()
print(r)  # caps text
print(text_scurt)
print(text_lung.upper())

#sarcina 6
subsir = text_scurt[0:3]  # Extragem primele 3 caractere din text_scurt
print(subsir)

sir = """A
B"""
print(len(sir))

subsir_lung = text_lung[10:20]  # extragem caracterele de la pozitia 10 la 19
print(subsir_lung)


i = 1
tip_i = type(i)
i = '123'
print(tip_i)


# a)
txt = "More results from text..."
substr = txt[4:12]
txt = "AAAAAAAAAAAAAAAAAAAAAAAAAAA"
print(substr)
print(substr.strip()) 
# b)
txt = "More results from text..."
a = txt.split()
a.append('789')
t = type(a)
print(a)
# c)
age = 36
txt = "My name is Mary, and I am {}"
print(txt.format(age))