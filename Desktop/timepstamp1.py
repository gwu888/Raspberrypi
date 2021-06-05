##
# Python's program to calculate time difference between two datetime objects.
 
import datetime
from datetime import timedelta
 
datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
date1 = '2016-04-16 10:01:28.585'
date2 = '2016-03-10 09:56:28.067'
diff = datetime.datetime.strptime(date1, datetimeFormat)\
    - datetime.datetime.strptime(date2, datetimeFormat)
 
print("Difference:", diff)
print("Days:", diff.days)
print("Microseconds:", diff.microseconds)
print("Seconds:", diff.seconds)
