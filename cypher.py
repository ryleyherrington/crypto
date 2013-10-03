#!/usr/bin/env python 
# Just run the program, give it a key, give it your message,
# give the key to your friend, let him run the program, 
# give it the key, give it the encoded text and you're done.

import string 

def encrypt(): 
	while True: 
		try: 
			key = input("Please enter the encryption key (a whole number): ") 
			break 
		except: 
			print "Enter a ******* number." 

	raw_message = raw_input("Input the message that you want to encrypt (DO NOT ENTER NUMBERS!!!): ") 
	message = string.lower(raw_message) 

	code = "" 

	for letter in message: 
		if letter in string.lowercase:									# if it's a character... 
			index = string.find(string.lowercase, letter)				# find its index in the list of characters 
			number = str(index + (key ** 2) - (key * 2) + (key + 1))	# do some mathematical operations on it to make encrypted message harder to crack 
			code += "%s " % number										# concatenate the letter into the final message 
		else: 
			if letter == " ":											# putting two spaces between words 
					code += " " 
			else: 
				code += "%s " % letter									# if it's not a character (ie. .,!?, etc...), concatenate it directly 

	print code[:-1]														# print the message, deleting the final space in the process 

# decryption function 
def decrypt(): 
	# initializing the message variable (the final plaintext output) 
	message = "" 

	# making sure the key is numeric, if not, asking the user for the key again 
	while True: 
		try: 
			key = input("Please enter the secret key: ") 
			break 
		except: 
			print "Enter a ******* number, idiot!" 

	# asking for the encrypted text 
	code = raw_input("Enter the encrypted text: ") 

	# splitting it into chunks 
	numberslist = code.split(" ") 

	for number in numberslist:								# going element by element in the list... 
		if number == "": 
			message += " "									# replacing two spaces with one space 
		else: 
			try:											# checking if the element is numeric 
				index = (int(number) - (key**2) + key - 1)	# elemenating all prior mathematical operations... 
				try: 
					letter = string.lowercase[index]		# checking if the key is within range for the encrypted text 
					message += letter						# concatenating the letter (or punctuation mark) to the final message in the process 
				except: 
					print "You have got the wrong key." 
					break 
			except ValueError: 
				letter = number 
				message += letter 
			 
	print string.capitalize(message)						# capitalizing the first letter. Might as well make it look good... 

# asking whether the user wants to encrypt or decrypt 
choice = raw_input("Would you like to encrypt your message or decrypt your code? [encrypt/decrypt]: ") 

if choice == "encrypt":		# running the correct function accordingly 
	encrypt() 
elif choice == "decrypt": 
	decrypt() 
else: 
	print 'Please enter either "encrypt" or "decrypt" only!' # if the user entered something else 

# thank you for viewing the source code of my program! INFRINGE MY COPYRIGHT AND I WILL RAPE YOU! 


