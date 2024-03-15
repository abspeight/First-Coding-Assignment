#Use to establish our ability to use the random function.
import random
#Print function that outputs a welcome sentence to our player.
print("Welcome! I'm happy to see a new player. Shall we proceed Start?")
#Creating a variable that allows us to input our/or the players name.
user1_round1 = input('Please Present Your Name')
#This allows us to print the name of the player.
print(user1_round1)
#our path1 variable allows us to input our path1 choice.
path1 = input('Choose Your Path, Think Wisely.')
#This code cell allows us to use the while function given certain conditions are met.
while path1 != 'N' and path1 !='S' and path1 != 'E' and path1 !='W':
    #Allows us to input our path1 choice again in the case the conditions were not met.
    path1 = input("That Path Doesn't Exist. Try again.")
#our if statement is applied if our path1 input is equal to N.
if path1 == 'N':
#This prints out the word assigned to our variable N. Which is North.
    print('North')
#our first elif statement is applied if our path1 input is equal to S.
elif path1 == 'S':
##This prints out the word assigned to our variable S which is South.
    print('South')
#our second elif statement is applied if our path1 input is equal to W.
elif path1 == 'W':
#This prints out the word assigned to our variable W Which is West.
    print('West')
#Our third elif statement is applied if our path1 input is equal to E.
elif path1 == 'E':
#This prints out the word assigned to our variable E.
    print('East')
#If the input in path1 is N we can executed the next lines of codes.
if path1 == 'N':
#This line of code allows us to input the answer to the following question giving to us.
    answer1 = input('What Casts an Infinite Shadow?')
#This line of code executes if our answer to the previous line of code is correct.
    if answer1 == 'night':
#Outputs a sentence that lets the player know if his answer is correct (congradulates him).
        print('Correct, Let us proceed to the next game.')
#A different condition is applied incase the previous line of code doesn't work.
    else:
#Showing the output that will happen if the code lines above aren't applied.
        print("You've lost the first game. There's still a chance for redemption; let's proceed to the next round.")
#If the input in path1 is S we can executed the next lines of code.
elif path1 == 'S':
#Input an answer to the question given to variable answer1.
    answer1 = input('You use me from your head to toe, the more I work, the smaller I grow.')
#An if statemnet will execute if the input in the line above is the same in this line of code.
    if answer1 == 'soap':
#An output will be printed letting the player know he's right and that he'll play another game.
        print('Correct, Let us proceed to the next game.')
#An else statement will commence if the code cell above doesn't meet the requirments.
    else:
#An output will be printed if the the above lines of code are not satisfied
        print("You've lost the first game. There's still a chance for redemption; let's proceed to the next round.")
#This line of code will be executed if path1 is equal to E.
elif path1 == 'E':
#This code line allows us to input an answer to the question assigned to the variable.
    answer1 = input('I often have a window, and a stamp, when you need to seal me, make my back damp.')
#if the answer in the above code line is the same as the string shoown we will have a statement applied.
    if answer1 == 'envelope':
#This statement will be printed if answer1 is the same as the string assigned to it's question.
        print('Correct, Let us proceed to the next game.')
#This else function allows us to give a condition if the above "if" statement isn't satisfied.
    else:
#A statement will be printed telling the player what happend based off his answer.
        print("You've lost the first game. There's still a chance for redemption; let's proceed to the next round.")
#This elif statement is assigned to the string W in the case that the input in path1 is W.
elif path1 == 'W':
#This variable is used to input an answer to the question assigned to it.
    answer1 = input('After a fall, I decide to take over. Then life starts to stall, or starts to grow slower.')
#This "if" statement allows us to assign a string to our answer in case it's the same string inputed in our variable.
    if answer1 == 'winter':
#This allows us to print an output if the condition to the statment about was satisfied.
        print('Correct, Let us proceed to the next game.')
#This commond allows us to give another condition incase the one above wasn't satisfied.
    else:
#This line of code allows us to print a statement depending on the condition that was satisfied.
        print("You've lost the first game. There's still a chance for redemption; let's proceed to the next round.")
