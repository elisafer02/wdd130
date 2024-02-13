import random 

listado = ['computadora','programador', 'python', 'javascript', 'nodejs']
clave = random.choice(listado)

intentos = int (len(clave))
while intentos != 0:
    print (intentos)
    intentos -= 1