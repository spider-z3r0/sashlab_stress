import random as ra

def main():
    check = attention_check()
    print(check)


def attention_check() -> bool:
    val_x = 10 - ra.randint(1,9)
    val_y = 10 -  ra.randint(1,9)

    try:
        answer = int(input(f"To test your keyboard please solve the following sum {val_x} - {val_y}:"))
    except ValueError as e:
        print(
            "Please make sure you enter a single numeric charachter"
            )

    return answer == val_x - val_y


if __name__ == '__main__':
    main()

