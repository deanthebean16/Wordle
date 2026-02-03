"""
******************************
CS 1026A Fall 2025
Assignment 2: Wordle
Created by: Yi Yuan Cheng
Student ID: yche4385
Student Number: 251500424
File created: October 16, 2025
******************************
This file is created to simulate the popular New York Times game "Wordle" where the user has to guess random word in 6 tries. 
"""

from randwords import *

def guess_word(length): 
    user_guess = input("Enter your guess: ") #asks the user for their guess 
    if length == len(user_guess): #Checks that their guess is the same amount of letters as the actual word 
        return user_guess.upper() #Returns the user's guess in all CAPS once the programs verified that the guess is valid 
    else:
        print("Incorrect length") # if it's not the right guess then I return false 
        return False

def check_guess(guess, actual): 
    # Convert to lists 
    guess_list = list(guess)
    actual_list = list(actual)
    output_list = ["^"] * len(actual)  # Start with all carets so it's easier to indicate where to insert
    
    # First pass: Check for exact matches 
    for i in range(len(actual)):
        if guess_list[i] == actual_list[i]:
            output_list[i] = "!"
            # Mark this position as used in actual word
            actual_list[i] = None  # Use None to mark used positions
    
    # Second pass: Check for partial matches 
    for i in range(len(actual)):
        if output_list[i] != "!":  # Only check positions that aren't exact matches
            current_letter = guess_list[i]
            # Check if this letter exists anywhere in the actual word
            if current_letter in actual_list:
                # Find the first available position in actual word
                for j in range(len(actual)):
                    if actual_list[j] == current_letter:
                        output_list[i] = "*"
                        actual_list[j] = None  # Mark this position as used
                        break
    
    return ''.join(output_list)

def play_game(actual=""):   
    guess_count = 1 #start the guess count at 1
    if actual == "": #if the playgame() is empty, then the actual word will be a random word from randwords.py
        randword = get_rand_word()
        print("The length of the word you are guessing is %d letters long" % len(randword))
        while guess_count < 7: 
            print("Guess #%d: " % guess_count, end="")
            user_input = guess_word(len(randword)) #calling the guess_word function inputing the length of the random word 
            if user_input != False: #This means if the user's guess is the correct length, then continue 
                if user_input == randword:  # Check if guess equals actual word
                    print("!" * len(randword))
                    print("You won!")
                    break #break the loop
                else: #since the user has not won yet
                    result = check_guess(user_input, randword)
                    print(result) #print which letters they got wrong/right
                    guess_count += 1 # Take in account how many guesses they've taken 
        if guess_count == 7: #when they reach the max amount of guesses, the loop breaks and let's the user know that they're out of guesses
            print("You Lost!")
            
    else: #if the playgame() is not empty that means the tester has entered their own actual word
        actual_upper = actual.upper()  # Convert to uppercase for consistency
        print("The length of the word you are guessing is %d" % len(actual_upper))
        while guess_count < 7: 
            print("Guess #%d: " % guess_count, end="")
            user_input = guess_word(len(actual_upper))
            if user_input != False: 
                if user_input == actual_upper:  # Check if guess equals actual word
                    print("!" * len(actual_upper))
                    print("You won!")
                    break
                else:
                    result = check_guess(user_input, actual_upper)
                    print(result)
                    guess_count += 1
        if guess_count == 7: 
            print("You lost!")

