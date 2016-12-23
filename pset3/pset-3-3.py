def getAvailableLetters(lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
   
    #creating a string of alphabet
    import string
    orig_alpha = string.ascii_lowercase
    
    for letter in lettersGuessed:
        if letter in orig_alpha:
            orig_alpha = orig_alpha.replace(letter,"")
    return orig_alpha

    
print(getAvailableLetters(['h', 'a', 'u',\
 'd', 'i', 'm', 'n', 'r', 't', 'u']))
 

