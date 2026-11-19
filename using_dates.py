from datetime import datetime

#string representation of a date(m/d/y)
my_birthday = "01/20/1972"

#read the string and make a datetime object
my_birthday_date_object = datetime.strptime(my_birthday,"%m/%d/%Y").date()

#print the object - 1972-01-20 00:00:00
print (my_birthday_date_object)
#use .date() to remove the time component

#create string from a datetime object
my_birthday_string = my_birthday_date_object.strftime("%B/%a/%y")

print(my_birthday_string)

# %m	Month number	11
# %d	Day of the month	18
# %y	Two-digit year	26
# %Y	Four-digit year	2026
# %b	Abbreviated month name	Nov
# %B	Full month name	November
# %a	Abbreviated weekday name	Wed
# %A	Full weekday name	Wednesday


 
 