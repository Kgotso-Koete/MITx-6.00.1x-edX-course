def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    right_letters = []
    num_guesses = 0
    printed_guess = ''   
    
    for letter in lettersGuessed:
        if letter in secretWord:
            right_letters.append(letter) 
            print("Good guess")
        num_guesses += 1
    for c in secretWord:
        if c in right_letters:
            printed_guess += c
        else:
            printed_guess += "_ "
        print(printed_guess)
    return (printed_guess)


    
print(getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']))