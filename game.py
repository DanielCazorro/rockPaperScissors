

def game_loop():

    while True:
        # Leo la selección del usuario (piedra, papel, tijera o parar el juego)
        user_choice = read_user_choice()
        # Siempre y cuando no quiera parar
        if not is_exit(user_choice):
            # Genero una jugada del ordenador
            comp_choice = generate_computer_choice()
            # Evalúo la jugada
            result = evaluate_move(user_choice, comp_choice)
            # Muestro el ganador en pantalla y vuelta al principio
            print_result(result)
        else:
            # El humano quiere parar
            break

def read_user_choice():
    pass

def is_exit():
    pass

def generate_computer_choice():
    pass

def evaluate_move():
    pass

def print_result():
    pass