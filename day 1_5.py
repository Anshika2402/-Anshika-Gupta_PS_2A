import datetime
import calendar
def findDay(date):
    d=datetime.datetime.strptime(date,'%d %m %Y').weekday()
    return (calendar.day_name[d])
date=str(input('Enter date [dd mm yyyy]: '))
print(findDay(date))
