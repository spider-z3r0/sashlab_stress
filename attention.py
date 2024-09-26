import random as ra


def main():
    check = attention_check()
    print(check)


def attention_check() -> bool:

    try:
        answer = int(
            input(f"To test your keyboard please solve the following sum 7 - 2: ")
        )
    except ValueError as e:
        print("Please make sure you enter a single numeric charachter")

    return answer == 7 - 2


if __name__ == "__main__":
    main()
