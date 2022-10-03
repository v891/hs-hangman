import random
import string


def print_board(word, tries):
    print()
    print(''.join(['-' if c not in tries else c for c in list(word)]))


won = 0
lost = 0
print('H', 'A', 'N', 'G', 'M', 'A', 'N')
while True:
    menu_option = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')

    if menu_option == "exit":
        break
    elif menu_option == "results":
        print(f'You won: {won} times')
        print(f'You lost: {lost} times')
    else:
        my_list = ['python', 'java', 'swift', 'javascript']
        ran_choice = random.choice(my_list)
        set_ran_choice = set(ran_choice)
        letter_set = set()
        bad_set = set()
        nu_tries = 0
        alphabet_string = string.ascii_lowercase

        while nu_tries < 8:
            print_board(ran_choice, letter_set)
            letter = input("Input a letter: ")

            if len(letter) != 1:
                print("Please, input a single letter.")
            elif letter not in alphabet_string:
                print("Please, enter a lowercase letter from the English alphabet.")
            elif letter in letter_set or letter in bad_set:
                print("You've already guessed this letter.")
            elif letter not in ran_choice:
                print("That letter doesn't appear in the word.")
                bad_set.add(letter)
                nu_tries += 1
            else:
                letter_set.add(letter)
                if set_ran_choice == letter_set:
                    print()
                    print("You guessed the word " + ran_choice + "!")
                    print("You survived!")
                    won += 1
                    break
        else:
            print()
            print("you lost!")
            lost += 1
