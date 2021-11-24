import random, math, time, sys

global user_choice1
global gym_badges
global stage_passed
global gyms
gym_badges = 0
stage_passed = []
time.sleep(2)
print("Welcome To Choose Your Own Adventure!")
print(" ")
time.sleep(3)
print("This game is based in the world of Pokemon!")
print(" ")
time.sleep(3)
print("To follow the proper storyline, please go in order of the gyms.")
print(" ")
time.sleep(3)
print("Throughout the game you will be given different options. \n\nPlease write exactly what is from the options given, in order to progress in the story.")
print(" ")
time.sleep(3)
print("The following types have an advantage against the fire type, Litten: Rock and Ground")
print(" ")
time.sleep(3)
print("The following types have an advantage against the water type, Popplio: Grass and Electric")
print(" ")
time.sleep(3)
print("The following types have an advantage against the grass type, Rowlet: Fire and Ground")
print(" ")
time.sleep(3)
input("Please press ANY KEY to start your adventure: ")
print(" ")
time.sleep(3)
user_choice1 = (str(input("Choose a starter pokemon you would like to have on your journey: Popplio, Rowlet or Litten? ")).lower()).strip()
gyms = ['rock gym', 'water gym', 'electric gym', 'grass gym', 'poison gym', 'psychic gym', 'fire gym', 'ground gym']
litten_move = []
popplio_move = []
rowlet_move = []
def exit_function():
    sys.exit()
def clear_screen():
    print("\n" * 50)
def call():
    global user_choice1
    if user_choice1 == "litten" or user_choice1 == "popplio" or user_choice1 == "rowlet":
        choose_starter()
        time.sleep(2)
        part_1()
        time.sleep(3)
        gym_1()
    else:
        print("Please Try Again")

def reset():
    global stage_passed
    global gyms
    global gym_badges
        
    print(" ")
    user_choice2 = str(input("Press ANY KEY to continue: ")).lower()
    while user_choice2 in stage_passed or user_choice2 not in stage_passed:
        print(" ")
        print(f'The following gyms that are left would be {gyms} or TYPE "EXIT" to exit the game!')
        print(" ")
        user_choice2 = (str(input("Which gym would you like to go to next? ")).lower()).strip()
        print(" ")
        if user_choice2 == "rock gym" and user_choice2 not in stage_passed:
            time.sleep(3)
            gym_1()
        elif user_choice2 == "exit":
            exit_function()
        elif user_choice2 != gyms[0]:
            print("Please try again!")
            print(" ")
            print("Incorrect Order of Gyms OR Incorrect input!")
        elif user_choice2 == "water gym" and user_choice2 not in stage_passed:
            time.sleep(3)
            gym_2()
        elif user_choice2 == "electric gym" and user_choice2 not in stage_passed:
            time.sleep(3)
            gym_3()
        elif user_choice2 == "grass gym" and user_choice2 not in stage_passed:
            time.sleep(3)
            gym_4()
        elif user_choice2 == "poison gym" and user_choice2 not in stage_passed:
            time.sleep(3)
            gym_5()
        elif user_choice2 == "psychic gym" and user_choice2 not in stage_passed:
            time.sleep(3)
            gym_6()
        elif user_choice2 == "fire gym" and user_choice2 not in stage_passed:
            time.sleep(3)
            gym_7()
        elif user_choice2 == "ground gym" and user_choice2 not in stage_passed:
            time.sleep(3)
            gym_8()
        else:
            print("Try Again")


def choose_starter():
    global user_choice1
    print(" ")
    time.sleep(3)
    print("You are in the amazing world of Pokemon." " To start your adventure you head to the pokemon research lab. Here, you meet the Pokemon Professor, He gives you your starter pokemon!")
    print(" ")
    starter1 = "litten"
    starter2 = "rowlet"
    starter3 = "popplio"

    if user_choice1 == starter1 or user_choice1 == starter2 or user_choice1 == starter3:
        if user_choice1 == starter1:
            time.sleep(3)
            print('As your partner you chose Litten!')
            print(" ")
            time.sleep(3)
            print("You also recieve a pokedex, a device that has information about all the pokemon you encounter.")
            print(" ")
            time.sleep(3)
            print("You ask the pokedex about your new chosen pokemon.")
            print(" ")
            time.sleep(3)
            print("It replies, Litten, The fire type pokemon, only available in the Alola Region!")
            print(" ")
        elif user_choice1 == starter2:
            time.sleep(3)
            print(f'As your partner you chose Rowlet!')
            print(" ")
            time.sleep(3)
            print("You also recieve a pokedex, a device that has information about all the pokemon you encounter.")
            print(" ")
            time.sleep(3)
            print("You ask the pokedex about your new chosen pokemon.")
            print(" ")
            time.sleep(3)
            print("It replies, Rowlet is the grass/flying type starter pokemon available only in the Alola Region!")
        elif user_choice1 == starter3:
            time.sleep(3)
            print(f'As your partner you chose Popplio!')
            print(" ")
            time.sleep(3)
            print("You also recieve a pokedex, a device that has information about all the pokemon you encounter.")
            print(" ")
            time.sleep(3)
            print("You ask the pokedex about your new chosen pokemon.")
            print(" ")
            time.sleep(3)
            print("It replies: Popplio, the water type pokemon, only available in the Alola Region!")
        else:
            print("Try again")
            reset()

    else:
        print("Please Try Again!")
        reset()

def part_1():
    global user_choice1
    time.sleep(3)
    print(" ")
    print("You now recieve some pokeballs to help you catch pokemon on your journey!")
    print(" ")
    time.sleep(3)
    print("You are told that there is a pokemon league in which if you win, you become the pokemon champion! ")
    print(" ")
    time.sleep(3)
    print("To enter the league, you must first beat all 8 gyms available in the kanto region. The 8 gyms available are the following: ")
    print(" ")
    print("------------------------------------")
    time.sleep(3)
    print("The rock gym: Pewter City ")
    print(" ")
    time.sleep(3)
    print("The water gym: Cerulean City ")
    print(" ")
    time.sleep(3)
    print("The electric gym: Vermillion City ")
    print(" ")
    time.sleep(3)
    print("The grass gym: Celadon City ")
    print(" ")
    time.sleep(3)
    print("The poison gym: Fuchsia City ")
    print(" ")
    time.sleep(3)
    print("The psychic gym: Saffron CIty ")
    print(" ")
    time.sleep(3)
    print("The fire gym: Cinnabar Island ")
    print(" ")
    time.sleep(3)
    print("The ground gym: Veridian City ")
    print("-------------------------------------")
    print(" ")
    time.sleep(3)
    print("To start, you go to Pewter City because it is the closest city to you.")
    print(" ")
    time.sleep(3)


def gym_1():
    global user_choice1
    global gym_badges
    print(" ")
    time.sleep(3)
    print("With your new partner, you have come to challenge the pewter city gym! You see the gym leader is Brock. He looks strong. ")
    print(" ")
    time.sleep(3)
    user_choice = (str(input("What would you like to do next, go ahead with the challenge? "
                            "\n\nOR Go back to prepare some more...(Note that if you go back, you will have to come back again. "
                            "\n\nType CHALLENGE to start the battle OR Type RUN to come back again: ")).lower()).strip()

    if user_choice == "challenge":
        print(" ")
        time.sleep(3)
        print("As you tell Brock you are here to challenge him, he accepts your challenge and the battle begins! Brock chooses Onix to battle!")
        if user_choice1 == "litten":
            gym_1_litten()
        elif user_choice1 == "popplio":
            gym_1_popplio()
        elif user_choice1 == "rowlet":
            gym_1_rowlet()
    elif user_choice == "run":
        time.sleep(3)
        print(" ")
        print("Come back to try again!")
        reset()
    else:
        print("NOT an option!")
        print(" ")
        print("Please Try Again!")
        reset()

def gym_1_litten():
    global user_choice1
    global gyms
    global gym_badges
    global stage_passed
    global litten_move
    if user_choice1 == "litten":
        time.sleep(3)
        print("You throw out your partner, Litten!")
        print(" ")
        time.sleep(3)
        print("As Litten is a fire type, it is extremely weak against Onix.")
        print(" ")
        time.sleep(3)
        litten_move.append("Scratch")
        litten_move.append("Ember")
        print(f'Your Litten knows the following moves: {litten_move}')
        time.sleep(3)
        print(" ")
        user_choice2 = (str(input(f'What move would you like {user_choice1} to use? ')).lower()).strip()
        print(" ")
        time.sleep(3)
        if user_choice2 == "ember":
            print("Litten uses ember!")
            print(" ")
            time.sleep(3)
            print("You lose as ember is not very effective against Onix, Litten takes a lot of damage from Onix's rock type moves.")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            litten_move.remove("Scratch")
            litten_move.remove("Ember")
            reset()
        elif user_choice2 == "scratch":
            print(" ")
            time.sleep(3)
            print("Litten uses scratch")
            print(" ")
            time.sleep(3)
            print("You win! Scratch is effective against Onix, but as Litten unleashed a barrage of this attack, Onix fainted!")
            print(" ")
            time.sleep(3)
            print("Brock gives you the pewter city badge!")
            gym_badges+=1
            print(" ")
            time.sleep(3)
            print(f'You are now {gym_badges}/8 of the way to become the champion!')
            stage_passed.append("rock gym")
            gyms.remove("rock gym")
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Try again")
            litten_move.remove("Scratch")
            litten_move.remove("Ember")
            reset()


