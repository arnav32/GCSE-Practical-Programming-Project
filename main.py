# GCSE OCR NEA Practical Programming Project [Task 2]: "Katarina's Dice Game"
# By Arnav Prasad 10X/Cs1 (Wilson's School)

# Comment tag key:
	# [Init] ------> A variable/array is being initialised, or modules are  being imported and installed.
	# [Test] ------> A script that was used temporarily during the testing stage of the project for testing purposes, but is not a part of the final program.
	# [Procedure] -> A procedure is a type of sub program—a set of instructions stored under one name used to simplify and shorten code that do not have to take parameters and never return a value.
	# [Function] --> A function is a type of sub program—a set of instructions stored under one name used to simplify and shorten code that always take at least one parameter and always return a value.
	# [Calc] ------> Calculation or manipulation of data is taking place.

# [Init] Importing and installing modules for later use in script
from random import randint
from time import sleep
from sys import stdout
from replit import clear
from prettytable import PrettyTable

# [Init] Global variables storing user and other information to be manipulated throughout script
pScore, loggedIn, pUsername, pPassword, roundNum, tiebreakRoll = [0] * 2, [False] * 2, [""] * 2, [""] * 2, int(0), [int(0)] * 2
rulesMessageHeader = "- - - - - Rules - - - - -\n\n"
rulesMessage = ["Rule 1 - Each player rolls two dice every round; the points rolled on your dice are added to your score.\n", 
								"Rule 2 - If the total of the dice is even, you also gain 10 points.\n", 
								"Rule 3 - If the total of the dice is odd, you also lose 5 points.\n", 
								"Rule 4 - If you roll a double, you roll a bonus die; the points on this die are added to your score.\n", 
								"Rule 5 - There are five rounds in the game, and there may be a tiebreeaker round."]

# [Init] "Dice Game" ASCII art as string
diceGameASCIItext = "   ___   _             _____                \n  / _ \ (_)____ ___   / ___/___ _ __ _  ___ \n / // // // __// -_) / (_ // _ `//  ` \/ -_)\n/____//_/ \__/ \__/  \___/ \___//_/_/_/\__/ \n"

# [Test] Global variable initialised values
'''
print(str(pScore))
print(str(loggedIn))
print(str(pUsername))
print(str(pPassword))
'''

# [Init] Dice graphics as string array
dieFaces = ["---------\n|       |\n|   o   |\n|       |\n---------",
            "---------\n| o     |\n|       |\n|     o |\n---------",
            "---------\n| o     |\n|   o   |\n|     o |\n---------",
            "---------\n| o   o |\n|       |\n| o   o |\n---------",
            "---------\n| o   o |\n|   o   |\n| o   o |\n---------",
            "---------\n| o   o |\n| o   o |\n| o   o |\n---------"]

# [Test] ASCII Dice graphics
'''
for i in range(0, 6):
	print(dieFaces[i] + "\n")
'''

# ------------------ Modules / Sub Programs ------------------

# [Procedure] Types a message letter-by-letter into the UI at normal speed
def tPrint(msg):
	for letter in msg:
		stdout.write(letter)
		stdout.flush()
		sleep(0.032) # Suspends the execution of the current thread for the given number of seconds: 0.032s

# [Procedure] Type message letter-by-letter into UI at reduced speed
def tPrintSlow(msg):
	for letter in msg:
		stdout.write(letter)
		stdout.flush()
		sleep(0.05)

# [Function] Type input message as string letter-by-letter into UI and return input
def tInput(msg):
	tPrint(msg)
	userInput = input()
	return userInput

# [Function] Set text colour based on individual RGB component values passed as arguments
def textCol(r, g, b):
	return "\033[38;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"

# [Function] Set text colour back to default colour of Replit Console
def textColReset():
	return "\033[0m"

# [Init] Variable storing "[Yes/No]" string with appropriate red/green colours to be used within input messages throughout script
colYesNoText = str(" [{}Yes{}/{}No{}] ".format(textCol(176, 255, 179), textColReset(), textCol(255, 189, 192), textColReset()))


# ------------------ New Module ------------------

# Module 1 - [Procedure] Sets up game by giving the user an option to view the rules and executing the player join system, including a sign-up and login system
def setupGame():
	showRules()
	joinSystem()

