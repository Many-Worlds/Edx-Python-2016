secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's','a','l']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE..
    correctguess = 0 
    word = list(secretWord)
    print word
    for letter in secretWord:
        if letter in lettersGuessed:             
            print('In')
            correctguess += 1
            print correctguess
        else: 
             print ('out')

    if correctguess == len(secretWord):
        return True
    else :
        return False


isWordGuessed(secretWord, lettersGuessed)
