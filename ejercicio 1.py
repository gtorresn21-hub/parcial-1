numero = int(input("ingrese un numero entero positivo: "))

if numero <= 0:
    print("debe ingresaer un numero positivo")

else:
    tabla_mas_larga = 0
    numero_tabla = 0

    for i in range(1, numero + 1):
    print("\ntabla del", i)
    contador = 0

    for j in range(1, 11)
     resultado = i * j
     print(i, "x", j, "=", resultado)

     contador = contador + 1

     if contador > tabla_mas_larga:
      tabla_mas_larga = contador
      numero_tabla = i

    print("\nla tabla mas larga fue la del numero: ", numero_tabla)    