#	 Module 1.1 [Procedure] - Asks the user if they would like to view the rules, displaying them in the UI if required
def showRules():
	viewRules = "" # [Init] Set the variable used to store user input about wanting to view rules to an empty string
	tPrintSlow(textCol(221, 176, 255) + "Welcome to Katarina's...\n") # Prints the former section of the welcome message to the user
	sleep(0.4)
	print(diceGameASCIItext + textColReset()) # Prints the latter section of the welcome message to the user in ASCII art; resets the current text colour
	sleep(1.5)
	clear() # Clears the UI
	viewRulesTemp = str(tInput(textColReset() + "Would you like to view the rules?" + colYesNoText)) # Creates a temporary variable to store the user input in response to whether they would like to view the rules
	while (not viewRules.lower().startswith("y")) and (not viewRules.lower().startswith("n")): # Looping to ensure a valid input is stored in the actual variable
		viewRules = viewRulesTemp # Sets the value of the actual variable to that of the temporary variable, which had a value assigned to it prior to the loop, to ensure that this 'while' loop is entered and not bypassed due to the condition involving the actual variable
		if viewRules.lower().startswith("y"): # Checks if the first character of the user's input—standardised to lowercase—is the character 'y', indicating an affirmatory response
			clear()
			tPrint(rulesMessageHeader) # Prints the header message of the rules to indicate that the rules will be listed individually below
			sleep(0.8)
			for i in range(5): # Loops over each element in the list containing the rules of the game
				tPrint(rulesMessage[i]) # Prints each rule in turn to the UI
				sleep(1.2)
			sleep(4)
			tInput("\n\nPress enter to continue. ") # Awaits user input to continue, allowing the rules to be read and understood fully
		elif viewRules.lower().startswith("n"): # Checks if the first character of the user's input—standardised to lowercase—is the character 'n', indicating a negative response
			tPrint("\nAlright, let's start!")
		else:
			tPrint("Please enter a valid response.") # Prints a message asking the user to enter a valid response—the first character of which is either 'y' or 'n'
			sleep(0.8)
			clear()
			viewRules = str(tInput("Would you like to view the rules?" + colYesNoText)) # Reassigns a value to the actual variable storing the user input, in response to whether they would like to view the rules, if the first character of the user's previous input is invalid: neither 'y' or 'n'
		sleep(0.8)
		clear()
	
# Module 1.2.1.1.1 [Function] - 
def enterAccCreds(pNum):
	print("- - - - - Player " + str(pNum) + " Login - - - - -")
	print(textCol(252, 243, 159))
	sleep(0.8)
	enteredUsername, enteredPassword = tInput("Enter username: "), tInput("Enter password: ")
	print(textColReset())
	return [enteredUsername, enteredPassword]
	
# Module 1.2.1.1.2 [Function] - 
def findLineNum(fileName, searchString):
	with open(fileName, "r") as file:
		fileLinesList = [i.strip() for i in file.readlines()]
		for lineNum in range(0, len(fileLinesList) + 1):
			if fileLinesList[lineNum] == searchString:
				return int(lineNum)
		return -1
		
'''	
for lineNum, line in enumerate(fileName, start = 0):
	if searchString in line:
		return lineNum
'''
'''
with open(fileName) as file:
	lines = file.readlines()  # reading the lines of the file in order
for line_number, line in enumerate(lines, 1):  # using enumerate to map each line of the file to it's line_number
	if key in line:  # searching for the keyword in file
			return line_number  # returning the line number
'''

# Module 1.2.1.1 [Function] - 
def pLogin(pNum):
	global pUsername, pPassword
	enteredCredsAccepted = False
	with open("usernames.txt", "r") as usernamesFile, open("passwords.txt", "r") as passwordsFile:
		usernamesList, passwordsList = [i.strip() for i in usernamesFile.readlines()], [i.strip() for i in passwordsFile.readlines()]
		while enteredCredsAccepted == False:
			enteredCreds = enterAccCreds(pNum)