#This code line allows us to output a statement that welcomes the player to the second part of the game.
print("The second portion of the game will start momentarily Please Provide Us With Your name again")
#This variable allows to input the players name again.
user1_round2 = input(' Please Provide Us With Your name again')
#This condition is given to check if the player is the same player from the first game.
if user1_round2 == user1_round1:
#This statement will execute in the case that the player from round one is the same from round two.
    print('Welcome Back', user1_round2)
#This allows us give another condition in case the condition in the previous two lines isn't satisfied.
else:
#This statement will be printed in the case the player isn't the same person.
    print('CHEATER! THIS IS NOT THE SAME PERSON. However, you will take their place. Lets proceed')
#This variable allows us to input another path but under a different variable but with the same conditions as before.
path2 = input('Choose Your Path, Think Wisely')
#This allows us to create a loop in the case that the condtions in this line of code isn't satisfied.
while path2 != 'N' and path2 !='S' and path2 != 'E' and path2 !='W':
#This variable allows us to input a string.
    path2 = input("That Path Doesn't Exist. Try again.")
#our first conditional statement for the path2 of game 2.
if path2 == 'N':
#This statement will be printed if path2 input is N.
    print('North, you get to play another game')
#our second conditional statement for the path2 of game 2.
elif path2 == 'S':
#This statement will be printed if path2 input is N.
    print("South, GAME OVER!")
#our third conditional statement for the path2 of game 2.
elif path2 == 'W':
#This statement will be printed if path2 input is N.
    print("West, GAME OVER!")
#our fourth conditional statement for the path2 of game 2.
elif path2 == 'E':
#This statement will be printed if path2 input is N.
    print("East, GAME OVER!")
#This line will execute if path1 and path2 input are the same (Both are N).
if path1 == 'N' and path2 =='N':
#This will output a statemnet informing the player of the type of game they will play.
    print('We will play a guessing game. Guess the name of one of the seven dwarves.')
#This variable attaches a list with the names related to the 7 dwarves.
    list_names = ['happy', 'doc', 'grumpy', 'dopey', 'bashful', 'sleepy', 'sneezy']
#This variable allows us to input a name.
    guess1 = input('Guess a Name')
#This is a conditional statment that will loop so long as the name inputed in the previous line of code is not one from the list.
    while guess1 != 'happy' and guess1 != 'doc' and guess1 != 'grumpy' and guess1 != 'dopey' and guess1 !='bashful' and guess1 != 'sleepy' and guess1 != 'sneezy':
#This allows us to keep inputing a name till a name from the list above is used.
        guess1= input('Try again. That name is not the name of one of the dwarves.')
#A conditional statemnt if our input is the string 'happy'.
    if guess1 == 'happy':
#This commond will execute if the above condition is meet.
        print('Correct!')
#A conditional statemnt if our input is the string 'doc'.
    elif guess1 == 'doc':
#This commond will execute if the above condition is meet.
        print('Correct!')
#A conditional statemnt if our input is the string 'grumpy'.
    elif guess1 == 'grumpy':
#This commond will execute if the above condition is meet.
        print('Correct!')
#A conditional statemnt if our input is the string 'dopey'
    elif guess1 == 'dopey':
#This commond will execute if the above condition is meet.
        print('Correct!')
#A conditional statemnt if our input is the string 'bashful'.
    elif guess1 == 'bashful':
#This commond will execute if the above condition is meet.
        print('Correct!')
#A conditional statemnt if our input is the string 'sleepy'.
    elif guess1 == 'sleepy':
#This commond will execute if the above condition is meet.
        print('Correct!')
#A conditional statemnt if our input is the string 'sneezy'.
    elif guess1 == 'sneezy':
#This commond will execute if the above condition is meet.
        print('Correct!')
#This allows us to input another name so that we can play the game again
    guess2 = input('lets go again')
#This loop will continue to happen if our first nammed guessed from the list is the same as the second.
    while guess2 == guess1:
#If the the two names are the same the while loop will execute untill we inout a different name for guess2.
        guess2 = input("You've guessed that name already, give me a different one")
