from __future__ import print_function
from pip import index
import datetime

print ("==================================")
print ("=                                =")
print ("=            Calendar            =")
print ("=                                =")
print ("==================================")
print ("\n")

KeepRunning = True

while KeepRunning:
	year =int(input('Enter Year: '))
	if year < 1900 or year > 9999:
		print ("Please enter a value between 1900 - 9999.")
		#Den xreiazetai pano apo 9999, giati oi epistimones lene oti se 5000 xronia (pano kato) o ilios tha katastrafei :P
		continue
	amonth =int(input('Enter Month: '))
	if amonth < 1 or amonth > 12:
		print ("Please enter a value between 1 - 12.")
		#Otidipote allo einai ektos topou kai xronou :P
		continue

	def leapYear(year):
		# Elegxei ean einai disekto etos
		if year % 4 == 0:
			if year % 100 == 0:
				if year % 400 == 0:
					return True
				else:
					return False
			else:
				return True
		else:
			return False

	# Lista apo "tuples" gia mines kai evros imeron
	# Prostethike + 1 gia na apofefxthi i sinxisi tou megistou evrous imeras
	if amonth == 1:
		calender = [('January', range(1, 31 + 1))]
	elif amonth == 2 and leapYear(year) == True:
		calender = [('February', range(1, 29 + 1))]
	elif amonth == 2:
		calender = [('February', range(1, 28 + 1))]
	elif amonth == 3:
		calender = [('March', range(1, 31 + 1))]
	elif amonth == 4:
		calender = [('April', range(1, 30 + 1))]
	elif amonth == 5:
		calender = [('May', range(1, 31 + 1))]
	elif amonth == 6:
		calender = [('June', range(1, 30 + 1))]
	elif amonth == 7:
		calender = [('July', range(1, 31 + 1))]
	elif amonth == 8:
		calender = [('August', range(1, 31 + 1))]
	elif amonth == 9:
		calender = [('September', range(1, 30 + 1))]
	elif amonth == 10:
		calender = [('October', range(1, 31 + 1))]
	elif amonth == 11:
		calender = [('November', range(1, 30 + 1))]
	elif amonth == 12:
		calender = [('December', range(1, 31 + 1))]
	else:
		print("Please enter a valid month.")

	week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

	def make_calendar(year, start_day):

		# Prosdiorizei tin trexousa thesi ekkinisi sto imerologio
		start_pos =  week.index(start_day)

		for month, days in calender:
			print ("")
			# Ektiposi titlou mina
			print('{0} {1}'.format(month, year).center(20, ' '))
			# Ektiposi tis epikefalides imeras
			print(''.join(['{0:<3}'.format(w) for w in week]))
			# Prosthetei apostasi gia mi arxiki thesi ekkinisi
			print('{0:<3}'.format('')*start_pos, end='')

			for day in days:
				# Ektiposi imeras
				print('{0:<3}'.format(day), end='')
				start_pos += 1
				if start_pos == 7:
					# Ean start_pos == 7 (Kiriaki) ksekinaei nea grammi
					print()
					start_pos = 0 # Epanafora metriti
			print('\n')

	ans = datetime.date(year, amonth, 1)
	WEEKDAY = ans.strftime("%a")
	make_calendar(year,WEEKDAY)