import random
print "Howdy, what's your name? "
guess_name = raw_input ('>')
print "Hello {}, I'm thinking of a number between 1 and 100.".format(guess_name)
print "Try to guess my number."
random_number = random.randint (1,100)
print random_number
while True:
    try:
		player_guess = int(raw_input("Your guess? "))
    except:
        print "You need to give a number between 1 and 100. Please try again"
        continue
    if player_guess < 0 or player_guess > 100:
        print " Your number is out of range. Give a number between 1 and 100."
        continue
        
    if player_guess == random_number:
        print "Congratulations you have guessed the number"
        break
        
    if player_guess > random_number:
        print "Your number is to high. Give a lower number"
    else:
        player_guess < random_number
        print "Your number is to low. Give a higher number"
        


    

