#!/usr/bin/python

import math

def cipher(plaintext,shift):  
  
	alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m",
			  "n","o","p","q","r","s","t","u","v","w","x","y","z"]  
  
	dic={}  
	for i in range(0,len(alphabet)):  
		dic[alphabet[i]]=alphabet[(i+int(shift))%len(alphabet)]  
  
	ciphertext=""  
	for n in plaintext.lower():  
		if n in dic:  
			n=dic[n]
		ciphertext+=n  
  
	return ciphertext 

def main():
	plaintext=raw_input("What would you like to shift?")
	shift = int(raw_input("How many places would you like to shift(negative to left)?"))
	
	print "plaintext: "+ str(plaintext)
	print "shift: "+ str(shift)
	
	ciphered = cipher(plaintext, shift)
	print "ciphered: "+str(ciphered)

if __name__=="__main__":
	main()
