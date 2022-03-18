import json
from difflib import get_close_matches as gcm 

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()

    # Returning the words definition when user has entered word correctly. Accounting for capitalization of proper nouns
    if word in data or word.capitalize() in data or word.upper() in data:

        # If the capitalized word is in data, converting to a capitalized word
        if word.capitalize() in data:
            word = word.capitalize()

        # If the upper case word is in data, converting to a upper case word
        if word.upper() in data:
            word = word.upper()

        # Iterating over the list to print out the definitions as strings and not a list object
        user_definition = data[word]
        counter = 1
        return_string = ''
        for i in user_definition:
            return_string += '\n' + str(counter) + '. ' + i 
            counter += 1
        return return_string


    # using difflib get_close_matches to see if word is close to a word in the data
    elif gcm(word.upper(), data.keys(), cutoff=.8) or gcm(word.capitalize(), data.keys(), cutoff=.8) or gcm(word, data.keys(), cutoff=.7):

        # If the captialized word is in the suggested words, convert it to a capitalized word
        if gcm(word.capitalize(), data.keys(), cutoff=.8):
            word = word.capitalize()

        # If the upper cased word is in the suggested words, convert it to a upper case word
        if gcm(word.upper(), data.keys(), cutoff=.8):
            word = word.upper()

        user_input = input("Did you mean %s? Y or N: " % gcm(word, data.keys(), cutoff=.7)[0])

        # If the suggested word is the correct word
        if user_input.lower() == 'y':
            # Iterating over the list to print out the definitions as strings and not a list object
            user_definition =  data[gcm(word, data.keys(), cutoff=.7)[0]]
            counter = 1
            return_string = ''
            for i in user_definition:
                return_string += '\n' + str(counter) + '. ' + i
                counter += 1
            return return_string

        # If suggested word is not correct, return message
        elif user_input.lower() == 'n':
            return "Word not in data, please try again."

        # Catch all for incorrect input
        else:
            return "Incorret input. Please try again."

    # Catch all for incorrect input       
    else:
        return "Word not in data, please try again."


word = input("Enter word for definition: ")
print(translate(word))