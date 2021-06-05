from datetime import datetime
import datetime as dt
import numpy as np

# get current date
now_t = datetime.now()
print('now_t: ', now_t)

print('datetime.now():', datetime.now())

iterations = 6
tstep = dt.timedelta(seconds=6)
print('TSTEP = ',tstep)
startTime = dt.datetime.now()
print('TIMESTAND = ',startTime)
for i in np.arange(iterations):
	while startTime < startTime + tstep:
		print(i)

