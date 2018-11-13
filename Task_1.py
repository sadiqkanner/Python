print("Enter the date or day of your birth")
day = int(input())
while day > 31 or day < 1:
    print("try again the day of your birth")
    day = int(input())
if day > 13:
    nmonth =  10-month
    td = 31+13-day

elif day <= 13:
    td = 13-day    
    nmonth =  11-month
    
print("Enter the month of your birth")
month = int(input())
while month >12 or month < 1:
    print("try again for the month of your birth")
    month = int(input())
if month > 11:
    nmonth = 12+11-month
elif month <= 11:
    nmonth = 11-month
print("Enter the year of your birth")
year = int(input())
while year >2018 or year < 0:
    print("try again the year of your birth")
    year = int(input())
else:
    if day==13 and month==11 and year==2018:
        print("Congrats You Born Today 13/11/2018")
    else:
        nyear = 2018-year
        print("Your "+str(nyear)+" years old & "+str(nmonth)+" month & "+str(td)+" day")
    

    