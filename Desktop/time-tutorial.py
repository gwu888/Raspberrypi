# import datetime class from datetime module
from datetime import datetime
import calendar
import datetime as dt
import numpy as np

# get current date
now_t = datetime.now()
print('datetime.now():', datetime.now())
print('now_t: ', now_t)
print('now_t.day - Day of Month: ', now_t.day)
print('Day of Week(number): ', now_t.weekday())
print('Day of Week(name): ', calendar.day_name[now_t.weekday()])
print('Hour: ', now_t.hour)
print('Minute: ', now_t.minute)

# convert current date into timestamp:
t_stamp = datetime.timestamp(now_t)

print("Date and Time: ", now_t)
print("Timestamp: ", t_stamp)

j = 0
for i in calendar.day_name:
	print(j,'-',i)
	j+=1

iterations = 6
tstep = dt.timedelta(seconds=60)
print('TSTEP = ',tstep)
startTime = dt.datetime.now()
print('TIMESTAND = ',startTime)
for i in np.arange(iterations):
	while startTime < startTime + tstep:
		1==1
	#	print(i)


# nothing here
# $ date +"%FT%T%Z"
