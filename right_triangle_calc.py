from math import sqrt
	
print("Welcome to the right triangle calculator!\nThis calculator let's you identify the value of the hypotenuse or one of the legs of a right triangle by entering out the value of the two given sides.\n")

def find_leg():
	leg = int(input("Enter the length of the leg: "))
	hyp = int(input("Enter the length of the hypotenuse: "))
	
	try:
		if (leg >= hyp):
			print("The value you've entered is invalid! Please try again.")
			print("Note: A triangle with a length of the leg greater than or equal that of the hypotenuse doesn't exist!\n")
			find_leg()
	
		leg_squared = (hyp ** 2) - (leg ** 2)
		leg_final = round(sqrt(leg_squared), 5)

		if (leg <= 0 or hyp <= 0):
			print("The value you've entered is invalid! Please try again.")
			print("Note: A triangle with a length of a negative or a value of zero doesn't exist!\n")
			find_leg()
		else:
			print("The length of the other leg of the triangle is " + str(leg_final) + ".")
			final_prompt()
	except ValueError:
		print("")

def find_hyp():
	leg_one = int(input("Enter the length of the first leg: "))
	leg_two = int(input("Enter the length of the second leg: "))
	
	hyp_squared = (leg_one ** 2) + (leg_two ** 2)
	hyp_final = round(sqrt(hyp_squared), 5)
	
	if (leg_one <= 0 or leg_two <= 0):
		print("The value you've entered is invalid! Please try again.")
		print("Note: A triangle with a length of a negative or a value of zero doesn't exist!\n")
		find_hyp()
	else:
		print("The length of the hypotenuse of the triangle is " + str(hyp_final) + ".")
		final_prompt()

def choose_side():
	option = input("Which side of the right triangle do you want to find the value of?\n1 - leg\n2 - hypotenuse\n")
	if (option == "1"):
		find_leg()
	elif (option == "2"):
		find_hyp()
	else:
		print("Wrong input! Please try again.\n")
		choose_side()

def final_prompt():
	continue_prompt = input("Do you want to continue calculating? y/n: ")
	
	if (continue_prompt == "y" or continue_prompt == "Y"):
		print("")
		choose_side()
	elif (continue_prompt == "n" or continue_prompt == "N"):
		print("")
	else:
		print("Wrong input! Please try again.")
		final_prompt()

choose_side()
input("Press Enter to exit the program...")