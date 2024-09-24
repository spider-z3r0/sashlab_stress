import time
import winsound
from .attention import attention_check
from .make_number import make_number
from .clear_prompt import clear_terminal
from .difficulty_manager import DifficultyManager
from .trial import trial
import keyboard as kb


def main():

    attention_counter = 0
    while not attention_check() and attention_counter < 5:
        attention_counter +=1
        if attention_counter >= 5:
            print("You have failed the attention check too many times")
            # print("\a")
            time.sleep(1)
            winsound.Beep(880, 2200)
            break

    clear_terminal()


    print("You have passed the attention check. Please press the spacebar when you are ready to continue")

    kb.wait(hotkey='spacebar')
    clear_terminal()



    d = DifficultyManager()

    print(f"You are playing at difficulty level {d.get_difficulty()-1}")

    trial(d.get_difficulty())


    

if __name__ == "__main__":
    main()
