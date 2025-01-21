import random

word_list = ["veruc", "unkempt harold", "thunderball fists", "striker", "sledes shotgun", "slagga", "skullmasher", "shreddifier", "pyrophobia", "pithfork", "ogre", "nukem", "norfleet", \
             "mongol", "maggie","Madhouse","lyuda", "longbow", "Logans gun", "kerblaster", "invader", "infinity", "hornet", "hellfire", "hammer buster","gunerang", "gub", \
            "flakker", "emperor", "deliverance", "conference call", "bunny", "bitch", "badaboom", "babymaker"]

def choose_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    word = choose_word(word_list)
    guessed_letters = set()
    attempts = 6

    print("Welcome to the Borderlands 2 Legendary gun guessing game!")
    print(display_word(word, guessed_letters))

    while attempts > 0 and set(word) != guessed_letters:
        guess = input("Please guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter, got the brain of a psycho or something?")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess Vault Hunter! {display_word(word, guessed_letters)}")
        else:
            attempts -= 1
            print(f"Ahhhh, better luck in the next guess. you have {attempts} attempts remaining!")
            print(display_word(word, guessed_letters))
        
    if set(word) == guessed_letters:
        print(f"Congratulations, you guessed the legendary {word}")
    else:
        print(f"Wrong!, the legendary was the {word}! I see you need to go farm some mini bosses vault hunter!")

def main():
    while True:
        play_hangman()
        play_again = input("Would you like to play again Vault hunter?: (yes or no?)").lower()
        if play_again not in ["yes", "y"]:
            print("See ya around!")
            break

main()


