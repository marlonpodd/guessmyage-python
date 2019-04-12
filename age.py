myAge = 14

myGuess = int(input( "Guess my age!: "))

while myGuess != myAge:
	if myGuess > myAge:
		print("Too big.. Guess again!")
		myGuess = int(input( "Guess my age!: "))
	
	if myGuess < myAge:
		print("Too small.. Guess again!")
		myGuess = int(input( "Guess my age!: "))

	if myGuess == myAge:
		print("Correct!")
		break