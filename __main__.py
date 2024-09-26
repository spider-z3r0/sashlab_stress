from .attention import attention_check
from .clear_prompt import clear_terminal
from .trial import trial
import keyboard as kb
import pandas as pd
import time
import winsound
from .Partitpant import Participant, MakeParticipant
from .difficulty_manager import DifficultyManager


def main():
    clear_terminal()
    print("Session set up:")
    participant: Participant = MakeParticipant()

    attention_counter = 0
    while not attention_check() and attention_counter < 5:
        attention_counter += 1
        if attention_counter >= 5:
            print("You have failed the attention check too many times")
            # print("\a")
            time.sleep(1)
            winsound.Beep(880, 2200)
            break

    participant.set_attention_fails(attention_counter)

    print(f"Partitipant id = {participant.id}")
    print(f"Attenttion failures = {participant.attention_fails}")

    print(
        """
        In the next section subtraction problems will appear on screen. Please solve the problem by entering your answer to the problem and then pressing enter. Ensure to only enter numeric characters.\n

        Press the Spacebar when you're ready to continue
        """
    )

    kb.wait(hotkey="spacebar")
    participant.set_start_time()
    clear_terminal()

    d = DifficultyManager()
    round = 1

    while True:
        try:
            print(f"You are playing at difficulty level {d.get_difficulty()-1}")

            answer = trial(d.get_difficulty())
            print(answer)
            d.update_streaks(answer)
            d.update_difficulty()
        except KeyboardInterrupt:
            print("Finished testing")
            break

if __name__ == "__main__":
    main()
