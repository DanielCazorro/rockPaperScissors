# User Choices
INVALID_CHOICE = -1
PAPER = 0
ROCK = 1
SCISSORS = 2
QUIT = 3

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
    """
    Lee una selección del usuario (piedra, papel, tijera o salir) y la devuelve
    """
    user_choice = INVALID_CHOICE
    while user_choice == INVALID_CHOICE:
        print("Select one number: ")
        print(f"{PAPER}. Paper")
        print(f"{ROCK}. Rock")
        print(f"{SCISSORS}. Scissors")
        print("--------------------")
        print(f"{QUIT}. Quit the game")

        user_choice = int(input('Enter your choice: '))
        # Valido lo que me ha dicho
        if user_choice  in range(PAPER, QUIT + 1):
            break # Ok y continuamos
        else:
            user_choice = INVALID_CHOICE 

    return user_choice

def is_exit(user_choice):
    """
    Predicado que devuelve True si el usuario ha decidido para y False
    si quiere seguir jugando
    """
    return True

def generate_computer_choice():
    """
    Genera y devuelve una jugada al azar
    """
    return None

def evaluate_move(user_choice, comp_choice):
    """
    Compara lass dos jugadas y devuelve un texto con el resultado
    """
    return None

def print_result():
    """
    Imprime bonito el resultado
    """
    return None

if __name__ == "__main__":
    print("Rock-Paper-Scissors")
    game_loop()