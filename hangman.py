import os
import random
import time
import sys
from termcolor import colored, cprint


from ast import literal_eval

game_time = 0
health = 6
high_score_list = []


def load_list():
    """Loading highscore list"""
    global high_score_list
    score_file = open('score.txt', 'r')
    high_score_list = [list(literal_eval(line)) for line in score_file]
    score_file.close()


def save_list():
    """Saving highscore list"""
    global high_score_list
    f = open('score.txt', 'w+')
    for i in high_score_list:
        f.write('{}\n'.format(i))
    f.close()


def score(time, attemps, city):
    """Count score"""
    score_formula = (city * 200) + 1100 - (time * 4.25) - (attemps * 95.75)
    return score_formula


def hang_animation(health_point):
    """Displaying hangman"""
    scene = open("end_scene.txt", "r")
    for x, line in enumerate(scene):
        if x < 25 and health_point == 0:
            print(line, end="")
        elif 29 <= x <= 53 and health_point == 1:
            print(line, end="")
        elif 59 <= x <= 83 and health_point == 2:
            print(line, end="")
        elif 89 <= x <= 113 and health_point == 3:
            print(line, end="")
        elif 119 <= x <= 143 and health_point == 4:
            print(line, end="")
        elif 149 <= x <= 173 and health_point == 5:
            print(line, end="")
        elif 179 <= x <= 204 and health_point == 6:
            print(line, end="")
        else:
            pass
    scene.close()


def fun_win(attemps, capital):
    """After win screen"""
    global high_score_list
    global game_time
    os.system('clear')
    game_time = time.time() - game_time
    cprint("\n" + 27 * '*' + "\n", 'yellow')
    hang_animation(6)

    cprint("\n" + 27 * '*', 'yellow')
    cprint("Congratulations you WON!", 'red', attrs=['bold'])
    cprint(27 * '*' + "\n\n", 'yellow')

    print("You guessed after %d attemps. It took you %d seconds. Your score: %d" % (
        attemps, game_time, score(game_time, attemps, len(capital))))
    name_user = input("Click Enter to continue (type your name): ")  # wraca do menu
    os.system('clear')
    load_list()
    high_score_list.append([score(game_time, attemps, len(capital)), name_user, game_time, attemps, capital])
    save_list()
    fun_leaderboards()
    return


def fun_lose(attemps):
    """After lose screen"""
    global game_time
    os.system('clear')
    game_time = time.time() - game_time
    cprint("\n" + 27 * '*' + "\n", 'yellow')
    hang_animation(0)

    cprint("\n" + 27 * '*', 'yellow')
    cprint("Congratulations you LOSE!", 'red', attrs=['bold'])
    cprint(27 * '*' + "\n\n", 'yellow')

    print("You not guessed after %d attemps. It took you %d seconds." % (attemps, game_time))
    input("Click Enter to continue")  # wraca do menu
    os.system('clear')
    return


def fun_play(country, capital, capitaldash):
    """Gameplay"""
    badletters = []
    attemps = 0
    global health

    while True:
        os.system('clear')
        cprint("\n" + 27 * '*' + "\n", 'yellow')
        hang_animation(health)
        cprint("\n" + 27 * '*' + "\n", 'yellow')
        print("Tell me what is capital city of ", country, "?")
        print("Length of word ", len(capitaldash), " Word:", capitaldash)
        cprint("\nMisses " + ",".join(badletters), 'red') # bad letters displaying
        userinput = input("\nEnter letter or word: ")
        userinput = userinput.upper()

        if len(userinput) > 1: #sprawdza czy uzytkownik wpisuje zdanie
            if userinput == capital:
                attemps += 1
                fun_win(attemps, capital)  # wygrana po calym zdaniu
                break
            else:
                badletters.append(userinput)
                health -= 2
        else: #sprawdza literki
            attemps += 1
            if userinput in capital: #jesli uzytkownik zgadl
                for x in range(len(capital)):
                    if capital[x] == userinput:
                        capitaldash = capitaldash[:x] + userinput + capitaldash[x + 1:]
                if capital == capitaldash:  # wygrana po literkach
                    fun_win(attemps, capital)
                    break
            else:
                badletters.append(userinput)
                health -= 1
        if health <= 0:
            fun_lose(attemps)
            break

    return


