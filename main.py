#1. ESCOGER las opciones en una funcion
#2. Apartar las reglas de la parte de quien gana o pierde

from pdb import run
import random



#JUEGO DE PIEDRA PAPEL O TIJERA POR CARLOS BEDON
print("BIENVENIDOS A MI JUEGO DE PIEDRA< PAPEL O TIJERA")


def choose_options():
    variables = ('piedra','papel','tijera')
    print('************************************************')
    usser = input('Selecciona 1-piedra, 2-papel o 3-tijera?  -->')
    #print('************************************************')
    usser = usser.lower()
    while not usser in variables:
        print('NO, NO, NO. Has selecionado una opcion no valida, favor intente de nuevo')
        usser = input('Selecciona piedra, papel o tijera?  -->')
        print('************************************************')
    computador = random.choice(variables)
    print("Usted ha selecionado {} ".format(usser))
    print("Computador ha seleecionado {} ".format(computador))
    return usser, computador

def rules_of_game(victorias=0,derrotas=0):
    usser, computador = choose_options() 
    if not usser == computador:
        
            if computador == 'piedra' and usser == 'papel':
                victorias += 1
                                
            elif computador == 'piedra' and usser == 'tijera':
                derrotas += 1
                
            elif computador == 'papel' and usser == 'piedra':
                derrotas += 1
                
            elif computador == 'papel' and usser == 'tijera':
                victorias += 1
                
            elif computador == 'tijera' and usser == 'papel':
                derrotas += 1
                
            elif computador == 'tijera' and usser == 'piedra':
                victorias += 1
    else: 
        print('Ha sido un empate por favor intenta de nuevo')
                
    return victorias, derrotas

def ganador(win,loose):
    if win == 2:
        print("FELICITACIONES HA GANADO")
    elif loose == 2:
        print("LO LAMENTO HAS PERDIDO, EL PC FUE MEJOR QUE TU")

def imprimir(contador_juegos,win,loose):
    print('ROUND #{}'.format(contador_juegos))
    print('VICTORIAS {} DERROTAS {}'.format(win,loose))
    print('----------------------------------------')

def run_game():
    contador_juegos = 1
    victorias = 0
    derrotas = 0
    win=0
    loose=0
    while win < 2 and loose < 2: 
        victorias,derrotas = rules_of_game()    
        if victorias == 1:
            win += 1
        elif derrotas == 1:
            loose += 1    
        contador_juegos += 1   
        imprimir(contador_juegos,win,loose)
        ganador(win,loose)

run_game()