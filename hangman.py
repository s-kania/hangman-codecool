import random, os , time

game_time = 0
health = 6


def score(time,attemps,city):
    score = (city * 200) + 1100 - (time*4.25) - (attemps*95.75)
    return score

def hang_animation(health):
    scene = open("end_scene.txt", "r")
    for x, line in enumerate(scene):
        if x < 25 and health == 0:
            print(line, end="")
        elif x >= 29 and x <= 53 and health == 1:
            print(line, end="")
        elif x >= 59 and x <= 83 and health == 2:
            print(line, end="")
        elif x >= 89 and x <= 113 and health == 3:
            print(line, end="")
        elif x >= 119 and x <= 143 and health == 4:
            print(line, end="")
        elif x >= 149 and x <= 173 and health == 5:
            print(line, end="")
        elif x >= 179 and x <= 204 and health == 6:
            print(line, end="")
        else:
            pass
    scene.close()



def fun_win(attemps,capital):
    global game_time
    os.system('clear')
    game_time = time.time() - game_time

    print("\n\n************************\nCongratulations you won!\n************************\n\n")
    print("You guessed after %d attemps. It took you %d seconds. Your score: %d" %(attemps,game_time,score(game_time,attemps,len(capital)) ))
    input("Click Enter to continue") #wraca do menu
    os.system('clear')
    return

def fun_lose(attemps):
    global game_time
    os.system('clear')
    game_time = time.time() - game_time
    print("\n***************************\n")
    hang_animation(0)
    print("\n**************************\nCongratulations you lose!\n**************************\n\n")
    print("You not guessed after %d attemps. It took you %d seconds." %(attemps,game_time))
    input("Click Enter to continue") #wraca do menu
    os.system('clear')
    return


def fun_play(country,capital,capitaldash):
    """Gameplay"""
    badletters = []
    attemps = 0
    global health

    while True:
        os.system('clear')
        print("\n***************************\n")
        hang_animation(health)
        print("\n***************************\nTell me what is capital city of ",country,"?")
        print("Length of word ",len(capitaldash)," Word:",capitaldash)
        print("\nMisses ",",".join(badletters))
        userinput = input("\nEnter letter or word: ")
        userinput = userinput.upper()

        if len(userinput) > 1:
            if userinput == capital:
                attemps += 1
                fun_win(attemps,capital) #wygrana po calym zdaniu
                break
            else:
                badletters.append(userinput)
                health -= 2
                print("\nBad! You lose one life")
        else:
            attemps += 1
            if userinput in capital:
                for x in range(len(capital)):
                    if capital[x] == userinput:
                        capitaldash = capitaldash[:x] + userinput + capitaldash[x+1:]
                if capital == capitaldash: #wygrana po literkach
                    fun_win(attemps,capital)
                    break
                print("\nGood!")
            else:
                badletters.append(userinput)
                health -= 1
                print("\nBad! You lose one life")
        if health <= 0:
            #time.sleep(1)
            fun_lose(attemps)
            break

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
    global game_time
    global health
    os.system('clear')
    print("Welcome in HANGMAN game!")

    while True:
        print("\n*************************\nMenu:\n1: Play game\n2: View Leaderboards\n3: Quit\n*************************")
        picked = input("You pick: ")

        if picked == "1":
            health = 6
            game_time = time.time()
            fun_initplay()
        elif picked == "2":
            fun_leaderboards()
        elif picked == "3":
            print("Goodbye!")
            break
        else:
            os.system('clear')
            print("\nWrong command")


if __name__ == "__main__":
    main()