def gym_1_popplio():
    global user_choice1
    global gym_badges
    global stage_passed
    global gyms
    global popplio_move
    print(" ")
    time.sleep(3)
    print("You throw out your partner, Popplio!")
    print(" ")
    time.sleep(3)
    print("With Popplio being a water type and Onix a rock type, Poplio is super effective against Onix!")
    print(" ")
    time.sleep(3)
    popplio_move.append("Bubble")
    print(f'Your Popplio knows the following moves: {popplio_move}')
    time.sleep(3)
    print(" ")
    user_choice3 = (str(input("What move would you like Popplio to use?")).lower()).strip()
    if user_choice3 == "bubble":
        print(" ")
        time.sleep(3)
        print("Popplio uses bubble!")
        print(" ")
        time.sleep(3)
        print("You win! Bubble is super effective against Onix as rock types are weak to water.")
        print(" ")
        time.sleep(3)
        print("Brock gives you the pewter city badge!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        print(f'You are now {gym_badges}/8 of the way to become the champion!')
        stage_passed.append("rock gym")
        gyms.remove("rock gym")
        if gym_badges == 8:
            end()
        else:
            reset()
    else:
        print("Try Again")
        popplio_move.remove("Bubble")
        reset()


def gym_1_rowlet():
    global user_choice1
    global gym_badges
    global stage_passed
    global gyms
    global rowlet_move
    print(" ")
    time.sleep(3)
    print("You throw out your partner, Rowlet!")
    print(" ")
    time.sleep(3)
    print("Rowlet is a grass type meaning it is super effective against Onix. ")
    print(" ")
    time.sleep(3)
    rowlet_move.append("Razor Leaf")
    print(f'Your Rowlet knows the following moves: {rowlet_move}')
    time.sleep(3)
    user_choice4 = (str(input("What move would you like Rowlet to use?")).lower()).strip()
    if user_choice4 == "razor leaf":
        print(" ")
        time.sleep(3)
        print("Rowlet uses razor leaf!")
        print(" ")
        time.sleep(3)
        print("You win! Razor Leaf is super effective against Onix as rock types are weak to grass.")
        print(" ")
        time.sleep(3)
        print("Brock gives you the pewter city badge!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        print(f'You are now {gym_badges}/8 of the way to become the champion!')
        stage_passed.append("rock gym")
        gyms.remove("rock gym")
        if gym_badges == 8:
            end()
        else:
            reset()
    else:
        print("Try again")
        rowlet_move.remove("Razor Leaf")
        reset()

def gym_2():
    global user_choice1
    global litten_move
    global popplio_move
    global rowlet_move
    if user_choice1 == "litten":
        new_move = "Fire Fang"
    elif user_choice1 == "popplio":
        new_move = "Water gun"
    elif user_choice1 == "rowlet":
        new_move = "Fly"
    print(" ")
    print("As you have now won against Brock, you head to the next gym, the water type gym in Cerulean City!")
    print(" ")
    time.sleep(3)
    print("As you arrive in the city, you instantly notice the huge gym! You head towards the gym and go inside.")
    print(" ")
    time.sleep(3)
    print("You meet Misty, the Cerulean City gym leader!")
    print(" ")
    time.sleep(3)
    print("You tell Misty that you are here to battle her, she accepts your challenge and the battle begins!")
    print(" ")
    time.sleep(3)
    print("Misty throws out her partner, Starmie!")
    print(" ")
    time.sleep(3)
    print(f'Your partner {user_choice1} has learned {new_move}!')
    print(" ")
    time.sleep(3)
    if user_choice1 == "litten":
        gym_2_litten()
    elif user_choice1 == "popplio":
        gym_2_popplio()
    elif user_choice1 == "rowlet":
        gym_2_rowlet()
    else:
        print("Try Again")


def gym_2_litten():
    global user_choice1
    global gym_badges
    global stage_passed
    global gyms
    global litten_move
    if user_choice1 == "litten":
        print(" ")
        print("You throw out your partner Litten!")
        print(" ")
        time.sleep(3)
        print("Litten is weak to water types meaning its fire type move ember would not be effective against Starmie.")
        print(" ")
        time.sleep(3)
        litten_move.append("Fire Fang")
        print(f'Your Litten knows the following moves {litten_move}')
        print(" ")
        time.sleep(3)
        user_choice = (str(input("What move would you like Litten to use? ")).lower()).strip()
        if user_choice == "ember":
            print(" ")
            print("Your Litten used ember, ember is not very effective against water types.")
            print(" ")
            time.sleep(3)
            print("You lose as Starmie uses water gun, a super effective move against your Litten!")
            print(" ")
            time.sleep(3)
            litten_move.remove("Fire Fang")
            reset()
        elif user_choice == "scratch":
            print(" ")
            print("Your Litten used Scratch, it is effective against Starmie!")
            time.sleep(3)
            if random.randrange(1, 3) == 1:
                print(" ")
                print("Litten loses as Starmie is faster and uses Water gun on Litten which is super effective")
                print(" ")
                time.sleep(3)
                print("Come back to try again!")
                print(" ")
                time.sleep(3)
                litten_move.remove("Fire Fang")
                reset()
            else:
                print("Litten wins as it was faster than Starmie and didnt give Starmie a chance to react.")
                print(" ")
                time.sleep(3)
                print("As you win, you recieve the Cerulean City badge from Misty!")
                print(" ")
                time.sleep(3)
                gym_badges+=1
                print(f'You are now {gym_badges}/8 of the way to become the champion!')
                time.sleep(3)
                stage_passed.append("water gym")
                gyms.remove("water gym")
                if gym_badges == 8:
                    end()
                else:
                    reset()
        elif user_choice == "fire fang":
            print(" ")
            print("Your Litten used Fire fang, it is not effective against Starmie!")
            time.sleep(3)
            if random.randrange(1, 3) == 1:
                print(" ")
                print("Litten wins!, Starmie could not predict Litten's movements!")
                print(" ")
                time.sleep(3)
                print("As you win, you recieve the Cerulean City badge from Misty!")
                print(" ")
                time.sleep(3)
                gym_badges+=1
                print(f'You are now {gym_badges}/8 of the way to become the champion!')
                time.sleep(3)
                stage_passed.append("water gym")
                gyms.remove("water gym")
                if gym_badges == 8:
                    end()
                else:
                    reset()
            else:
                print(" ")
                print("Litten looses")
                print(" ")
                time.sleep(3)
                print("Come back to try again!")
                time.sleep(3)
                litten_move.remove("Fire Fang")
                reset()

        else:
            print("Try Again!")
            litten_move.remove("Fire Fang")
            reset()


def gym_2_popplio():
    global user_choice1
    global gym_badges
    global stage_passed
    global popplio_move
    global gyms
    if user_choice1 == "popplio":
        print(" ")
        print("You throw out your partner Popplio!")
        print(" ")
        time.sleep(3)
        print("As Popplio is the same type as Starmie, water type attacks are effective against it.")
        print(" ")
        time.sleep(3)
        popplio_move.append("Water gun")
        print(f'Your Popplio knows the following moves: {popplio_move}')
        time.sleep(3)
        print(" ")
        user_choice2 = (str(input("What move would you like Popplio to use? ")).lower()).strip()
        if user_choice2 == "bubble":
            print(" ")
            print("Popplio used Bubble!, it is effective against Starmie")
            time.sleep(3)
            if random.randrange(1, 3) == 1:
                print(" ")
                print("Popplio loses")
                print(" ")
                time.sleep(3)
                print("Come back and Try again")
                time.sleep(3)
                popplio_move.remove("Water gun")
                reset()
            else:
                print(" ")
                print("You win! The opposing Starmie could not do enough damage to Popplio before it fainted.")
                print(" ")
                time.sleep(3)
                print("You recieve the cerulean city gym badge!")
                print(" ")
                time.sleep(3)
                gym_badges+=1
                gyms.remove("water gym")
                print(f'You are now {gym_badges}/8 of the way to become the champion!')
                time.sleep(3)
                stage_passed.append("water gym")
                if gym_badges == 8:
                    end()
                else:
                    reset()
        elif user_choice2 == "water gun":
            print(" ")
            print("Popplio used water gun!, it is effective against Starmie")
            print(" ")
            time.sleep(3)
            if random.randrange(1, 3) == 1:
                print(" ")
                print("Popplio loses")
                print(" ")
                time.sleep(3)
                print("Come back and Try again")
                print(" ")
                time.sleep(3)
                popplio_move.remove("Water gun")
                reset()
            else:
                print("You win! The opposing Starmie could not do enough damage to Popplio before it fainted.")
                print(" ")
                time.sleep(3)
                print("You recieve the cerulean city gym badge!")
                print(" ")
                time.sleep(3)
                gym_badges+=1
                gyms.remove("water gym")
                print(f'You are now {gym_badges}/8 of the way to become the champion!')
                time.sleep(3)
                stage_passed.append("water gym")
                if gym_badges == 8:
                    end()
                else:
                    reset()


def gym_2_rowlet():
    global user_choice1
    global gym_badges
    global stage_passed
    global rowlet_move
    global gyms
    if user_choice1 == "rowlet":
        print(" ")
        print("You throw out your partner Rowlet!")
        print(" ")
        time.sleep(3)
        print("As Rowlet is a grass type, it is super effective against Starmie!")
        print(" ")
        time.sleep(3)
        rowlet_move.append("Fly")
        print(f'Your Rowlet knows the follwing moves: {rowlet_move}')
        print(" ")
        time.sleep(3)
        user_choice3 = (str(input("What move would you like Rowlet to use?")).lower()).strip()
        print(" ")
        if user_choice3 == "razor leaf":
            print("Rowlet used Razor Leaf!, it is super effective against Starmie!")
            print(" ")
            time.sleep(3)
            print("Rowlet wins!")
            print(" ")
            time.sleep(3)
            print("You recieve the Cerulean city badge!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            print(f'You are now {gym_badges}/8 of the way to become the champion!')
            time.sleep(3)
            stage_passed.append("water gym")
            gyms.remove("water gym")
            if gym_badges == 8:
                end()
            else:
                reset()
        elif user_choice3 == "fly":
            print(" ")
            print("Rowlet used Fly!, it is effective against Starmie!")
            time.sleep(3)
            if random.randrange(1, 3) == 1:
                print(" ")
                print("Rowlet Wins!")
                print(" ")
                time.sleep(3)
                print("You recieve the Cerulean city badge!")
                print(" ")
                time.sleep(3)
                gym_badges+=1
                print(f'You are now {gym_badges}/8 of the way to become the champion!')
                time.sleep(3)
                stage_passed.append("water gym")
                gyms.remove("water gym")
                if gym_badges == 8:
                    end()
                else:
                    reset()
            else:
                print(" ")
                print("You lose, Starmie used Ice Beam to counter Fly.")
                print(" ")
                time.sleep(3)
                print("Come back to try again!")
                time.sleep(3)
                rowlet_move.remove("Fly")
                reset()
        else:
            print("Try again")
            rowlet_move.remove("Fly")
            reset()

def gym_3():
    global user_choice1
    global litten_move
    global popplio_move
    global rowlet_move
    if user_choice1 == "litten":
        evolve = "Torracat"
        move = "Flamethrower"
        litten_move.append("Flamethrower")
    elif user_choice1 == "popplio":
        evolve = "Brione"
        move = "Ice Beam"
        popplio_move.append("Ice Beam")
    elif user_choice1 == "rowlet":
        evolve = "Dartrix"
        move = "Earthquake"
        rowlet_move.append("Earthquake")
    print(f'As you beat the Cerulean City gym, the water gym. Your partner, {user_choice1} has evolved into {evolve}!')
    print(" ")
    time.sleep(3)
    print(f'{evolve} has learned a new move, {move}.')
    print(" ")
    time.sleep(3)
    print("You arrive in Vermillion City to challenge the electric gym!")
    print(" ")
    time.sleep(3)
    print("The gym leader is Lt. Surge, he is also known as the strongest electric type trainer in the whole kanto region!")
    print(" ")
    time.sleep(3)
    print("You tell Lt. Surge that you are here to challenge him and the battle begins!")
    print(" ")
    time.sleep(3)
    print("Lt. Surge throws out his partner, Electrivire!")
    print(" ")
    time.sleep(3)
    if user_choice1 == "litten":
        gym_3_torracat()
    elif user_choice1 == "popplio":
        gym_3_brione()
    elif user_choice1 == "rowlet":
        gym_3_dartrix()


def gym_3_torracat():
    global user_choice1
    global gym_badges
    global stage_passed
    global gyms
    global litten_move
    print("You throw out your partner Torracat!")
    print(" ")
    time.sleep(3)
    print("As Torracat is a fire type, Litten is effective against Electrivire!")
    print(" ")
    time.sleep(3)
    print(f'Your Torracat knows the following moves: {litten_move}')
    print(" ")
    time.sleep(3)
    user_choice2 = (str(input("What move would you like Torracat to use? ")).lower()).strip()
    if user_choice2 == "ember":
        print(" ")
        print("Torracat uses ember!, it is effective against Electrivire!")
        print(" ")
        time.sleep(3)
        if random.randrange(1, 3) == 1:
            print("Torracat wins!")
            print(" ")
            time.sleep(3)
            print("Electrivire suffers from a lot of damage from its burn from ember and it faints!")
            print(" ")
            time.sleep(3)
            print("You recieve the Vermillion City Badge!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            print(f'You are now {gym_badges}/8 of the way to become the champion!')
            print(" ")
            time.sleep(3)
            stage_passed.append("electric gym")
            gyms.remove("electric gym")
            litten_move.remove("Scratch")
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Torracat looses!")
            print(" ")
            time.sleep(3)
            print("Come back to try again")
            print(" ")
            time.sleep(3)
            litten_move.remove("Fire Fang")
            reset()
    elif user_choice2 == "fire fang":
        print(" ")
        print("Torracat uses Fire Fang!, it is effective against Electrivire!")
        print(" ")
        time.sleep(3)
        if random.randrange(1, 3) == 1:
            print("Torracat wins!")
            print(" ")
            time.sleep(3)
            print("Electrivire suffers from a lot of damage from its burn from ember and it faints!")
            print(" ")
            time.sleep(3)
            print("You recieve the Vermillion City Badge!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            print(f'You are now {gym_badges}/8 of the way to become the champion!')
            print(" ")
            time.sleep(3)
            stage_passed.append("electric gym")
            gyms.remove("electric gym")
            litten_move.remove("Scratch")
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Torracat looses!")
            print(" ")
            time.sleep(3)
            print("Come back to try again")
            print(" ")
            time.sleep(3)
            litten_move.remove("Flamethrower")
            reset()
    elif user_choice2 == "flamethrower":
        print(" ")
        print("Torracat uses Flamethrower!, it is effective against Electrivire!")
        print(" ")
        time.sleep(3)
        if random.randrange(1, 3) == 1:
            print("Torracat wins!")
            print(" ")
            time.sleep(3)
            print("Electrivire suffers from a lot of damage from its burn from ember and it faints!")
            print(" ")
            time.sleep(3)
            print("You recieve the Vermillion City Badge!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            print(f'You are now {gym_badges}/8 of the way to become the champion!')
            print(" ")
            time.sleep(3)
            stage_passed.append("electric gym")
            gyms.remove("electric gym")
            litten_move.remove("Scratch")
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Torracat looses!")
            print(" ")
            time.sleep(3)
            print("Come back to try again")
            print(" ")
            time.sleep(3)
            litten_move.remove("Flamethrower")
            reset()
    elif user_choice == "scratch":
        print(" ")
        print("Your Litten used Scratch, it is effective against Electrivire!")
        time.sleep(3)
        if random.randrange(1, 3) == 1:
            print(" ")
            print("Litten loses as Electrivire uses Thunderbolt to paralyize Litten, it faints")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            litten_move.remove("Flamethrower")
            reset()
        else:
            print("Litten wins as it was faster than Electrivire and didnt give it a chance to react.")
            print(" ")
            time.sleep(3)
            print("As you win, you recieve the Vermillion City badge from Lt. Surge!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            print(f'You are now {gym_badges}/8 of the way to become the champion!')
            time.sleep(3)
            stage_passed.append("electric gym")
            gyms.remove("electric gym")
            if gym_badges == 8:
                end()
            else:
                reset()
                    
    
    else:
        print("Try Again")
        litten_move.remove("Flamethrower")
        reset()
def gym_3_brione():
    global user_choice1
    global gym_badges
    global stage_passed
    global gyms
    global popplio_move
    print("You throw out your partner Brione!")
    print(" ")
    time.sleep(3)
    print("As Brione is a water type, Electrivire is super effective against Popplio")
    print(" ")
    time.sleep(3)
    print(f'Your Brione knows the following moves: {popplio_move}')
    print(" ")
    time.sleep(3)
    user_choice2 = (str(input("What move would you like Brione to use? ")).lower()).strip()
    print(" ")
    time.sleep(3)
    if user_choice2 == "water gun":
        print("Brione used Water Gun!, it is ineffective against Electrivire.")
        print(" ")
        time.sleep(3)
        if random.randrange(1, 3) == 1:
            print("Brione wins!")
            print(" ")
            time.sleep(3)
            print("Electrivire could not handle the speed of Brione")
            print(" ")
            time.sleep(3)
            print("You recieve the Vermillion City Badge!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            print(f'You are now {gym_badges}/8 of the way to become the champion!')
            print(" ")
            time.sleep(3)
            stage_passed.append("electric gym")
            gyms.remove("electric gym")
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Brione looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again")
            print(" ")
            time.sleep(3)
            popplio_move.remove("Ice Beam")
            reset()
    elif user_choice2 == "ice beam":
        print("Brione used Ice Beam!, it is effective against Electrivire.")
        print(" ")
        time.sleep(3)
        if random.randrange(1, 3) == 1:
            print("Brione wins!")
            print(" ")
            time.sleep(3)
            print("Brione's ice beam froze Electrivire, it fainted as Popplio did not let it free.")
            print(" ")
            time.sleep(3)
            print("You recieve the Vermillion City Badge!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            print(f'You are now {gym_badges}/8 of the way to become the champion!')
            print(" ")
            time.sleep(3)
            stage_passed.append("electric gym")
            gyms.remove("electric gym")
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Brione looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again")
            print(" ")
            time.sleep(3)
            popplio_move.remove("Ice Beam")
            reset()
    elif user_choice2 == "bubble":
        print("Brione used Bubble!, it is ineffective against Electrivire.")
        print(" ")
        time.sleep(3)
        if random.randrange(1, 3) == 1:
            print("Brione wins!")
            print(" ")
            time.sleep(3)
            print("Electrivire could not handle the speed of Popplio")
            print(" ")
            time.sleep(3)
            print("You recieve the Vermillion City Badge!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            print(f'You are now {gym_badges}/8 of the way to become the champion!')
            print(" ")
            time.sleep(3)
            stage_passed.append("electric gym")
            gyms.remove("electric gym")
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Brione looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again")
            print(" ")
            time.sleep(3)
            popplio_move.remove("Ice Beam")
            reset()
    else:
        print("Try again")
        reset()
def gym_3_dartrix():
    global user_choice1
    global gym_badges
    global stage_passed
    global gyms
    global rowlet_move
    print("You throw out your partner Dartrix!")
    print(" ")
    time.sleep(3)
    print("As Dartrix is a grass type, Dartrix is effective against Electrivire!")
    print(" ")
    time.sleep(3)
    print(f'Your Dartrix knows the follwing moves: {rowlet_move}')
    print(" ")
    time.sleep(3)
    user_choice2 = (str(input("What move would you like Dartrix to use? ")).lower()).strip
    print(" ")
    time.sleep(3)
    if user_choice2 == "earthquake":
        print("Dartrix used Earthquake!, it is super effective against Electrivire!.")
        print(" ")
        time.sleep(3)
        print("Dartrix wins as Electrivire cannot handle the Earthquake, it faints!")
        print(" ")
        time.sleep(3)
        print("You recieve the Vermillion City Badge!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        print(f'You are now {gym_badges}/8 of the way to become the champion!')
        print(" ")
        time.sleep(3)
        stage_passed.append("electric gym")
        gyms.remove("electric gym")
        if gym_badges == 8:
            end()
        else:
            reset()
    elif user_choice2 == "razor leaf":
        print("Dartrix used Razor Leaf!, it is effective against Electrivire!.")
        print(" ")
        time.sleep(3)
        if random.randrange(1, 3) == 1:
            print("Dartrix wins!")
            print(" ")
            time.sleep(3)
            print("You recieve the Vermillion City Badge!")
            print(" ")
            time.sleep(3)
            print("You are 3/8 of the way to become the champion!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            print(f'You are now {gym_badges}/8 of the way to become the champion!')
            print(" ")
            time.sleep(3)
            stage_passed.append("electric gym")
            gyms.remove("electric gym")
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Dartrix looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again")
            print(" ")
            time.sleep(3)
            rowlet_move.remove("Earthquake")
    elif user_choice2 == "fly":
        print("Dartrix used fly, it is not effective against Electrivire!")
        print(" ")
        time.sleep(3)
        print("Dartrix looses as Electrivire uses Thunderbolt, a super effective move against a flying move")
        print(" ")
        time.sleep(3)
        print("Come back to try again")
        print(" ")
        time.sleep(3)
        rowlet_move.remove("Earthquake")
        reset()
    else:
        print("Try again")
        reset()

def gym_4():
    global user_choice1
    global litten_move
    global popplop_move
    global rowlet_move
    if user_choice1 == "litten":
        move = "Darkest Lariat"
        evolution = "Torracat"
        litten_move.append("Darkest Lariat")
    elif user_choice1 == "popplio":
        move = "Sparking Aria"
        evolution = "Brione"
        popplio_move.append("Sparkling Aria")
    elif user_choice1 == "rowlet":
        move = "Spirit Shackle"
        evolution = "Dartrix"
        rowlet_move.append("Spirit Shackle")
    print("You arrive in Celadon City to challenge the Grass Gym!")
    print(" ")
    time.sleep(3)
    print("The gym leader is Erika who specializes in grass type pokemon!")
    print(" ")
    time.sleep(3)
    print("Erika accepts your challenge and the battle begins!")
    print(" ")
    time.sleep(3)
    print("Erika throws out her partner Venusaur!")
    print(" ")
    time.sleep(3)
    print(f'Your partner, {evolution} has learned a new move, {move}!')
    time.sleep(3)
    if user_choice1 == "litten":
        gym_4_torracat()
    elif user_choice1 == "popplio":
        gym_4_brione()
    elif user_choice1 == "rowlet":
        gym_4_dartrix()


def gym_4_torracat():
    global user_choice1
    global gym_badges
    global stage_passed
    global gyms
    global litten_move
    print("You throw out your partner, Torracat!")
    print(" ")
    time.sleep(3)
    print("As Torracat is a fire type, it is super effective against Venusaur!")
    print(" ")
    time.sleep(3)
    print(f'Your Torracat knows the follwing moves: {litten_move}')
    print(" ")
    time.sleep(3)
    user_choice = (str(input("What move would you like Torracat to use? ")).lower()).strip()
    print(" ")
    time.sleep(3)
    if user_choice == "ember":
        print("Torracat used Ember!, it is super effective against Venusaur!")
        print(" ")
        time.sleep(3)
        if random.randrange(1, 3) == 1:
            print("Torracat wins!")
            print(" ")
            time.sleep(3)
            print("Venusaur got a burn from Torracat's ember, as it suffered too much damage, it fainted!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            print(f'You are now {gym_badges}/8 of the way to become the champion!')
            print(" ")
            time.sleep(3)
            stage_passed.append("grass gym")
            gyms.remove("grass gym")
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Torracat looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again")
            print(" ")
            time.sleep(3)
            litten_move.remove("Darkest Lariat")
            reset()
    elif user_choice == "fire fang":
        print("Torracat used Fire Fang!, it is super effective against Venusaur!")
        print(" ")
        time.sleep(3)
        print("Torracat wins!, Venusaur got severe burns from Torracat's fire fang, it fainted as it could not fight back!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        print(f'You are now {gym_badges}/8 of the way to become the champion')
        print(" ")
        time.sleep(3)
        stage_passed.append("grass gym")
        gyms.remove("grass gym")
        if gym_badges == 8:
            end()
        else:
            reset()
    elif user_choice == "flamethrower":
        print("Torracat used Flamethrower!, it is super effective against Venusaur!")
        print(" ")
        time.sleep(3)
        if random.randrange(1, 3) == 1:
            print("Torracat wins!, as Venusaur was dealt with severe burns from Torracat's flamethrower, it fainted!")
            print(" ")
            time.sleep(3)
            print("You recieve the Celadon City badge from Erika!")
            print(" ")
            time.sleep(3)
            gym_badges += 1
            print(f'You are now {gym_badges}/8 of the way to become the champion')
            print(" ")
            time.sleep(3)
            stage_passed.append("grass gym")
            gyms.remove("grass gym")
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Torracat looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again")
            print(" ")
            time.sleep(3)
            litten_move.remove("Darkest Lariat")
            reset()
        reset()
    elif user_choice == "darkest lariat":
        print("Torracat used Darkest Lariat!")
        print(" ")
        time.sleep(3)
        if random.randint(1,2) == 1:
            print("Torracat wins!")
            print(" ")
            time.sleep(3)
            print("Venusaur cannot handle the sheer power of Darkest Lariat!")
            print(" ")
            time.sleep(3)
            print("You recieve the Celadon City badge from Erika!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            stage_passed.append("grass gym")
            gyms.remove("grass gym")
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Torracat looses, Venusaur unleashes a powerful barrage of Vine Whip attacks!, it faints")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            time.sleep(3)
            litten_move.remove("Darkest Lariat")
            reset()
            
def gym_4_brione():
    global user_choice1
    global gym_badges
    global stage_passed
    global gyms
    global popplio_move
    print("You throw out your partner, Brione!")
    print(" ")
    time.sleep(3)
    print("As Brione is a water type, Venusaur is super effective against it.")
    print(" ")
    time.sleep(3)
    print(f'Your Brione knows the following moves: {popplio_move}')
    print(" ")
    time.sleep(3)
    user_choice = (str(input("What move would you like Brione to use? ")).lower()).strip()
    print(" ")
    time.sleep(3)
    if user_choice == "ice beam":
        print("Brione used Ice Beam!, it is super effective against Venusaur!")
        print(" ")
        time.sleep(3)
        print("Venusaur faints as it gets frozen from the ice beam Brione used on it.")
        print(" ")
        time.sleep(3)
        print("You recieve the Celadon City badge from Erika!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        stage_passed.append("grass gym")
        gyms.remove("grass gym")
        print(f'You are now {gym_badges}/8 of the way to become the champion')
        print(" ")
        time.sleep(3)
        if gym_badges == 8:
            end()
        else:
            reset()
    elif user_choice == "water gun":
        print("Brione used Water Gun, it is not very effective against Venusaur!")
        print(" ")
        time.sleep(3)
        if random.randrange(1, 3) == 1:
            print("Brione wins!, Venusaur could not handle Brione's speed and pressure of the water gun!")
            print(" ")
            time.sleep(3)
            print("You recieve the Celadon City Badge from Erika!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            stage_passed.append("grass gym")
            gyms.remove("grass gym")
            print(f'You are now {gym_badges}/8 of the way to become the champion!')
            print(" ")
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Brione looses!, Venusaur uses Vine Whip which is super effective against Brione, it faints")
            print(" ")
            time.sleep(3)
            print("Come back to try again")
            print(" ")
            time.sleep(3)
            popplio_move.remove("Sparkling Aria")
            reset()
    elif user_choice == "bubble":
        print("Brione used Bubble, it is not very effective against Venusaur!")
        print(" ")
        time.sleep(3)
        print("Brione looses as Bubble does not do nearly enough damage to Venusaur.")
        print(" ")
        time.sleep(3)
        print("Come back to try again")
        print(" ")
        time.sleep(3)
        popplio_move.remove("Sparkling Aria")
        reset()
    elif user_choice == "sparkling aria":
        print("Brione used Sparkling Aria!, it is not very effective against Venusaur!")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("You win!, Venusaur looses as it gets absorbed by Sparkling Aria!")
            print(" ")
            time.sleep(3)
            print("You recieve the Celadon City badge from Erika!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            stage_passed.append("grass gym")
            gyms.remove("grass gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            print(" ")
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Brione looses, Venusaur uses Vine Whip which is super effective against Brione!, it faints")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            time.sleep(3)
            popplio_move.remove("Sparkling Aria")
            reset()
            
def gym_4_dartrix():
    global gym_badges
    global stage_passed
    global gyms
    global rowlet_move
    print("You throw out your partner, Dartrix!")
    print(" ")
    time.sleep(3)
    print("As Dartrix is a flying/grass type, it can be super effective against Venusaur!")
    print(" ")
    time.sleep(3)    
    print(f'Your Dartrix knows the following moves: {rowlet_move}')
    print(" ")
    time.sleep(3)
    user_choice = (str(input("What move would you like Dartrix to use? ")).lower()).strip()
    print(" ")
    time.sleep(3)
    if user_choice == "razor leaf":
        print("Dartrix uses Razor Leaf!")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("Dartrix wins! Venusaur could not land a single hit on Dartrix as it flew around Venusaur very quickly!")
            print(" ")
            time.sleep(3)
            print("You recieve the Celadon City badge from Erika!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            print(f'You are now {gym_badges}/8 of the way to become the champion!')
            print(" ")
            time.sleep(3)
            stage_passed.append("grass gym")
            gyms.remove("grass gym")
            if gym_badges == 8:
                  end()
            else:
                reset()
        else:
            print("Dartrix used Razor leaf however, it lost as Venusaur unleashed a powerful solar beam which dartrix could not handle.")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            rowlet_move.remove("Spirit Shackle")
            reset()
    elif user_choice == "fly":
        print("Dartrix uses Fly!")
        print(" ")
        time.sleep(3)
        print("It flies up into the air and avoid all attacks from Venusaur")
        print(" ")
        time.sleep(3)
        print("The attack has a direct and powerful it, as it is super effective against Venusaur, it faints!")
        print(" ")
        time.sleep(3)
        print("You win the battle and recieve the Celadon City badge from Erika!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        print(f'You are {gym_badges}/8 of the way to become the champion!')
        print(" ")
        time.sleep(3)
        stage_passed.append("grass gym")
        gyms.remove("grass gym")
        if gym_badges == 8:
            end()
        else:
            reset()
    elif user_choice == "spirit shackle":
        print("Dartrix uses Spirit Shackle!")
        print(" ")
        time.sleep(3)
        print("As Spirit Shackle is a ghost type move, it is effective against Venusaur!")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("Dartrix wins! Venusaur couldnt handle the power of Spirit Shackle!")
            print(" ")
            time.sleep(3)
            print("You recieve the Celadon City badge from Erika!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("grass gym")
            print(f'You are {gym_badges}/8 of the way to become the champion!')
            print(" ")
            time.sleep(3)
            stage_passed.append("grass gym")
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Dartrix looses!, Venusaur overpowers it with Vine Whip!")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            time.sleep(3)
            rowlet_move.remove("Spirit Shackle")
            reset()
            
    elif user_choice == "earthquake":
        print("Dartrix used Earthquake!, it is super effective against Venusaur!.")
        print(" ")
        time.sleep(3)
        print("Dartrix wins as Venusaur cannot handle the Earthquake, it faints!")
        print(" ")
        time.sleep(3)
        print("You recieve the Celadon City Badge!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        print(f'You are now {gym_badges}/8 of the way to become the champion!')
        print(" ")
        time.sleep(3)
        stage_passed.append("grass gym")
        gyms.remove("grass gym")
        if gym_badges == 8:
            end()
        else:
            reset()

def gym_5():
    global user_choice1
    print("You arrive in Fuchsia City, to challenge the Poison gym!")
    print(" ")
    time.sleep(3)
    print("The gym leader is Janine")
    print(" ")
    time.sleep(3)
    print("Janine accepts your challenge and the battle begins!")
    print(" ")
    time.sleep(3)
    print("Janine throws out her partner, Crobat!")
    print(" ")
    time.sleep(3)
    print("Crobat is a poison type pokemon")
    print(" ")
    time.sleep(3)
    if user_choice1 == "litten":
        gym_5_torracat()
    elif user_choice1 == "popplio":
        gym_5_brione()
    elif user_choice1 == "rowlet":
        gym_5_dartrix()

def gym_5_torracat():
    global gym_badges
    global stage_passed
    global gyms
    global litten_move
    print("You throw out your partner, Torracat!")
    print(" ")
    time.sleep(3)
    print("As Torracat is a fire type, it is effective against Crobat")
    print(" ")
    time.sleep(3)
    print(f'Your Torracat knows the following moves: {litten_move}')
    print(" ")
    time.sleep(3)
    user_choice = (str(input("What move would you like Torracat use? ")).lower()).strip()
    print(" ")
    time.sleep(3)
    if user_choice == "fire fang":
        print("Torracat used fire fang!, it is effective against Crobat!")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("Torracat wins!, Crobat couldn't handle the power of Torracat's Fire fang and it fainted!")
            print(" ")
            time.sleep(3)
            print("You recieve the Fuchsia City badge from Janine!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            print(f'You are now {gym_badges}/8 of the way to become the champion!')
            print(" ")
            time.sleep(3)
            stage_passed.append("poison gym")
            gyms.remove("poison gym") 
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Torracat looses as Crobat overpowers it by using Cross-Poison!")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "flamethrower":
        print("Torracat used Flamethrower!, it is effective against Crobat!")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("Torracat wins!, Crobat couldn't handle the power of Torracat's Flamethrower!")
            print(" ")
            time.sleep(3)
            print("You recieve the Fuchsia City badge from Janine!")
            print(" ")
            gym_badges+=1
            time.sleep(3)
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            print(" ")
            time.sleep(3)
            stage_passed.append("poison gym")
            gyms.remove("poison gym")            
            if gym_badges == 8:
                end()
            else:
                reset()

        else:
            print("Torracat looses, Crobat uses Cross-Poison and it poisoned Torracat, it fainted")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "ember":
        print("Torracat used Ember!")
        print(" ")
        time.sleep(3)
        print("Torracat looses as Ember is a very weak move to use against Crobat")
        print(" ")
        time.sleep(3)
        print("Come back to try again!")
        print(" ")
        time.sleep(3)
        reset()
    elif user_choice == "darkest lariat":
        print("Torrcat used Darkest Lariat!")
        print(" ")
        time.sleep(3)
        print("Torracat wins!, Darkest Lariat is too powerful for Crobat to handle!")
        print(" ")
        time.sleep(3)
        print("You recieve the Fuchsia City badge from Janine!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        print(f'You are now {gym_badges}/8 of the of becoming the champion!')
        print(" ")
        time.sleep(3)
        stage_passed.append("poison gym")
        gyms.remove("poison gym")
        if gym_badges == 8:
            end()
        else:
            reset()
        

def gym_5_brione():
    global gym_badges
    global stage_passed
    global gyms
    global popplio_move
    print("You throw out your partner Brione!")
    print(" ")
    time.sleep(3)
    print(f'Your Brione knows the following moves: {popplio_move}')
    print(" ")
    time.sleep(3)
    user_choice = (str(input("What move would you like Brione to use? ")).lower()).strip()
    print(" ")
    time.sleep(3)
    if user_choice == "sparkling aria":
        print("Brione uses Sparkling Aria!, it is effective against Crobat")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("Brione wins!, Crobat is absorbed by the huge bubble created by Brione's Sparkling Aria!")
            print(" ")
            time.sleep(3)
            print("You recieve the Fuchsia City badge from Janine!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            print(f'You are {gym_badges}/8 of the way to become the champion!')
            print(" ")
            time.sleep(3)
            stage_passed.append("poison gym")
            gyms.remove("poison gym")
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Brione looses, it is overpowered by Crobat and cannot survive its Cross-Poison")
            print(" ")
            time.sleep(3)
            print("Come back to try again")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "water gun":
        print("Brione uses Water gun!, it is effective against Crobat")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("Brione wins!, Crobat looses as water gun overpowered Crobat's Cross-Poison!")
            print(" ")
            time.sleep(3)
            print("You recieve the Fuchsia city badge from Janine!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            stage_passed.append("poison gym")
            gyms.remove("poison gym")
            print(f'You are {gym_badges}/8 of the way to become the champion!')
            print(" ")
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Brione looses, Crobat is faster than Brione which results in more attacks landing from Crobat. Brione fainted")
            print(" ")
            time.sleep(3)
            print("Come back to try again")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "bubble":
        print("Brione uses Bubble!, it is effective against Crobat!")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("Brione wins!, Bubble overpowers Crobat's cross-poison.")
            print(" ")
            time.sleep(3)
            print("You recieve the Fuchsia City badge from Janine")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            print(f'You are {gym_badges}/8 of the way to become the champion!')
            print(" ")
            time.sleep(3)
            stage_passed.append("poison gym")
            gyms.remove("poison gym")
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Brione looses, Crobat is faster than Brione, it faints as Crobat poisons Brione")
            print(" ")
            time.sleep(3)
            print("Come back to try again")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "ice beam":
        print("Brione uses Ice Beam!")
        print(" ")
        print("It is super effective against Crobat, it faints!")
        print(" ")
        print("You win!, you recieve the Fuchsia City badge from Janine!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        print(f'You are {gym_badges}/8 of the way to become the champion!')
        print(" ")
        time.sleep(3)
        stage_passed.append("poison gym")
        gyms.remove("poison gym")
        if gym_badges == 8:
            end()
        else:
            reset()
def gym_5_dartrix():
    global gym_badges
    global stage_passed
    global gyms
    global rowlet_move
    print("You throw out your partner, Dartrix!")
    print(" ")
    time.sleep(3)
    print(f'Your Dartrix knows the following moves: {rowlet_move}')
    print(" ")
    time.sleep(3)
    user_choice = (str(input("What move would you like Dartrix to use? ")).lower()).strip()
    print(" ")
    time.sleep(3)
    if user_choice == "spirit shackle":
        print("Dartrix used Spirit Shackle, Spirit Shackle is effective against Crobat")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("Dartrix wins!, Crobat could not handle the sheer power of Spirit Shackle, it fainted")
            print(" ")
            time.sleep(3)
            print("You recieve the Fuchsia City badge from Janine!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            stage_passed.append("poison gym")
            gyms.remove("poison gym")
            print(f'You are {gym_badges}/8 of the way to become the champion!')
            print(" ")
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Dartrix looses, Crobat poisoned Dartrix by using Cross-Poison, it fainted.")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()

    elif user_choice == "fly":
        print("Datrix uses Fly!, it is effective against Crobat!")
        print(" ")
        time.sleep(3)
        print("Dartrix wins!, As Dartrix flies towards Crobat at high speeds, it does a lot of damage to Crobat, as a result, it faints")
        print(" ")
        time.sleep(3)
        print("You recieve the Fuchsia City badge from Janine")
        print(" ")
        gym_badges+=1
        time.sleep(3)
        stage_passed.append("poison gym")
        gyms.remove("poison gym")
        print(f'You are now {gym_badges}/8 of the way to become the champion!')
        print(" ")
        time.sleep(3)
        if gym_badges == 8:
            end()
        else:
            reset()
    elif user_choice == "razor leaf":
        print("Dartrix uses Razor Leaf!, it is effective against Crobat!")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("Dartrix wins!, Crobat fainted!")
            print(" ")
            time.sleep(3)
            print("You recieve the Fuchsia City badge from Janine!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            stage_passed.append("poison gym")
            gyms.remove("poison gym")
            print(f'You are now {gym_badges} of the way to become the champion!')
            print(" ")
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Dartrix looses, Crobat poisoned Dartrix by using Cross-Poison, it fainted.")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "earthquake":
        print("Dartrix used Earthquake!, it is super effective against Crobat!.")
        print(" ")
        time.sleep(3)
        print("Dartrix looses as Crobat is not affected by Earthquake, Crobat poisoned Dartrix by using Cross-Poison, it faints!")
        print(" ")
        time.sleep(3)
        print("Come back to try again!")
        print(" ")
        time.sleep(3)
        reset()


def gym_6():
    global gym_badges
    global user_choice1
    global stage_passed
    print(" ")
    print("You arrive at the psychic gym in Saffron City!")
    print(" ")
    time.sleep(3)
    print("You meet the gym leader Sabrina!")
    print(" ")
    time.sleep(3)
    print("You ask Sabrina for a gym battle, she accepts your challenge and the battle begins!")
    print(" ")
    time.sleep(3)
    print("She throws out her partner Alakazam!")
    if user_choice1 == "litten":
        gym_6_torracat()
    elif user_choice1 == "popplio":
        gym_6_brione()
    elif user_choice1 == "rowlet":
        gym_6_dartrix()
    else:
        print("Try again!")
        reset()

def gym_6_torracat():
    global gym_badges
    global stage_passed
    global gyms
    global litten_move
    print(" ")
    print("You throw out your partner, Torracat!")
    print(" ")
    time.sleep(3)
    print("As Torracat is a fire type, it is effective against Alakazam!")
    print(" ")
    time.sleep(3)
    print(f'Your Torracat knows the following moves: {litten_move}')
    print(" ")
    time.sleep(3)
    user_choice = (str(input("What move would you like Torracat to use? ")).lower()).strip()
    if user_choice == "darkest lariat":
        print(" ")
        print("Torracat used Darkest Lariat!")
        print(" ")
        time.sleep(3)
        print("This move is super effective against Alakazam!")
        print(" ")
        time.sleep(3)
        print("You win!, Alakazam could not survive the power of Darkest Lariat!")
        print(" ")
        time.sleep(3)
        print("You recieve the Saffron City badge from Sabrina!")
        gym_badges+=1
        print(" ")
        time.sleep(3)
        gyms.remove("psychic gym")
        stage_passed.append("psychic gym")
        print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
        time.sleep(3)
        if gym_badges == 8:
            end()
        else:
            reset()
    elif user_choice == "ember":
        print(" ")
        print("Torracat used Ember!")
        print(" ")
        time.sleep(3)
        print("Ember is effective against Alakazam")
        time.sleep(3)
        print(" ")
        if random.randrange(1,3) == 1:
            print("You win!, Torracat gave Alakazam a burn from its Ember! It fainted")
            print(" ")
            time.sleep(3)
            print("You recieve the Saffrom city badge from Sabrina!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("psychic gym")
            stage_passed.append("psychic gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Torracat looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "flamethrower":
        print(" ")
        print("Torracat used Flamethrower")
        print(" ")
        time.sleep(3)
        print("Flamethrower is effective against Alakazam!")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("You win!, Torracat gave Alakazam a burn from its Flamethrower! It fainted")
            print(" ")
            time.sleep(3)
            print("You recieve the Saffrom city badge from Sabrina!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("psychic gym")
            stage_passed.append("psychic gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Torracat looses")
            time.sleep(3)
            print(" ")
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "fire fang":
        print(" ")
        print("Torracat used Fire Fang!")
        print(" ")
        time.sleep(3)
        print("Fire Fang is effective against Alakazam")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("You win!, Torracat gave Alakazam a burn from its Fire Fang!")
            print(" ")
            time.sleep(3)
            print("You recieve the Saffrom city badge from Sabrina!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("psychic gym")
            stage_passed.append("psychic gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Torracat looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
def gym_6_brione():
    global gym_badges
    global stage_passed
    global gyms
    global popplio_move
    print(" ")
    print("You throw out your partner, Brione!")
    print(" ")
    time.sleep(3)
    print("As Brione is a water type, it is effective against Alakazam!")
    print(" ")
    time.sleep(3)
    print(f'Your Brione knows the following moves: {popplio_move}')
    print(" ")
    time.sleep(3)
    user_choice = (str(input("What move would you like Brione to use? ")).lower()).strip()
    time.sleep(3)
    if user_choice == "sparkling aria":
        print("Brione used Sparkling Aria!")
        print(" ")
        time.sleep(3)
        print("Sparkling Aria is effective against Alakazam!")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("You win!, Alakazam got absorbed by Brione's Sparkling Aria, it faints!")
            print(" ")
            time.sleep(3)
            print("You recieve the Saffron City badge from Sabrina!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            stage_passed.append("psychic gym")
            gyms.remove("psychic gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                    end()
            else:
                reset()
        else:
            print(" ")
            print("Brione looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "bubble":
        print(" ")
        print("Brione used Bubble!")
        print(" ")
        time.sleep(3)
        print("Bubble is effective against Alakazam")
        print(" ")
        time.sleep(3)
        print("Unfortunately, Bubble is not strong enough to do damage to Alakazam as it uses Psychic, Brione faints!")
        print(" ")
        time.sleep(3)
        print("Come back to try again!")
        print(" ")
        time.sleep(3)
        reset()
    elif user_choice == "water gun":
        print(" ")
        print("Brione used Water gun!")
        print(" ")
        time.sleep(3)
        print("Water gun is effective against Alakazam!")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("Brione wins!, Alakazam could not handle the power of Brione's water gun!")
            print(" ")
            time.sleep(3)
            print("You recieve the Saffron City badge from Sabrina!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("psychic gym")
            stage_passed.append("psychic gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                 reset()
        else:
            print(" ")
            print("Brione looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()

    elif user_choice == "ice beam":
        print("Brione uses Ice Beam!")
        print(" ")
        print("It is effective against Alakazam, it faints!")
        print(" ")
        print("You win!, you recieve the Saffron City badge from Sabrina!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        print(f'You are {gym_badges}/8 of the way to become the champion!')
        print(" ")
        time.sleep(3)
        stage_passed.append("psychic gym")
        gyms.remove("psychic gym")
        if gym_badges == 8:
            end()
        else:
            reset()
            
    else:
        print("Try Again!")
        reset()


def gym_6_dartrix():
    global gym_badges
    global stage_passed
    global gyms
    global rowlet_move
    print(" ")
    print("You throw out your partner, Dartrix!")
    print(" ")
    time.sleep(3)
    print("As Dartrix is a grass type, it is effective against Alakazam!")
    print(" ")
    time.sleep(3)
    print(f'Your Dartrix knows the following moves: {rowlet_move}')
    print(" ")
    time.sleep(3)
    user_choice = (str(input("What move would you like Dartrix to use? ")).lower()).strip()
    if user_choice == "earthquake":
        print("Dartrix used Earthquake!")
        print(" ")
        time.sleep(3)
        print("It is effective against Alakazam!")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print(" ")
            print("You win!, Earthquake is too powerful for Alakazam to handle, it faints!")
            print(" ")
            time.sleep(3)
            print("You recieve the Saffron City badge from Sabrina!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("psychic gym")
            stage_passed.append("psychic gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print(" ")
            print("Dartrix looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "fly":
        print("Dartrix used Fly")
        print(" ")
        time.sleep(3)
        print("It is effective against Alakazam!")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print(" ")
            print("You win!, As Dartrix flies in towards Alakazam, it gets a direct hit, Alakazam faints!")
            print(" ")
            time.sleep(3)
            print("You recieve the Saffron City badge from Sabrina!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("psychic gym")
            stage_passed.append("psychic gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print(" ")
            print("Dartrix looses, Alakazam uses Psychic, it faints!")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "razor leaf":
        print(" ")
        print("Dartrix used Razor Leaf!")
        print(" ")
        time.sleep(3)
        print("Razor Leaf is effective against Alakazam!")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print(" ")
            print("You win!, Razor Leaf is too powerful for Alakazam to handle, it faints!")
            print(" ")
            time.sleep(3)
            print("You recieve the Saffron City badge from Sabrina!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("psychic gym")
            stage_passed.append("psychic gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print(" ")
            print("Dartrix looses!, Alakazam uses Psychic which is too powerful for Dartrix to handle, it faints!")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "spirit shackle":
        print(" ")
        print("Dartrix used Spirit Shackle!")
        print(" ")
        time.sleep(3)
        print("Spirit Shackle is super effective against Alakazam!")
        print(" ")
        time.sleep(3)
        print("You win!, Alakazam faints as Spirit Shackle is too powerful for it to handle!")
        print(" ")
        time.sleep(3)
        print("You recieve the Saffron City badge from Sabrina!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        gyms.remove("psychic gym")
        stage_passed.append("psychic gym")
        print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
        time.sleep(3)
        if gym_badges == 8:
            end()
        else:
            reset()
            
def gym_7():
    global user_choice1
    if user_choice1 == "litten":
        now = "Torracat"
        evolution = "Incineroar"
    elif user_choice1 == "popplio":
        evolution = "Primirina"
        now = "Brione"
    elif user_choice1 == "rowlet":
        evolution = "Decidueye"
        now = "Dartrix"
    print("As you make your way to Cinnabar Island, you battle tons of pokemon!")
    print(" ")
    time.sleep(3)
    print(f'You notice that something strange is happening to {now}, looks like it is evolving!')
    print(" ")
    time.sleep(3)
    print(f'Your partner has now evolved from {now} to {evolution}!')
    print(" ")
    time.sleep(3)
    print("You arrive in Cinnabar Island to challenge the Fire Gym!")
    print(" ")
    time.sleep(3)
    print("You meet the Cinnabar Island gym leader, Blaine!")
    print(" ")
    time.sleep(3)
    print("As you tell him that you are here to challenge him, he accepts it and the battle begins!")
    print(" ")
    time.sleep(3)
    print("Gym leader Blaine throws out his partner, Arcanine!")
    time.sleep(3)
    if user_choice1 == "litten":
        gym_7_incineroar()
    elif user_choice1 == "popplio":
        gym_7_primirina()
    elif user_choice1 == "rowlet":
        gym_7_decidueye()
    else:
        print("Try again!")

def gym_7_incineroar():
    global gym_badges
    global stage_passed
    global gyms
    global litten_move
    print(" ")
    print("You throw out your partner, Incineroar!")
    print(" ")
    time.sleep(3)
    print("As Incineroar is a fire type, it is effective against Arcanine!")
    print(" ")
    time.sleep(3)
    print(f'Your Incineroar knows the following moves: {litten_move}')
    time.sleep(3)
    user_choice = (str(input("What move would you like Incineroar to use? ")).lower()).strip()
    if user_choice == "darkest lariat":
        print(" ")
        print("Incineroar used Darkest Lariat!")
        print(" ")
        time.sleep(3)
        print("This move is effective against Arcanine!")
        print(" ")
        time.sleep(3)
        print("You win!, Arcanine could not survive the power of Darkest Lariat!")
        print(" ")
        time.sleep(3)
        print("You recieve the Cinnabar Island badge from Blaine!")
        gym_badges+=1
        print(" ")
        time.sleep(3)
        gyms.remove("fire gym")
        stage_passed.append("fire gym")
        print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
        time.sleep(3)
        if gym_badges == 8:
            end()
        else:
            reset()
    elif user_choice == "ember":
        print(" ")
        print("Incineroar used Ember!")
        print(" ")
        time.sleep(3)
        print("Ember is not very effective against Arcanine")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("You win!, Incineroar gave Arcanine a burn from its Ember! It fainted")
            print(" ")
            time.sleep(3)
            print("You recieve the Cinnabar Island badge from Blaine!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("fire gym")
            stage_passed.append("fire gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print(" ")
            print("Incineroar looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "flamethrower":
        print(" ")
        print("Incineroar used Flamethrower")
        print(" ")
        time.sleep(3)
        print("Flamethrower is effective against Arcanine!")
        time.sleep(3)
        print(" ")
        if random.randrange(1,3) == 1:
            print("You win!, Incineroar gave Arcanine a burn from its Flamethrower! It fainted")
            print(" ")
            time.sleep(3)
            print("You recieve the Cinnabar Island badge from Blaine!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("fire gym")
            stage_passed.append("fire gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Incineroar looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "fire fang":
        print(" ")
        print("Incineroar used Fire Fang!")
        print(" ")
        time.sleep(3)
        print("Fire Fang is not very effective against Arcanine")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("You win!, Incineroar gave Arcanine a burn from its Fire Fang!")
            print(" ")
            time.sleep(3)
            print("You recieve the Cinnabar Island badge from Blaine!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("fire gym")
            stage_passed.append("fire gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Incineroar looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    
                      


def gym_7_primirina():
    global gym_badges
    global stage_passed
    global gyms
    global popplio_move
    print(" ")
    print("You throw out your partner, Primirina!")
    print(" ")
    time.sleep(3)
    print("As Primirina is a water type, it is super effective against Arcanine!")
    print(" ")
    time.sleep(3)
    print(f'Your Primirina knows the following moves: {popplio_move}')
    print(" ")
    time.sleep(3)
    user_choice = (str(input("What move would you like Primirina to use? ")).lower()).strip()
    time.sleep(3)
    if user_choice == "sparkling aria":
        print("Primirina used Sparkling Aria!")
        print(" ")
        time.sleep(3)
        print("Sparkling Aria is super effective against Arcanine!")
        print(" ")
        time.sleep(3)
        print("You win!, Arcanine got absorbed by Brione's Sparkling Aria, it faints!")
        print(" ")
        time.sleep(3)
        print("You recieve the Cinnabar Island badge from Blaine!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        stage_passed.append("fire gym")
        gyms.remove("fire gym")
        print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
        time.sleep(3)
        if gym_badges == 8:
            end()
        else:
            reset()
    elif user_choice == "bubble":
        print(" ")
        print("Primirina used Bubble!")
        print(" ")
        time.sleep(3)
        print("Bubble is super effective against Arcanine")
        print(" ")
        time.sleep(3)
        print("You win!, Bubble does too much damage to Arcanine, it faints!")
        print(" ")
        time.sleep(3)
        print("You recieve the Cinnabar Island badge from Blaine!")
        time.sleep(3)
        gym_badges+=1
        stage_passed.append("fire gym")
        gyms.remove("fire gym")
        print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
        time.sleep(3)
        if gym_badges == 8:
            end()
        else:
            reset()
    elif user_choice == "water gun":
        print(" ")
        print("Primirina used Water gun!")
        print(" ")
        time.sleep(3)
        print("Water gun is super effective against Arcanine!")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("Primirina wins!, Arcanine could not handle the power of Primirina's water gun!")
            print(" ")
            time.sleep(3)
            print("You recieve the Cinnabar Island badge from Blaine!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("fire gym")
            stage_passed.append("fire gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
                
    elif user_choice == "ice beam":
        print("Primirina uses Ice Beam!")
        print(" ")
        print("It is super effective against Arcanine, it faints!")
        print(" ")
        print("You win!, you recieve the Cinnabar Island badge from Blaine!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        print(f'You are {gym_badges}/8 of the way to become the champion!')
        print(" ")
        time.sleep(3)
        stage_passed.append("fire gym")
        gyms.remove("fire gym")
        if gym_badges == 8:
            end()
        else:
            reset()
        
    else:
        print("Try Again!")
        reset()



def gym_7_decidueye():
    global gym_badges
    global stage_passed
    global gyms
    global rowlet_move
    print(" ")
    print("You throw out your partner, Decidueye!")
    print(" ")
    time.sleep(3)
    print("As Decidueye is a grass type, it is effective against Arcanine!")
    print(" ")
    time.sleep(3)
    print(f'Your Decidueye knows the following moves: {rowlet_move}')
    print(" ")
    time.sleep(3)
    user_choice = (str(input("What move would you like Dartrix to use? ")).lower()).strip()
    time.sleep(3)
    if user_choice == "earthquake":
        print("Decidueye used Earthquake!")
        print(" ")
        time.sleep(3)
        print("It is super effective against Arcanine!")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print(" ")
            print("You win!, Earthquake is too powerful for Arcanine to handle, it faints!")
            print(" ")
            time.sleep(3)
            print("You recieve the Cinnabar Island badge from Blaine!")
            print(" ")
            time.sleep(3)            
            gym_badges+=1
            gyms.remove("fire gym")
            stage_passed.append("fire gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print(" ")
            print("Decidueye looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "fly":
        print("Decidueye used Fly")
        print(" ")
        time.sleep(3)
        print("It is effective against Arcanine!")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print(" ")
            print("You win!, As Decidueye flies in towards Arcanine, it gets a direct hit, Arcanine faints!")
            print(" ")
            time.sleep(3)
            print("You recieve the Cinnabar Island badge from Blaine!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("fire gym")
            stage_passed.append("fire gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print(" ")
            print("Decidueye looses, Alakazam uses Psychic, it faints!")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "razor leaf":
        print(" ")
        print("Decidueye used Razor Leaf!")
        print(" ")
        time.sleep(3)
        print("Razor Leaf is not very effective against Arcanine!")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print(" ")
            print("You win!, Razor Leaf is too powerful for Alakazam to handle even though it is not very effective against Arcanine, it faints!")
            print(" ")
            time.sleep(3)
            print("You recieve the Cinnabar Island badge from Blaine!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("fire gym")
            stage_passed.append("fire gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print(" ")
            print("Decidueye looses!, Alakazam uses Psychic which is too powerful for Dartrix to handle, it faints!")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "spirit shackle":
        print(" ")
        print("Dartrix used Spirit Shackle!")
        print(" ")
        time.sleep(3)
        print("Spirit Shackle is effective against Alakazam!")
        print(" ")
        time.sleep(3)
        print("You win!, Alakazam faints as Spirit Shackle is too powerful for it to handle!")
        print(" ")
        time.sleep(3)
        print("You recieve the Cinnabar Island badge from Blaine!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        gyms.remove("fire gym")
        stage_passed.append("fire gym")
        print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
        time.sleep(3)
        if gym_badges == 8:
            end()
        else:
            reset()


def gym_8():
    global user_choice1
    print(" ")
    print("You arrive at the Ground gym in Veridian City!")
    print(" ")
    time.sleep(3)
    print("You meet the Veridian City gym leader, Giovanni!")
    print(" ")
    time.sleep(3)
    print("You ask Giovanni for a battle, he accepts your challenge and the battle begins!")
    print(" ")
    time.sleep(3)
    print("Giovanni throws out his partner, MEWTWO!")
    print(" ")
    time.sleep(3)
    print("Mewtwo is a legendary pokemon which in very powerful")
    print(" ")
    time.sleep(3)
    if user_choice1 == "litten":
        gym_8_incineroar()
    elif user_choice1 == "popplio":
        gym_8_primirina()
    elif user_choice1 == "rowlet":
        gym_8_decidueye()
    else:
        print("Try again!")


def gym_8_incineroar():
    global gym_badges
    global stage_passed
    global gyms
    global litten_move
    print(" ")
    print("You throw out your partner, Incineroar!")
    print(" ")
    time.sleep(3)
    print("As Incineroar is a fire type, it is effective against Mewtwo!")
    print(" ")
    time.sleep(3)
    print(f'Your Incineroar knows the following moves: {litten_move}')
    print(" ")
    time.sleep(3)
    user_choice = (str(input("What move would you like Incineroar to use? ")).lower()).strip()
    time.sleep(3)
    if user_choice == "darkest lariat":
        print(" ")
        print("Incineroar used Darkest Lariat!")
        print(" ")
        time.sleep(3)
        print("This move is super effective against Mewtwo!")
        print(" ")
        time.sleep(3)
        print("You win!, Mewtwo could not survive the power of Darkest Lariat!")
        print(" ")
        time.sleep(3)
        print("You recieve the Veridian City badge from Giovanni!")
        time.sleep(3)
        gym_badges+=1
        print(" ")
        gyms.remove("ground gym")
        stage_passed.append("ground gym")
        print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
        time.sleep(3)
        if gym_badges == 8:
            end()
        else:
            reset()
    elif user_choice == "ember":
        print(" ")
        print("Incineroar used Ember!")
        print(" ")
        time.sleep(3)
        print("Ember is not very effective against Mewtwo")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("You win!, Incineroar gave Mewtwo a serious burn from its Ember! It fainted")
            print(" ")
            time.sleep(3)
            print("You recieve the Veridian City badge from Giovanni!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("ground gym")
            stage_passed.append("ground gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print(" ")
            print("Incineroar looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "flamethrower":
        print(" ")
        print("Incineroar used Flamethrower")
        print(" ")
        time.sleep(3)
        print("Flamethrower is effective against Mewtwo!")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print(" ")
            print("You win!, Incineroar gave Mewtwo a burn from its Flamethrower! It fainted")
            print(" ")
            time.sleep(3)
            print("You recieve the Veridian City badge from Giovanni!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("ground gym")
            stage_passed.append("ground gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Incineroar looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "fire fang":
        print(" ")
        print("Incineroar used Fire Fang!")
        print(" ")
        time.sleep(3)
        print("Fire Fang is effective against Mewtwo")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("You win!, Incineroar gave Mewtwo a serious burn from its Fire Fang!")
            print(" ")
            time.sleep(3)
            print("You recieve the Veridian City badge from Giovanni!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("ground gym")
            stage_passed.append("ground gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print("Incineroar looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()


def gym_8_primirina():
    global gym_badges
    global stage_passed
    global gyms
    global popplio_move
    print(" ")
    print("You throw out your partner, Primirina!")
    print(" ")
    time.sleep(3)
    print("As Primirina is a water type, it is effective against Mewtwo!")
    print(" ")
    time.sleep(3)
    print(f'Your Primirina knows the following moves: {popplio_move}')
    print(" ")
    time.sleep(3)
    user_choice = (str(input("What move would you like Primirina to use? ")).lower()).strip()
    time.sleep(3)
    if user_choice == "sparkling aria":
        print("Primirina used Sparkling Aria!")
        print(" ")
        time.sleep(3)
        print("Sparkling Aria is effective against Mewtwo!")
        print(" ")
        time.sleep(3)
        print("You win!, Arcanine got absorbed by Primirina's Sparkling Aria, it faints!")
        print(" ")
        time.sleep(3)
        print("You recieve the Veridian City badge from Giovanni!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        stage_passed.append("ground gym")
        gyms.remove("ground gym")
        print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
        time.sleep(3)
        if gym_badges == 8:
            end()
        else:
            reset()
    elif user_choice == "bubble":
        print(" ")
        print("Primirina used Bubble!")
        print(" ")
        time.sleep(3)
        print("Bubble is effective against Mewtwo")
        print(" ")
        time.sleep(3)
        print("You win!, Bubble does too much damage to Mewtwo, it faints!")
        print(" ")
        time.sleep(3)
        print("You recieve the Cinnabar Island badge from Blaine!")
        time.sleep(3)
        print(" ")
        gym_badges+=1
        stage_passed.append("ground gym")
        gyms.remove("ground gym")
        print(f'ou are now {gym_badges}/8 of the way of becoming the champion!')
        time.sleep(3)
        if gym_badges == 8:
            end()
        else:
            reset()
    elif user_choice == "water gun":
        print(" ")
        print("Primirina used Water gun!")
        print(" ")
        time.sleep(3)
        print("Water gun is effective against Mewtwo!")
        print(" ")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print("Primirina wins!, Mewtwo could not handle the power of Primirina's water gun!")
            print(" ")
            time.sleep(3)
            print("You recieve the Veridian City badge from Giovanni!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("ground gym")
            stage_passed.append("ground gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
    elif user_choice == "ice beam":
        print(" ")
        print("Primirina used Ice Beam!")
        print(" ")
        time.sleep(3)
        print("Ice Beam is effective against Mewtwo")
        print(" ")
        time.sleep(3)
        print("You win!, Mewtwo is frozen by Ice Beam, it faints!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        gyms.remove("ground gym")
        stage_passed.append("ground gym")
        print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
        time.sleep(3)
    else:
        print("Try Again!")
        reset()
                      

def gym_8_decidueye():
    global gym_badges
    global stage_passed
    global gyms
    global rowlet_move
    print(" ")
    print("You throw out your partner, Decidueye!")
    print(" ")
    time.sleep(3)
    print("As Decidueye is a grass type, it is effective against Mewtwo!")
    print(" ")
    time.sleep(3)
    print(f'Your Decidueye knows the following moves: {rowlet_move}')
    print(" ")
    time.sleep(3)
    user_choice = (str(input("What move would you like Decidueye to use? ")).lower()).strip()
    time.sleep(3)
    if user_choice == "earthquake":
        print("Decidueye used Earthquake!")
        print(" ")
        time.sleep(3)
        print("It is effective against Mewtwo!")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print(" ")
            print("You win!, Earthquake is too powerful for Mewtwo to handle, it faints!")
            print(" ")
            time.sleep(3)
            print("You recieve the Veridian City badge from Giovanni!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("ground gym")
            stage_passed.append("ground gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print(" ")
            print("Decidueye looses")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "fly":
        print("Decidueye used Fly")
        print(" ")
        time.sleep(3)
        print("It is effective against Mewtwo!")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print(" ")
            print("You win!, As Decidueye flies in towards Mewtwo, it gets a direct hit, Arcanine faints!")
            print(" ")
            time.sleep(3)
            print("You recieve the Veridian City badge from Giovanni!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("ground gym")
            stage_passed.append("ground gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print(" ")
            print("Decidueye looses, Mewtwo uses Psychic, it faints!")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "razor leaf":
        print(" ")
        print("Dartrix used Razor Leaf!")
        print(" ")
        time.sleep(3)
        print("Razor Leaf is effective against Mewtwo!")
        time.sleep(3)
        if random.randrange(1,3) == 1:
            print(" ")
            print("You win!, Razor Leaf is too powerful for Mewtwo to handle, it faints!")
            print(" ")
            time.sleep(3)
            print("You recieve the Veridian City badge from Giovanni!")
            print(" ")
            time.sleep(3)
            gym_badges+=1
            gyms.remove("ground gym")
            stage_passed.append("ground gym")
            print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
            time.sleep(3)
            if gym_badges == 8:
                end()
            else:
                reset()
        else:
            print(" ")
            print("Decidueye looses!, Mewtwo uses Psychic which is too powerful for Dartrix to handle, it faints!")
            print(" ")
            time.sleep(3)
            print("Come back to try again!")
            print(" ")
            time.sleep(3)
            reset()
    elif user_choice == "spirit shackle":
        print(" ")
        print("Dartrix used Spirit Shackle!")
        print(" ")
        time.sleep(3)
        print("Spirit Shackle is effective against Mewtwo!")
        print(" ")
        time.sleep(3)
        print("You win!, Mewtwo faints as Spirit Shackle is too powerful for it to handle!")
        print(" ")
        time.sleep(3)
        print("You recieve the Veridian City badge from Giovanni!")
        print(" ")
        time.sleep(3)
        gym_badges+=1
        gyms.remove("ground gym")
        stage_passed.append("ground gym")
        print(f'You are now {gym_badges}/8 of the way of becoming the champion!')
        time.sleep(3)
        if gym_badges == 8:
            end()
        else:
            reset()


def end():
    print(" ")
    print("Congratulations!! You are now the Champion of the Kanto Region!")
    print(" ")
    time.sleep(3)
    print("You have earned this title by beating all of the 8 gyms!") 
    sys.exit()

call()
