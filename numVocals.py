palabra = input("Ingresa una palabra y te dire cuantas volales tiene")
vo = ['a','e','i','o','u']
count = 0
for l in palabra:
    if l in vo:
        count += 1
print("Número de vocales:", count)