# 		[Test]
#			print(enteredCreds)
#			print(usernamesList)
#			print(passwordsList)			
#			print(findLineNum("usernames.txt", enteredCreds[0]))
#			print(passwordsList[findLineNum("usernames.txt", enteredCreds[0])])
			if enteredCreds[0] in usernamesList:
				usernameLineNum = findLineNum("usernames.txt", enteredCreds[0])
				if (enteredCreds[1] in passwordsList) and (usernameLineNum >= 0):
					if enteredCreds[1] == passwordsList[usernameLineNum]:
						pUsername[pNum - 1], pPassword[pNum - 1] = enteredCreds[0], enteredCreds[1]
						tPrint(textCol(145, 207, 255) + "Player " + str(pNum) + " login successful." + textColReset())
						enteredCredsAccepted = True
					else:
						tPrint(textCol(255, 189, 192) + "Incorrect password." + textColReset())
				else:
					tPrint(textCol(255, 189, 192) + "Incorrect password." + textColReset())
				sleep(1.5)
				clear()
			else:
				tPrint(textCol(255, 189, 192) + "Username does not exist." + textColReset())
			sleep(0.8)
			clear()

# Module 1.2.1.2.1 [Function] - Input system for the user to create their account with a username and password
def createAccCreds(pNum):
	print("- - - - - Create Account for Player " + str(pNum) + " - - - - -" + textCol(252, 243, 159) + "\n") # Prints a header message indicating that the user can create a player account
	sleep(1.5)
	createdUsername, createdPassword, createdPasswordConf = tInput("Create a username: "), tInput("Create a password: "), tInput("Confirm password: ")
	print(textColReset())
	return [createdUsername, createdPassword, createdPasswordConf]

# Module 1.2.1.2 [Function] - Sign-up system allowing a user to create an account with a username and password that are verified to fit certain criteria for these credentials:
	# Username criteria:
		# 5 or more characters
		# Does not already exist
	# Password criteria:
		# Re-entered password matches initially entered password
def pSignUp(pNum):
	global pUsername, pPassword # Declares the global variables storing the player usernames and passwords within the function
	createdCredsAccepted = False # The value of the boolean variable storing whether the credentials entered by the user fit all the criteria and have therefore been accepted by the system
	with open("usernames.txt", "r+") as usernamesFile, open("passwords.txt", "a") as passwordsFile: # Temporarily opens the text files storing all player usernames (in read and write mode) and passwords (in append mode) individually as objects
		usernamesList = [i.strip() for i in usernamesFile.readlines()] # Creates a list storing each line in the usernames text file as an element, having removed any leading and trailing whitespaces
		while createdCredsAccepted == False: # Loops until the credentials entered by the user fit all the criteria
			createdCreds = createAccCreds(pNum) # Stores the returned values of the user's credentials in a list
			if createdCreds[1] != createdCreds[2]: # Checks if the user's re-entered password does not match the user's initially entered password
				tPrint(textCol(255, 189, 192) + "Passwords do not match." + textColReset())
			elif len(createdCreds[0]) < 5: # Checks if the user's entered username is less than 5 characters
				tPrint(textCol(255, 189, 192) + "Username must be 5 or more characters." + textColReset())
			elif createdCreds[0] in usernamesList: # Checks if the user's entered username already exists in the database text file
				tPrint(textCol(255, 189, 192) + "Username already exists." + textColReset())
			else:
				pUsername[pNum - 1], pPassword[pNum - 1] = createdCreds[0], createdCreds[1] # Sets the value of the player's username and password variables to their inputs
				usernamesFile.write("\n" + createdCreds[0]) # Appends the user's accepted username to the username database file after appending a new line
				passwordsFile.write("\n" + createdCreds[1]) # Appends the user's accepted password to the password database file after appending a new line
				tPrint(textCol(145, 207, 255) + "Account created." + textColReset()) # Sets the text colours to light blue; prints a message to the UI verifying that the player's account has been created; resets the current text colour
				createdCredsAccepted = True # Sets the boolean variable indicating whether the credentials entered by the user fit all the criteria and have therefore been accepted by the system to true, allowing the while loop to be exited
			sleep(0.8)
			clear()
		
