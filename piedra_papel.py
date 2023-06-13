# eleccion aleatoria maq
import random

# function randint(min,max)
rand_int =random.randint (1,3)
if rand_int ==1:
    choice_maq = 'piedra'
elif rand_int ==2:
    choice_maq = 'papel'
else:
    choice_maq = 'tijeras'

#eleccion usuario
choice_text = '''
escribe una de las opciones:
    piedra
    papel
    tijeras
'''
choice_user = input (choice_text)

#impresion de opciones
print('usuario eligio ->', choice_user)
print('maquina eligio ->', choice_maq)

#ganador!
if choice_maq == choice_user:
    print ("es un empate")
else:
    if choice_maq== 'piedra' and choice_user == 'papel':
        print('gana usuario')
    elif choice_maq == 'piedra' and choice_user == 'tijeras':
        print ('gana maquina')
    elif choice_maq == 'papel' and choice_user == 'tijeras':
        print ('gana usuario')
    elif choice_maq == 'papel' and choice_user == 'priedra':
        print ('gana maquina')
    elif choice_maq == 'tijeras' and choice_user == 'piedra':
        print ('gana usuario')
    else:
        print('gana maquina')

