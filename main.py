import json
from difflib import get_close_matches as cm

# Opening the file with the dictionary of words
data = json.load(open('data.json'))

def main():
    print('This program will ask for a word and give a definition of the word if found in the dicitonary.')
    print()
    word = input("Enter a word to get the definition(s): ").lower() # Getting user input and converting the word to lower case 
    if word.title() in data:  # Checking to see if the capital version of the word exists in the data dictionary and making the word capitalized if so
        word = word.title()
    if word in data:  # If an exact match is made, print out the definition(s)
        print()
        print(f"The following are the definition(s) of the word: {word}")
        print()
        print("=========================================================")
        output = data[word]
        index = 1  # Index for print output with definition numbering
        for sent in output:  # For loop to cycle through the different definitions
            print(f"{index}: {sent}")
            index += 1
        print("=========================================================")
        print()
        

    else:
        result = close_match(word) # Using the difflib(get_close_match) module to get the closest word to what was entered
        if result == []:  # if no similair words were found, let the user know
            print()
            print("No words found similiar to what was entered, please try again.")
        else:
            # Asking user if they meant the closest found word in the dict.
            user_conf = input(f'Did you mean "{result}"? Enter "Y" for yes or "N" for no: ').lower() 

            while user_conf != 'y' and user_conf != 'n':  # input validation for yes or no statement 
                user_conf = input(f'Did you mean "{result}"? Enter "Y" for yes or "N" for no: ').lower()

            if user_conf == 'y':  # If user wanted definition of the closest found word, return it for printing
                print()
                print(f"The following are the definition(s) of the word: {result}")
                print()
                print("=========================================================")
                output = data[result]
                index = 1  # Index for print output with definition numbering
                for sent in output:  # For loop to cycle through the different definitions
                    print(f"{index}: {sent}")
                    index += 1
                print("=========================================================")
                print()
            else:  # Let user know word was not found if "no" was entered
                print()
                print("The word was not found, please try again.")


def close_match(word):
    # Using the get_close_matches module from difflib to get closest word match and if none returning an empty string.
    try:
        result = cm(word, data.keys())[0]
        return result
    except IndexError:
        return []


# Calling the main function 
main()
