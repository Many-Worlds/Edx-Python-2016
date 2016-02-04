import string

secretWord = 'apple'
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    swl = len(secretWord)
    hypen = '-------------'
    guesses = 8
    avaibl = string.ascii_lowercase
    lettersGuessed= ''
    lettersleft =''

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ',swl,' letters long.'


    while guesses > 0:
        print hypen
        print 'You have ',guesses,' left.'
        for letter in avaibl:
            if letter in lettersGuessed:
                avaibl = avaibl.replace(letter,'')         
        print 'Available letters: :',avaibl
        guess=str(raw_input("Please guess a letter: ")).lower()
        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter: "
        if guess not in lettersGuessed:
            if guess in secretWord:
                result = ''
                for letter in secretWord:
                    if letter in lettersGuessed:
                        result = result + letter
                    else:
                        result = result + '_'
                print 'Good Job : ' +result   

hangman(secretWord)