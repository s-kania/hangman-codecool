import random



def fun_play():
    """Gameplay"""
    country_capital = fun_loadcountries()
    capitaldash = []
    badletters = []

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


    while True:
        print("\nTell me what is capital city of ",country,"?")
        print("Length of word ",len(capitaldash)," Word:",capitaldash)
        print("\nMisses ",badletters)
        userinput = input("\nEnter letter or word ")
        userinput = userinput.upper()

        if len(userinput) > 1:
            if userinput == capital:
                print("You win!")
                break
        else:
            for x in range(len(capital)):
               if capital[x] == userinput:
                   capitaldash = capitaldash[:x] + userinput + capitaldash[x+1:]
                   print("Good!")

        if userinput == "EXIT":
            break





    #print(capitaldash," length ", len(capitaldash))

    return


def fun_leaderboards():
    capital = 'ssasd'
    capitaldash = '_____'
    userinput = input('sd: ')
    for x in range(len(capital)):
       if capital[x] == userinput:
           capitaldash = capitaldash[:x] + userinput + capitaldash[x+1:]
    print(capitaldash)
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
