#ex1
import datetime
x = datetime.datetime.now()
print(x.day-5)


#ex2
import datetime

today = datetime.date.today()

yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)



#ex3
import datetime

x = datetime.datetime.now()

y = x.replace(microsecond=0)

print(y)


#ex4
import datetime

date1 = datetime.datetime(2022, 3, 1, 12, 0, 0)
date2 = datetime.datetime(2022, 3, 1, 13, 30, 0)

diff = (date2 - date1).total_seconds()

print(diff)
