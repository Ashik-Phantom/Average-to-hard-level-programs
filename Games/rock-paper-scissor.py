
#SIMPLE ROCK PAPER SCISSORS GAME USING PYTHON RANDOM with exception handling
#code by Ashik-Phantom 

import random
import os
from time import sleep
from retrying import retry

print("\n\t\t\t██████╗░░█████╗░░█████╗░██╗░░██╗   ██████╗░░█████╗░██████╗░███████╗██████╗░")
print("\t\t\t██╔══██╗██╔══██╗██╔══██╗██║░██╔╝   ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
print("\t\t\t██████╔╝██║░░██║██║░░╚═╝█████═╝░   ██████╔╝███████║██████╔╝█████╗░░██████╔╝")
print("\t\t\t██╔══██╗██║░░██║██║░░██╗██╔═██╗░   ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗")
print("\t\t\t██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗   ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║")
print("\t\t\t╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝   ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝")

print("\t\t\t\t░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗")
print("\t\t\t\t██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝")
print("\t\t\t\t╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░")
print("\t\t\t\t░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗")
print("\t\t\t\t█████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝")
print("\t\t\t\t╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░")
print("\n\t\t\t\t\t\t\tBY ASHIK-PHANTOM")

#Getting Inputs for time reset and max score
while(True):
	try:
		reset_time=int(input("\n\t\t\t\t\t\t   Set reset time:(in sec): "))
		break
	except:
		print('\n\t\t\t\t\t\t     Please enter a number')
while(True):
	try:
		max_score=int(input("\n\t\t\t\t\t\t   Set Max score:(in units): "))
		break
	except:
		print('\n\t\t\t\t\t\t     Please enter a number')
	
sleep(1)
os.system('cls')

your_score,computer_score=0,0

while True:
	print('\n\t\t\t\t\t\tROCK | PAPER | SCISSORS\n')
	print('\t\t\t\t\t\t   Make your choice:')
	choice = str(input("\n\t\t\t\t\t\t\t "))
	choice = choice.lower()
	os.system('cls')
	choices = ['rock', 'paper', 'scissors']

	computer_choice = random.choice(choices)
	print()
	if choice in choices:
		if choice == computer_choice:
			print('\t\t\t\t\t***************it is a tie**************')
		if choice == 'rock':
			if computer_choice == 'paper':
				print('\t\t\t\t\t****************Computer wins***************')
				computer_score+=1
			elif computer_choice == 'scissors':
				print('\t\t\t\t\t*********************You win*******************')
				your_score+=1
		if choice == 'paper':
			if computer_choice == 'scissors':
				print('\t\t\t\t\t****************Computer wins***************')
				computer_score+=1
			elif computer_choice == 'rock':
				print('\t\t\t\t\t*********************You win*******************')
				your_score+=1
		if choice == 'scissors':
			if computer_choice == 'rock':
				print('\t\t\t\t\t****************Computer wins***************')
				computer_score+=1
			elif computer_choice == 'paper':
				print('\t\t\t\t\t*********************You win*******************')
				your_score+=1 
		print() 
		print("\t\t\t\t\t---------------------------------------------")
		print("\t\t\t\t\t\t\t SCORE ")
		print("\t\t\t\t\tYour choice: "+choice.upper()+" | "+computer_choice.upper()+" :Computer's choice")
		print("\t\t\t\t\t\t   YOU: "+str(your_score)+" | "+str(computer_score)+" :Computer")
		print("\t\t\t\t\t_____________________________________________") 
		sleep(reset_time)
		os.system('cls')
		if your_score==max_score:
			print("\n\n\n\n\n\n\n\n\n\t\t\t\t\t\tYou win!!!!! congrats :)\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			break
		elif computer_score==max_score:
			print("\n\n\n\n\n\n\n\n\n\t\t\t\t\t\tyou lose, sorry :(\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			break
	else:
		print("\t\t\t\t\t\tinvalid choice, try again")




