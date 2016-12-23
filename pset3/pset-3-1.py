def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    right_letters = []
    
    for letter in lettersGuessed:
        if letter in secretWord:
            right_letters.append(letter)
            
    return len(right_letters) == len(secretWord)

    
print(isWordGuessed('durian', ['h', 'a', 'c',\
 'd', 'i', 'm', 'n', 'r', 't', 'u']))