# Module 1.2.1 [Function] - Allows a single user to join the game, taking the player number as a parameter
def pJoin(pNum):
	global pUsername, pPassword # Declares the global variables storing the player usernames and passwords within the function
	existingAccCheck = "" # [Init] User input indicating whether they have an existing account or not
	existingAccCheckTemp = str(tInput("Player " + str(pNum) + ", do you have an existing account?" + colYesNoText)) # Creates a temporary variable to store the user input in response to whether they have an existing account or not
	while not existingAccCheck.lower().startswith("y") and not existingAccCheck.lower().startswith("n"): # Looping to ensure a valid input is stored in the actual variable
		existingAccCheck = existingAccCheckTemp  # Sets the value of the actual variable to that of the temporary variable, which had a value assigned to it prior to the loop, to ensure that this 'while' loop is entered and not bypassed due to the condition involving the actual variable
		clear()
		sleep(0.4)
		if existingAccCheck.lower().startswith("y"): # Checks if the first character of the user's input—standardised to lowercase—is the character 'y', indicating an affirmatory response
			pLogin(pNum) # Initiates the player login system module
		elif existingAccCheck.lower().startswith("n"): # Checks if the first character of the user's input—standardised to lowercase—is the character 'n', indicating a negative response
			pSignUp(pNum) # Initiates the player sign-up system module
		else:
			tPrint("Please enter a valid response.") # Prints a message asking the user to enter a valid response—the first character of which is either 'y' or 'n'
			sleep(0.8)
			clear()
			existingAccCheck = existingAccCheckTemp = str(tInput("Player " + str(pNum) + ", do you have an existing account?" + colYesNoText)) # Reassigns a value to the actual variable storing the user input, in response to whether they have an exising account or not, if the first character of the user's previous input is invalid: neither 'y' or 'n'

# Module 1.2 [Procedure] - Allows two users to join the game as players, through either a login or sign-up system based on whether they have an existing account
def joinSystem():
	pJoin(1)
	pJoin(2)

# ------------------ New Module ------------------

# Module 2.1.1.2.1
def updateRollingInterface(pNum, i):
	sleep(i/100)
	clear()
	print(textCol(245, 240, 152) + "Round " + str(roundNum) + textColReset() + "\n\n- - - - - Player " + str(pNum) + " ({}) Roll - - - - -\n".format(pUsername[pNum - 1]))
	print("Rolling...\n")
	die1Num = rollDie()
	die2Num = rollDie()
	updateDiceGraphics(die1Num, die2Num)

# Module 2.1.1.2.2
def rollDie():
	return randint(1,6)

# Module 2.1.1.2.3.1
def updateSingleDieGraphics(dieNum):
	print(dieFaces[dieNum - 1])
	print("    " + str(dieNum))
	
# Module 2.1.1.2.3
def updateDiceGraphics(die1Num, die2Num):
	updateSingleDieGraphics(die1Num)
	print("\n")
	updateSingleDieGraphics(die2Num)
	
# Module 2.1.1.1
def scoreCalc(rolls):
	global pScore
	if rolls[0] == rolls[1]:
		return ["double", rolls[0]]
	elif (rolls[0] + rolls[1]) % 2 == 0:
		return [rolls[0] + rolls[1] + 10]
	elif (rolls[0] + rolls[1]) % 2 == 1:
		return [rolls[0] + rolls[1] - 5]
	else:
		return [rolls[0] + rolls[1]]
# [Test] Score calculator
# print(str(scoreCalc(pTurn())))

# Module 2.1.1.2
def pTurn(pNum):
	clear()
	print(textCol(245, 240, 152) + "Round " + str(roundNum) + textColReset() + "\n\n- - - - - Player " + str(pNum) + " ({}) Roll - - - - -\n".format(pUsername[pNum - 1]))
	sleep(1)
	tInput("Press enter to roll. ")
	for i in range(1, 25):
		updateRollingInterface(pNum, i)
	sleep(0.8)
	clear()
	print(textCol(245, 240, 152) + "Round " + str(roundNum) + textColReset() + "\n\n- - - - - Player " + str(pNum) + " ({}) Roll - - - - -\n".format(pUsername[pNum - 1]))
	die1Num = rollDie()
	die2Num = rollDie()
	updateDiceGraphics(die1Num, die2Num)
	tPrint("\n\n")
	sleep(1.2)
	rollTotal = die1Num + die2Num
	tPrintSlow("Total: " + str(rollTotal) + "\n\n")
	sleep(1.2)
	if die1Num == die2Num:
		tPrint("You rolled a double. (Bonus roll!)")
	elif rollTotal % 2 == 0:
		tPrint("Your total is even. [+10 points]")
	elif rollTotal % 2 == 1:
		tPrint("Your total is odd. [-5 points]")
	sleep(1.2)
	return [die1Num, die2Num]

