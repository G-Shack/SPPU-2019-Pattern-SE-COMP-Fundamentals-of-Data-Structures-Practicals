"""Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N
students in the class. Write functions to compute following: a) The average score of class b)
Highest score and lowest score of class c) Count of students who were absent for the test d) Display
mark with highest frequency."""

a= []
avg = 0
sum = 0
absent = 0
maxmrksfreq = 0
n = int(input("Enter total number of students in class:- "))
print("Enter -1 for absent student")

for i in range (0,n):
	mrks = int(input("Enter Marks obtained: "))
	a.append(mrks)
for x in a:
	if (x !=-1):
		sum = sum + x
		
	else:
		absent += 1
avg = sum/(n-absent)
print("Average marks obtained by ther class are ")
print(avg)


print("Total number of absent students are ")
print(absent)


high = a[0]
for x in a:
	if (x > high):
		high = x
print("Highest marks: ")
print(high)

for x in a:
	if(x != -1):
		low = x
for x in a:
	if( x < low and x != -1):
		low = x
		
	
print("Highest marks obtained in the class are:- ")
print(high)
print("Lowest marks obtained in the class are:- ")
print(low)

for x in a:
	if (x == high):
		maxmrksfreq =+ 1
print("Maxmarks are scored by" )
print(maxmrksfreq)
