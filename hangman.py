def fun_play():
    return


def fun_leaderboards():
    return


def main():
    print("Welcome in HANGMAN game!")

    while True:
        print("\nMenu:\n1: Play game\n2: View Leaderboards\n3: Quit")
        picked = input("You pick: ")

        if picked == "1":
            fun_play()
        elif picked == "2":
            fun_leaderboards()
        elif picked == "3":
            print("Goodbye!")
            break
        else:
            print("\nWrong command")



if __name__ == "__main__":
    main()
