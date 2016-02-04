import string

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alpha = string.ascii_lowercase
    wordsleft=''
    for letter in alpha:
        if letter not in lettersGuessed:
            wordsleft+= letter
    return wordsleft



print (getAvailableLetters(lettersGuessed))