# Module 2.1.1.3
def pExtraTurn(pNum):
	clear()
	print(textCol(245, 240, 152) + "Round " + str(roundNum) + textColReset() + "\n\n- - - - - Player " + str(pNum) + " ({}) Bonus Roll - - - - -\n".format(pUsername[pNum - 1]))
	sleep(1)
	tInput("Press enter to roll. ")
	for i in range(1, 25):
		sleep(i/100)
		clear()
		print(textCol(245, 240, 152) + "Round " + str(roundNum) + textColReset() + "\n\n- - - - - Player " + str(pNum) + " ({}) Bonus Roll - - - - -\n".format(pUsername[pNum - 1]))
		dieNum = rollDie()
		updateSingleDieGraphics(dieNum)
	sleep(1)
	tPrintSlow("\n\nAdded score: " + str(dieNum))
	return dieNum

# Module 2.1.1
def updatePlayerScore(pNum):
	global pScore
	rollScore = scoreCalc(pTurn(pNum))
	if rollScore[0] != "double":
		pScore[pNum - 1] += rollScore[0]
	else:
		# The function 'scoreCalc()' is not required since the number rolled on the third dice is added directly to the score.
		pScore[pNum - 1] += (rollScore[1] * 2) + pExtraTurn(pNum)
	if pScore[pNum - 1] < 0:
		pScore[pNum - 1] = 0
	print("\n\n")
	print("        Scores:")
	sleep(0.4)
	pScoresDisplay = PrettyTable(["Player 1", "Player 2"])
	pScoresDisplay.add_row([str(pScore[0]), str(pScore[1])])
	print(pScoresDisplay)
	sleep(1.2)
	tInput("\nPress enter to continue. ")
'''
	print("\n\nPlayer 1 Score: " + str(pScore[0]))
	print("\nPlayer 2 Score: " + str(pScore[1]))
'''

# Module 2.1
def updateScores():
	updatePlayerScore(1)
	updatePlayerScore(2)

# Module 2
def playGame():
	global pUsername, roundNum
	roundNum = 0
	for i in range(5):
		roundNum += 1
		updateScores()

# ------------------ New Module ------------------

# Module 3.2.1
def compareScores():
	if pScore[0] > pScore[1]:
		return 1
	elif pScore[0] < pScore[1]:
		return 2
	elif pScore[0] == pScore[1]:
		return 0

# Module 3.2.2.1
def updateTiebreakerDieGraphics(dieNum):
	print(dieFaces[dieNum - 1])
	print("    " + str(dieNum))

# Module 3.2.2.1
def tiebreakTurn(pNum, tiebreakRoundNum):
	clear()
	print(textCol(245, 240, 152) + "Tiebreak Round " + str(tiebreakRoundNum) + textColReset() + "\n\n- - - - - Player " + str(pNum) + " ({}) Roll - - - - -\n".format(pUsername[pNum - 1]))
	sleep(1)
	tInput("Press enter to roll. ")
	for i in range(1, 25):
		sleep(i/100)		
		clear()
		print(textCol(245, 240, 152) + "Tiebreak Round " + str(tiebreakRoundNum) + textColReset() + "\n\n- - - - - Player " + str(pNum) + " ({}) Roll - - - - -\n".format(pUsername[pNum - 1]))
		dieNum = rollDie()
		updateTiebreakerDieGraphics(dieNum)
	tiebreakRoll[pNum - 1] = dieNum
	

	
# Module 3.2.2
def playTiebreaker():
	global tiebreakRoll
	tiebreakRoundNum = 1
	pNum = 2
	for i in range(2):
		pNum = 2 - ((pNum + 1) % 2)
		tiebreakTurn(pNum, tiebreakRoundNum)
		sleep(1)
	while tiebreakRoll[0] == tiebreakRoll[1]:
		for i in range(2):
			pNum = 2 - ((pNum + 1) % 2)
			tiebreakTurn(pNum, tiebreakRoundNum)
			sleep(1)
	if tiebreakRoll[0] > tiebreakRoll[1]:
		return 1
	elif tiebreakRoll[1] > tiebreakRoll[0]:
		return 2
		
