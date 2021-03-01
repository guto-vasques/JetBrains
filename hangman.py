import random

print("H A N G M A N")
def game():
    words = ['python', 'java', 'kotlin', 'javascript']
    answer = random.choice(words)
    size = len(answer)
    secret = list("-"*size)
    parcial = "".join(secret)
    list_answer = list(answer)
    position = []
    tried = []
    tried_wrong = []
    num_guess = 0

    while num_guess < 9:
        print()
        parcial = "".join(secret)
        print(parcial)
        if num_guess < 8:
            guess = input("Input a letter:")
            if len(guess) != 1:
                print("You should input a single letter")
                continue
            if guess in tried:
                print("You've already guessed this letter")
                continue
            if guess.islower() == False or guess.isalpha() == False:
                print("Please enter a lowercase English letter")
                continue
        if guess not in answer:
            print("That letter doesn't appear in the word")
            tried.append(guess)
            tried_wrong.append(guess)
            num_guess += 1
            
        if guess in tried:
            if guess not in tried_wrong:
                print("No improvements")
                num_guess += 1
        
        if guess in answer:
            tried.append(guess)
            for i in range(len(answer)):
                if guess  == answer[i]:
                    secret[i] = guess
            parcial = "".join(secret)
        if parcial == answer:
            print("You guessed the word!")
            print("You survived!")
            num_guess = 10
        if num_guess == 8:
            print("You lost!")
            num_guess = 10
            
while True:
    menu = input('Type "play" to play the game, "exit" to quit:')
    if menu == "play":
        game()
    elif menu == "exit":
        break
