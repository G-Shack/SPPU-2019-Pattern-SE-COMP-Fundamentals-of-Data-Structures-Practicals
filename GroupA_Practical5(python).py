str1 = input("Enter your string: ")

list1=str1.split()

#part1
def longest_str(): 
	Max=0
	for word in list1:
		if (len(word)>Max):
			Max = len(word)
			temp = word
			print("The longest word in the string is ", temp,"It's length is ", Max)

#part2
def char_freq():
    count=0
    char = input("Enter a character: ")
    for i in range (len(str1)):
        if (str1[i] == char):count += 1
    print("The frequency of occurence of char in string is", count)

#part3
def pal():
	for word in list1:
		if (word == word[::-1]):
			print(" Is the palindrome of ", word)
		else :
			print("Not a palindrome!")

#part4
def sub_str():
	subs = input("Enter the substring to search: ")

	for i in range (len(str1)-len(subs)+1):
		if(str1[i:i+len(subs)] == subs):
			print("The first apperence of substring in string is at ", i)

#part5
def word_count():
	counts  = dict()
	for word in list1:
		if word in counts:
			counts[word] +=1
			print(word,",",counts[word])
		else:
			counts[word] = 1
			print(word,",",counts[word])
			

#Menu Driven
flag = 1

while flag == 1:
	print("*_*_*_*_*_*_*_*_*_MENU_*_*_*_*_*_*_*_*_*")
	print("Enter your choice to perform followin string functions:- ")
	print("Press 1 to print the LONGEST word and it's LENGTH.")
	print("Press 2 to find a character's OCCURENCE in a string.")
	print("Press 3 to find a PALINDROME in the string.")
	print("Press 4 to find INDEX of a SUBSTRING.")
	print("Press 5 to print ALL the WORDS and their COUNT.")
	print("Press 6 to exit the program.")
	operation = int(input("Enter your choice:- ")) 
		
	if (operation == 1):
		longest_str()
	elif operation == 2:
		char_freq()
	elif operation == 3:
		pal()
	elif operation == 4:
        	sub_str()
	elif operation == 5:
        	word_count()
	elif operation == 6:
        	flag = 0
        	print("You have terminated the program.")
	else:
		print("You have provided a wrong option.")
      
