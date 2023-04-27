
from random import choice
from words import words_list
from hangman_figure import hangman_figure

run_command = True

print("")
while run_command:
    guessed = False
    tries = 6

    question = choice(words_list).lower()

    question_as_array = []
    guessed_letter = []
    guessed_letter_str = ''
    word_completion = '_' * len(question)

    while not guessed and tries > 0: 
        user_input = input('Guess a letter: ').lower()
        if len(user_input) > 1:
            print('Enter a single letter!')
            print("")
            user_input = input('Guess a letter: ').lower()
        if user_input.isalpha == False:
            print('Enter an alphabet dumbo!')
            print("")
            user_input = input('Guess a letter: ').lower()
        
        for letter in question:
            question_as_array.append(letter) 
        word_as_list = list(word_completion)
        
        if user_input in guessed_letter:
            print("")
            print("You've already tried it. Try something else")
            
        elif user_input in str(question_as_array).lower():
            guessed_letter.append(user_input)
            print(f'Great Job! You guess the letter {user_input} right!')
            indices = [i for i, letter in enumerate(question) if letter == user_input]
            for index in indices:
                word_as_list[index] = user_input
            word_completion = "".join(word_as_list) 
            if "_" not in word_completion:
                    guessed = True
                    print("")
                    print('Congratulations! You Win! 🎉')
        
        elif user_input not in question_as_array:
            tries -= 1
            print(f"'{user_input}' doesn't exist in the word")
            guessed_letter.append(user_input)
        
        for i in guessed_letter:
            guessed_letter_str += i + ', '

        print(hangman_figure[tries])
        print(word_completion)
        print("") 
        print(f'Words Tried: {guessed_letter_str}')
        print("")
        guessed_letter_str = ''
    if tries == 0:
        print("")
        print('You Lose 😔')
        print(f"The word was '{question.title()}'")
        print("") 
    play = input("Type 'e' to end or enter key to continue ").lower()
    
    if play == 'e':
        run_command = False
    print("")
    

print('Alright! Stopped Your Game')
print("")
