# funciones en python
#def name_function(params):
#   codigo
#   return

#funcion sin parametros y sin retornos 
def saludos():
    print("hola a todos")

saludos()

# funciones con 1 parametro
def get_age_in_future(age):
    print(f"en 3 años tendras {age} años" )

    get_age_in_future(39)

#funciones con 2 parametros sin retorno
def suma(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")

suma(12,35)

#funciones con parametro opcionales
def get_heroes(h1 ="Batman", h2 = "Superman"):
    print(h1, h2)

get_heroes()
get_heroes("ironman")
get_heroes("ironman", "flash")
get_heroes(h2="ironman", h1="flash")

#funciones con retorno
def title(texto):
    return texto.title()

text_changed = title ("HoLa A tOdOs")
print(text_changed)


