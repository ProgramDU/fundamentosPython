#function input -> retorna string

num_a =("ingresa un numero: ")
num_b =("ingresa un numero: ")

print(num_a + num_b)

name = input ("ingresa tu nombre: ")
age = int(input("ingresa tu edad: "))
city = input("ingresa ciudad/pueblo: ")

# string format """ hola, soy name, tengo age años  vivo en city """
greeting =" hola, soy {}, tengo {} años y vivo en {}"
greeting.format(name, age, city)

print(greeting)