#	if tiebreakRoll[0] > tiebreakRoll[1]:
#		return 1
#	else:
#		return 2

 
# Module 3.1
def storeWinningResults(winningResults):
	with open("leaderboard.txt", "a") as leaderboardFile:
		leaderboardFile.write("\n" + winningResults[0] + "\n" + str(winningResults[1]))

# Module 3.2
def calcWinner():
	global pScore
	pWinner = compareScores()
	if pWinner == 0:
		pWinner = playTiebreaker()
	return [pUsername[pWinner - 1], pScore[pWinner - 1]]

# Module 3.32
def sortLeaderboard():
	with open("leaderboard.txt", "r") as leaderboardFile:
		lineNumParity = 1
		for line in leaderboardFile:
			lineNumParity = 2 - ((lineNumParity + 1) % 2)
	
# Module 3.4
def displayLeaderboard():
	with open("leaderboard.txt", "r") as leaderboardFile:
		leaderboardListAll = [i.strip() for i in leaderboardFile.readlines()]
		
		# [Test] Values of the list leaderboardListAll
		print(str(leaderboardListAll) + "\n")
		
		leaderboardGroupedList = []
		for i in range(0, len(leaderboardListAll) - 1, 2):
			leaderboardGroupedList.append([leaderboardListAll[i], int(leaderboardListAll[i + 1])])
			print(str(leaderboardGroupedList) + "\n")
		sortedLeaderboardGroupedList = sorted(leaderboardGroupedList, key = lambda i: i[1], reverse = True)
		print(str(sortedLeaderboardGroupedList))
		
		#leaderboardListUsernames = leaderboardListAll[::2]
		#leaderboardListScores = leaderboardListAll[1::2]

		leaderboardDisplay = PrettyTable(["Username", "Score"])
		if len(sortedLeaderboardGroupedList) < 5:
			leaderboardLen = len(sortedLeaderboardGroupedList)
		else:
			leaderboardLen = 5
		for i in range(leaderboardLen):
			leaderboardDisplay.add_row([str(sortedLeaderboardGroupedList[i][0]), str(sortedLeaderboardGroupedList[i][1])])
		print(leaderboardDisplay)

# Module 3
def postGame():
	storeWinningResults(calcWinner())
	sortLeaderboard()
	displayLeaderboard()
	
# ------------------ Program Start ------------------
setupGame()
playGame()
postGame()





























# Pseudocode
'''
# Module 2
def playGame():
#   Module 2.1
  def playRound():
#     Module 2.1.1
    def dieRoll():
#     Module 2.1.2
    def playerRolls():
#       Module 2.1.2.1
      def p1Roll():
#       Module 2.1.2.2
      def p1Roll():
#     Module 2.1.3
    def updateScores():
#       Module 2.1.3.1
      if total roll is even:
        asdf
      elif total roll is odd:
        asdf
      elif rolls are equal:
        asdf
      else:
        print("Error: Roll does not satisfy any predefined conditions in ruleset")
#     Module 2.1.4
    def keepScorePos():
#       Module 2.1.4.1
#       Module 2.1.4.2


def postGame():
#   Module 3.1
  def calcWinner():
#     Module 3.1.1
    def playTiebreaker():
#       Module 3.1.1.1
    def compareScores():
    # If the difference between the players' scores is zero
    if compareScores() == 0:
      playTiebreaker()
#   Module 3.2
  def storeWinningResults():
#     Module 3.2.1
    
#   Module 3.3
  def displayLeaderboard():
#     Module 3.3.1
    def readLeaderboardFile():
'''


