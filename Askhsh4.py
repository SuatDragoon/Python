#Onoma programatos (gia efe :P)
from time import *
print ("=================================")
print ("=                               =")
print ("=        Roman Converter        =")
print ("=                               =")
print ("=================================")
print ("\n")
print ("=================================")
print ("=         Instructions          =")
print ("=================================")
print ("=                               =")
print ("= Use numbers from 1 to 1000000 =")
print ("=  To exit the programm type 0  =")
print ("=                               =")
print ("=================================\n")
num_map=[
			(1000, 'M'),
			(900, 'CM'), 
			(500, 'D'),
			(400, 'CD'), 
			(100, 'C'), 
			(90, 'XC'),
			(50, 'L'), 
			(40, 'XL'),
			(10, 'X'),
			(9, 'IX'), 
			(5, 'V'),
			(4, 'IV'),
			(1, 'I')
		]

KeepRunning = True

while KeepRunning:		
	def num2roman(num):
		roman = ""
		while num > 0:
			for i, r in num_map:
				while num >= i:
					roman += r
					num -= i
		return roman
	#epidei den ksero ean enoousate 1000000 kofti stin eisodo xristi to prosthesa
	num = int(input("\nEnter a number: "))
	if num == 0:
		print ("User close the program.")
		break
	elif num < 0 or num > 1000000:
		print ("Please enter a number between 1 and 1000000.")
	else:		
		print ("Roman number: %s") % (num2roman(num))