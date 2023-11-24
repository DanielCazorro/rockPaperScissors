from enum import Enum
from random import choice

class GameChoice(Enum):
    INVALID = -1
    PAPER = 0
    ROCK = 1
    SCISSORS = 2
    QUIT = 3

def game_loop():
    """
    Bucle principal del juego
    """
    while True:
        user_choice = read_user_choice()
        if not is_exit(user_choice):
            comp_choice = generate_computer_choice()
            result = evaluate_move(user_choice, comp_choice)
            print_result(result)
        else:
            break

def read_user_choice():
    """
    Lee una selección del usuario (piedra, papel, tijera o salir) y la devuelve
    """
    user_choice = GameChoice.INVALID
    while user_choice == GameChoice.INVALID:
        print_menu()
        try:
            user_input = int(input('Enter your choice: '))
            user_choice = GameChoice(user_input)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

    return user_choice

def print_menu():
    """
    Muestra el menú de selección al usuario
    """
    print("Select one number: ")
    print(f'{GameChoice.PAPER.value}. Paper')
    print(f'{GameChoice.ROCK.value}. Rock')
    print(f'{GameChoice.SCISSORS.value}. Scissors')
    print(f'--------------------')
    print(f'{GameChoice.QUIT.value}. Quit the game')

def is_exit(user_choice):
    """
    Predicado que devuelve True si el usuario ha decidido parar y False
    si quiere seguir jugando
    """
    return user_choice == GameChoice.QUIT

def generate_computer_choice():
    """
    Genera y devuelve una jugada al azar
    """
    return choice([GameChoice.PAPER, GameChoice.ROCK, GameChoice.SCISSORS])

def evaluate_move(user_choice, comp_choice):
    """
    Compara las dos jugadas y devuelve un texto con el resultado
    """
    assert user_choice != GameChoice.INVALID and user_choice != GameChoice.QUIT
    assert comp_choice != GameChoice.INVALID and comp_choice != GameChoice.QUIT

    result = ''

    if user_choice == GameChoice.PAPER:
        if comp_choice == GameChoice.PAPER:
            result = "It's a tie!"
        elif comp_choice == GameChoice.ROCK:
            result = 'You win! Paper covers Rock'
        else:
            result = "I win! Scissors cut paper"

    elif user_choice == GameChoice.ROCK:
        if comp_choice == GameChoice.ROCK:
            result = "It's a tie!"
        elif comp_choice == GameChoice.PAPER:
            result = 'I win! Paper covers Rock'
        else:
            result = "You win! Rock smashes Scissors"


    else:
        # Scissors
        if comp_choice == GameChoice.SCISSORS:
            result = "It's a tie!"
        elif comp_choice == GameChoice.PAPER:
            result = 'You win! Scissors cut Paper'
        else:
            # Rock
            result = "I win! Rock smashes Scissors"



    return result

def print_result(result):
    """
    Imprime bonito el resultado
    """
    print('\n\n--------------------')
    print('Game Over!')
    print(result)
    print('--------------------\n\n')

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