import random

WORDS = ['PYTHON', 'PROJECT', 'HELLO', 'SAMURAI']


def game():
    print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    game start!!!
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    is_continue = "y"
    while is_continue == "y" or is_continue == "Y":
        word = random.choice(WORDS)
        answer = word
        jumble = ""
        while word:
            position = random.randrange(len(word))
            jumble += word[position]
            word = word[:position] + word[position + 1:]
        print('After shuffling, the word is: ' + jumble)
        guess = input("\n please guess: ")
        while guess != answer and guess != "":
            print("you are wrong.")
            guess = input("\n please guess: ")
            if guess == answer:
                print("Good Job, Game Over")
                break


if __name__ == '__main__':
    game()