'''
Thank you for taking an interest in my code :) - Arnav

                                     ▄╖ ▄                             
                                     ████
                               ▀█████████
                              ██████████▌
                    ▄▄██▄▄      ▀███████▌
                   ▐██▌▀███▄   ▄████████     ▄█▄
                   █▄▄╟▓▄▄███▄████████      ███▌
                   ▓██▓╬██▀██████████▌    ▄█████     ╓ 
               ╔▒N ╙▀████████████████▌   ██████▌    ▓█▄
             ,▓▒▒▒▌    ╙▀▀▀▀█████████   ▐██████▌   ▐████w   ,▄▄
       ▀██████▓▓█▒▌          ▐████████  ██████▀    ╘█████▄▄██
        └██████████▄           ████████ ▐█████▌  ▄███████████
          ╬████████╝         ,▄▄▓█▀████▌▄█████     ╙████████
          └██████▌          ▓▓████  █████████▌       ██████  ,▄▄▄▄
  ╓8▓▓▓█@⌐  █████          ▓▓▓███▌  █████████▀       ████▀▄▄████████
 ▓██▓▓▓▓█▒▒██▀▄█▒         ▄▓███████▌▐███▓▓▀██▓█▌   ▄███▀▄████████████▌
 ▌█╬▓▓▓██▒▓█╬▒█▓▄▒▒████▓▄▄╥▄▄▄▓██████████▓▓▓▓▓███████████████▓▓▓,,▐▀▓
 ▀█▓▌▄▄██▌▀▀▓▓▓██████▓▓▓▓▓▓▌▓█████████████▓█████████████▀▀   ▓▓▓▓▓█▓ 
   ██████▄▄,     ╙▓██████▓███▓█████▓▓█████▓████▓▓▓▓▓▄╦    ╔█▓▓███▓▓▓
   ▀█████████▄▄▄█████▀▓▓███████████▓▓██▓████████▌▀▓▓██╬▓B▓▓▓▓▓▀▀▓▓▓▀
    ╙▀█ `╙▓███████▀    ▐██████▓▐██████▓██▓▓▓▓█▌▓    ▀▓▓█▓██▓@╥  ╩╜
        ▄██████▀  .....▐█████▓▓▓▓█████▀█▄▓▄▓▓█▓▓.....  ▀▓█▓▓██▓▄ 
      .██████▀  @ █████████▒▓▓▓▓▓████████████████████∩█▄ ╙▓▓▓▓▓▓▓.
      █████▀  Æ██▓█▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓████▐███▄ ▄██▓▓██    
     ▐████▓▓▓▓▓▓▓▓█▓▓████████████████████████████▌█▓█████████▓▓▓██    
     ▐███▌▐▓▓▓▓▓▓▓▓██████████████████████████████▌███████████▄▓███    
      ████▓▓▓▓▓▓▓▀█╬▓████▓▓▓▓██▄███▓▓██▄██▓████▓█▌███Ü▀▀█████████     
       ████▓▓▓▄,  ▓╬███████████████▒▄████████████▌█▓█⌐╓▄███████▀      
        ╙▀█▓▓▓▓▓▓▄▓╬▓█▓▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▓█▓█████████▀▄▌      
        ╟█▄╙▀▓▓▓▓▓█▌▓▓███████████████████████████▌▓▓█████▀▀ ▐██▌      
        ▓▓▓▌  ╙▀▓▓█▌▓▓███████▓██████▓▓█▓█████████▓▓▓███▀    ███▌      
        █▓▓▓██╖  ▓▓▌▓▓▓███████▓▀███▓▓▓▓██████████▌▓▓█▓  ▓███████      
        ██▓▓▀▀▀Γ ▄██▓▓▓█████▓▓▓▓▓▓▓▓▓▓███████████▓▓▓█▓▓▓╥╓╥╦███▌      
        ╙███████████▓▓▓██████████▓▓▓▓███▓▓██████▓▓▓█▀▓█▓▒█▒▒▓█▀       
          ▀██████▀` █▓▓▓██████████▓▓▓▓██▌▓██████▓▓▓▌  ╙╩ÑÑ▀▀╙         
                    ╙█▓▓▓█████████▓▓▓▓▓████████▓▓▓█                   
                     ╙█▓▓▓█████████▓█▓▓███████▓▓▓▀                    
                       █▓▓▓▓██████▌███▓█████▓▓▓▓▀                     
                        ▀█▓▓▓▓████▓███▓███▓▓▓▓▓
                          ▀█▓▓▓▓████████▓▓▓▓▓╜
                            ▀█▓▓▓▓▓██▓▓▓▓█▀
                               ▀▓█▓▓▓▓█▀▀
                                  ▀▀▀ 
'''