def fun_initplay():
    """Init Gameplay"""
    country_capital = fun_loadcountries()
    capitaldash = []
    # dzielenie country_capital na dwie zmienne
    for x in range(len(country_capital)):
        if country_capital[x] == "|":
            country = country_capital[:x - 1]
            capital = country_capital[x + 2:len(country_capital) - 1]
            capital = capital.upper()
            capitaldash = capital[:]
            break
    # zmienna capitaldash zamienia sie na "_" ale pomija spacje
    for i in range(len(capitaldash)):
        if capitaldash[i] != " ":
            capitaldash = capitaldash[:i] + '_' + capitaldash[i + 1:]

    # uruchomienie rozgrywki
    fun_play(country, capital, capitaldash)
    return


def fun_leaderboards():
    """Show leaderboards"""
    fun_effectwow('1effect.txt')
    load_list()
    high_score_list.sort(key=lambda x: int(x[0]), reverse=True)

    #creepy - to cos znajduje najdluzszy element z highscorelist aby poprawnie
    #wyswietlalo linie ******* etc.
    new_list = []
    for index, item in enumerate(high_score_list):
        new_list.append( len("{}. Score: {}  Name: {}  Time: {}sec  Atempts: {} Word: {}" \
              .format(index + 1, int(item[0]), item[1], int(item[2]), item[3], item[4]) ) )
    best_length = max(new_list)
    #creepy end


    cprint("\n" + (best_length * '*') +"\n", 'green', attrs=['bold', 'reverse'])

    for index, item in enumerate(high_score_list):
        print("{}. Score: {}  Name: {}  Time: {}sec  Atempts: {} Word: {}" \
              .format(index + 1, int(item[0]), item[1], int(item[2]), item[3], item[4]))

    cprint("\n" + (best_length * '*') +"\n", 'green', attrs=['bold', 'reverse'])
    input("Click Enter to continue")  # wraca do menu
    return


def fun_loadcountries():
    """Loading all contries and return random one"""
    countries_file = open("countries_and_capitals.txt", "r")
    countries_array = countries_file.readlines()
    countries_file.close()

    return countries_array[random.randrange(0, len(countries_array) - 1)]
    # zwraca losowe panstwo i jego stolice


def fun_effectwow(what):
    """Special effect"""
    f = open(what, 'r')
    colorlist = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    effect_list = [line[:-1] for line in f]
    f.close()

    for i in range( len(effect_list[0]) ):
        os.system('clear')
        for x in range(len(effect_list)):
            cprint(effect_list[x][:i],random.choice(colorlist))
        time.sleep(0.02)



# dziala
def main():
    """First function after loading program"""
    if not os.path.exists("score.txt"):
        scorelist = open("score.txt", "w")
        scorelist.close()

    global game_time
    global health
    os.system('clear')

    while True:
        fun_effectwow('2effect.txt')
        cprint('\n\n'+ 25 * '*', 'magenta', attrs=['bold'])
        print("\nMenu:\n1: Play game\n2: View Leaderboards\n3: Quit\n")
        cprint(25 * '*', 'magenta', attrs=['bold'])
        picked = input("\nYou pick: ")

        #menu system
        if picked == "1":
            health = 6
            game_time = time.time()
            fun_initplay()
        elif picked == "2":
            fun_leaderboards()
        elif picked == "3":
            cprint("\nGoodbye!\n", 'red', attrs=['bold'])
            break
        else:
            cprint("\nWrong command\n", 'red', attrs=['bold'])
            input()


if __name__ == "__main__":
    main()
