from .make_number import make_number

def main():
    print("lets run a trial")
    print(trial())


def trial(difficulty: int = 2) -> bool:
    if difficulty < 2:
        raise ValueError("Difficulty must be greater than 2")
    x_val = make_number(difficulty)
    y_val = make_number(difficulty-1)

    answered = False
    
    while not answered:
        try:
            answer = int(input(f"Please solve {x_val} - {y_val}: \n"))
            answered = True
        except ValueError as e:
            print("Please only type Numeric characters: ie '4'")

    return answer == x_val - y_val

if __name__ == '__main__':
    main()
