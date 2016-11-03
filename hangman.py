import random, os

def fun_win():
    os.system('clear')
    print("\n\n************************\nCongratulations you won!\n************************\n\n")
    print()
    input("Click Enter to continue") #wraca do menu
    os.system('clear')
    return


def fun_play(country,capital,capitaldash):
    """Gameplay"""
    badletters = []

    while True:
        os.system('clear')
        print("\n***************************\nTell me what is capital city of ",country,"?")
        print("Length of word ",len(capitaldash)," Word:",capitaldash)
        print("\nMisses ",badletters)
        userinput = input("\nEnter letter or word ")
        userinput = userinput.upper()

        if len(userinput) > 1:
            if userinput == capital:
                fun_win() #wygrana po calym zdaniu
                break
            else:
                badletters.append(userinput)
                print("\nBad! You lose one life")
        else:
            if userinput in capital:
                for x in range(len(capital)):
                    if capital[x] == userinput:
                        capitaldash = capitaldash[:x] + userinput + capitaldash[x+1:]
                if capital == capitaldash: #wygrana po literkach
                    fun_win()
                    break
                print("\nGood!")
            else:
                badletters.append(userinput)
                print("\nBad! You lose one life")

    return

def fun_initplay():
    """Init Gameplay"""
    country_capital = fun_loadcountries()
    capitaldash = []
    #dzielenie country_capital na dwie zmienne
    for x in range(len(country_capital)):
        if country_capital[x] == "|":
            country = country_capital[:x-1]
            capital = country_capital[x+2:len(country_capital)-1]
            capital = capital.upper()
            capitaldash = capital[:]
            break
    #zmienna capitaldash zamienia sie na "_"
    for i in range(len(capitaldash)):
        if capitaldash[i] != " ":
            capitaldash = capitaldash[:i] + '_' + capitaldash[i+1:]

    #uruchomienie rozgrywki
    fun_play(country,capital,capitaldash)
    return


def fun_leaderboards():
    return


def fun_loadcountries():
    """Loading all contries and return random one"""
    countries_file = open("countries_and_capitals.txt", "r")
    countries_array = countries_file.readlines()
    countries_file.close()

    return countries_array[random.randrange(0, len(countries_array) - 1 )]
    #zwraca losowe panstwo i jego stolice


#dziala
def main():
    os.system('clear')
    print("Welcome in HANGMAN game!")

    while True:
        print("\n*************************\nMenu:\n1: Play game\n2: View Leaderboards\n3: Quit\n*************************")
        picked = input("You pick: ")

        if picked == "1":
            fun_initplay()
        elif picked == "2":
            fun_leaderboards()
        elif picked == "3":
            print("Goodbye!")
            break
        else:
            print("\nWrong command")


if __name__ == "__main__":
    main()
