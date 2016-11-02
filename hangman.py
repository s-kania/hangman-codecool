import random



def fun_play():
    """Gameplay"""
    country_capital = fun_loadcountries()
    capitaldash = []

    #dzielenie country_capital na dwie zmienne
    for x in range(0, len(country_capital) ):
        if country_capital[x] == "|":
            country = country_capital[:x-1]
            capital = country_capital[x+2:len(country_capital)-1]
            capital = capital.upper()
            capitaldash = capital[:]
            break

    #zmienna capitaldash zamienia sie na "_"
    for i in range(0,len(capitaldash)):
        if capitaldash[i] != " ":
            capitaldash = capitaldash[:i] + '_' + capitaldash[i+1:]


    print(capital," length ", len(capital))
    print(capitaldash," length ", len(capitaldash))

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
