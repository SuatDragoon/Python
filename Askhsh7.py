#Onoma programatos (gia efe :P)
print ("================================================================")
print ("=                                                              =")
print ("=   ENTOPISMOS MELLONTIKON IMERON ME VASI TIN TREXOUSA IMERA   =")
print ("=                                                              =")
print ("================================================================")
print ("")

import datetime
from itertools import takewhile
from itertools import groupby
from operator import attrgetter


YEARS = 10
START = datetime.date.today()

def years_from(date, years):
    #Epistrefei thn teleutaia imera tou etous pou einai "eti" mprosta apo tin imerominia
    return datetime.date(date.year + years, 12, 31)

MAX_DATE = years_from(START, YEARS)
today = str(datetime.date.today())
WEEKDAY = int(datetime.date.today().strftime("%w"))

def intersections(weekday, day):
    #Dimiourgei imerominies opou i dedomeni imera tis evdomadas kai i imera tou mina temnontai
    date = START
    while True:
        if date.day == day and date.isoweekday() == weekday:
            yield date
        date += datetime.timedelta(days=1)

def weekday_today_occurrences():
    return intersections(WEEKDAY, int(today[8:10]))

def weekday_today_before_max(max_date=MAX_DATE):
    def date_is_before_max(date):
        return date <= max_date
    return takewhile(date_is_before_max, weekday_today_occurrences())


def weekday_today_by_year():
    return groupby(weekday_today_before_max(), attrgetter("year"))

print ("Oi mellontikes imeres me vasi tin trexousa mera << " + datetime.date.today().strftime("%A") + " " + datetime.date.today().strftime("%d") + " >> einai: ")
print ("")
print [d.isoformat() for d in weekday_today_before_max()]