from enum import Enum

class UserChoice(Enum):
    # User Choices
    INVALID = -1
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
    user_choice = UserChoice.INVALID
    while user_choice == UserChoice.INVALID:
        print("Select one number: ")
        print(f"{UserChoice.PAPER}. Paper")
        print(f"{UserChoice.ROCK}. Rock")
        print(f"{UserChoice.SCISSORS}. Scissors")
        print("--------------------")
        print(f"{UserChoice.QUIT}. Quit the game")

        # Compruebo que los datos son correctos
        try:
            user_choice = int(input('Enter your choice: '))
        except ValueError:
            user_choice = UserChoice.INVALID # Si no lo son, vuelvo al menú

        # Valido lo que me ha dicho
        if user_choice  != UserChoice.INVALID:
            break # Ok y continuamos
        else:
            user_choice = UserChoice.INVALID 

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

def log_error(error):
    """
    Guarda los datos del error en Crashlytics
    """
    print(error)

if __name__ == "__main__":
    print("Rock-Paper-Scissors")
    try:
        game_loop()
    except Exception as error:
        log_error(error)