#If the name from guess1 is not the same as guess2 then a statemnt will be printed to let the player know he has won the game.
    else:
        print("Correct!, You Have Won The Game. Let's meet with snow white and find the 8th dwarf, Breezy.")
#This condition will execute if the path from game1 is S and the path from game2 is N.
elif path1 == 'S' and path2 == 'N':
#A statement informing the player of the kind of game they will play.
    print('We Will Play a Dice Game')
#This variable allows us to randomly genenrate a number in the range of 1 through 6.
    Dice_roll = random.randint(1,6)
#A conitional statment will execute if the number generated is even.
    if Dice_roll % 2 == 0:
#This allows us to print the random number generated.
        print(Dice_roll)
#This allow the player to look at the number printed and tell if it's even or odd.
        Dice_question1 = input('Is it even or odd')
#This condition will execute if the player enters the word 'even'.
        if Dice_question1 == 'even':
#This statement will generate if the player is correct in saying if the number is even.
            print("Correct! You have won the game.")
#If the player states that the number is not even, even though it is, a statement will inform him that he has lost the game.
        else:
            print('Incorrect. GAME OVER!')
#When the dice_roll variable outputs an odd number this condition will generate.
    elif Dice_roll % 1:
#This allow sthe player to look at the number ouputed and tell if it's even or odd.
        Dice_question2 = input('is it even or odd')
#This condition will generate if the number generated is odd.
        if Dice_question2 == 'odd':
#This statement will be outputed to inform the player he won if he answerd correctly.
            print("Correct! You have won the game.")
#This conditional statemnt will generate the line of code above wasn't applied.
        else:
#A statement will be printed to let the player know he lost if he answerd incorrectly.
            print('Incorrect. GAME OVER!')
#This line of code will generate if path1 is E and Path2 is N.
elif path1 == 'E' and path2 == 'N':
#A statement to inform the player of the kind of game he's playing (A word game).
    print('Lets Play a Word Game')
#This varibale allows us to store a few words in a list as it will be used in this game.
    Original_Word = ['diaper', 'desserts', 'pan', 'gateman','raw', 'rewarder' ]
#This commond will be executed to generate a randoom word from the list above.
    Choice_word = random.choice(Original_Word)
#This outputs the random word selected.
    print(Choice_word)
#This variable allows the player to input the word generated backwards.
    respell_word = input('Spell The Word Backwards')
#This conditional statement will execute if the word respelled backwards is correct.
    if respell_word == 'repair' or respell_word == 'stressed' or respell_word == 'nap' or respell_word == 'nametag' or respell_word == 'war' or respell_word == 'redrawer':
#This statment will be printed if the word spelled is correct to inform the player that he has won.
        print("Correct! you have won the game")
#This conditional statement will execute if the above conditions aren't satisfied.
    else:
#This statement will print if all else fails.
        print("Incorrect! you've lost the game")
#This conditional will execute if path1 is W and path2 is N.
elif path1 == 'W' and path2 == 'N':
#A statement informing the player of the kind of game he will play (Guessing a prime number).
    print('Lets play a numbers game. Guess a prime number')
#This allows us to input a number.
    number_guess = int(input('Enter a number'))
#this is a conditional statement that will execute if the number is less than oor equal to 1.
    if number_guess <=1:
#This will print a statement of the condition above is satisfied
        print('Incorrect! GAME OVER!')
#If the first "if" statement doesn't execute due to it's condition, this line of code will execute.
    else:
#This sets a range for the numbers that are inputed too fall under.
        for i in range (2, number_guess ):
#If the number entered has no remaining when divided by any number in the range, it will equal to 0.
            if(number_guess % i) == 0:
#This statement will execute if the above conditions isn't satisfied.
                print('Incorrect! GAME OVER!')
#This will stop the the printing of the above statement.
                break
#If the "if" statement doesn't execute due to it's condition, this line of code will execute.
        else:
#This will print a statement to let the player know he's won the game.
            print('Correct! You have won the game')
                
    
