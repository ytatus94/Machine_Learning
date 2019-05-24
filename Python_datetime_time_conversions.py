# https://www.saltycrane.com/blog/2008/11/python-datetime-time-conversions/

from datetime import datetime
import time
import calendar

#------------------------------------------------
# Conversion to strings
#------------------------------------------------

# datetime object to string
dt_obj = datetime(2018, 11, 10, 17, 53, 59)
date_str = dt_obj.strftime('%Y-%m-%d %H:%M:%S') # string format time
print(date_str) # 輸出 2018-11-10 17:53:59

# time tuple to string
time_tuple = (2008, 11, 12, 13, 51, 18, 2, 317, 0)
date_str = time.strftime('%Y-%m-%d %H:%M:%S', time_tuple)
print(date_str) # 輸出 2008-11-12 13:51:18

#------------------------------------------------
# Conversion to datetime objects
#------------------------------------------------

# time tuple to datetime object
time_tuple = (2008, 11, 12, 13, 51, 18, 2, 317, 0)
dt_obj = datetime(*time_tuple[0:6]) # 注意要把 tuple 解開
print(dt_obj) # 輸出 2008-11-12 13:51:18
print(repr(dt_obj)) # 輸出 datetime.datetime(2008, 11, 12, 13, 51, 18)

# date string to datetime object
date_str = '2018-11-10 17:53:59'
dt_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S') # string parse time
print(dt_obj) # 輸出 2018-11-10 17:53:59
print(repr(dt_obj)) # 輸出 datetime.datetime(2018, 11, 10, 17, 53, 59)

# timestamp to datetime object in local time
timestamp = 1226527167.595983
dt_obj = datetime.fromtimestamp(timestamp)
print(dt_obj) # 2008-11-12 13:59:27.595983
print(repr(dt_obj)) # datetime.datetime(2008, 11, 12, 13, 59, 27, 595983)

# timestamp to datetime object in UTC
timestamp = 1226527167.595983
dt_obj = datetime.utcfromtimestamp(timestamp)
print(dt_obj) # 輸出 2008-11-12 13:59:27.595983
print(repr(dt_obj)) # 輸出 datetime.datetime(2008, 11, 12, 13, 59, 27, 595983)

#------------------------------------------------
# Conversion to time tuples
#------------------------------------------------

# datetime object to time tuple
dt_obj = datetime(2018, 11, 10, 17, 53, 59)
time_tuple = dt_obj.timetuple()
print(time_tuple) # 輸出 time.struct_time(tm_year=2018, tm_mon=11, tm_mday=10, tm_hour=17, tm_min=53, tm_sec=59, tm_wday=5, tm_yday=314, tm_isdst=-1)
print(repr(time_tuple)) # 輸出 time.struct_time(tm_year=2018, tm_mon=11, tm_mday=10, tm_hour=17, tm_min=53, tm_sec=59, tm_wday=5, tm_yday=314, tm_isdst=-1)

# string to time tuple
date_str = '2018-11-10 17:53:59'
time_tuple = time.strptime(date_str, '%Y-%m-%d %H:%M:%S')
print(time_tuple) # 輸出 time.struct_time(tm_year=2018, tm_mon=11, tm_mday=10, tm_hour=17, tm_min=53, tm_sec=59, tm_wday=5, tm_yday=314, tm_isdst=-1)
print(repr(time_tuple)) # 輸出 time.struct_time(tm_year=2018, tm_mon=11, tm_mday=10, tm_hour=17, tm_min=53, tm_sec=59, tm_wday=5, tm_yday=314, tm_isdst=-1)

# timestamp to time tuple in UTC
timestamp = 1226527167.595983
time_tuple = time.gmtime(timestamp)
print(time_tuple) # 輸出 time.struct_time(tm_year=2008, tm_mon=11, tm_mday=12, tm_hour=21, tm_min=59, tm_sec=27, tm_wday=2, tm_yday=317, tm_isdst=0)
print(repr(time_tuple)) # 輸出 time.struct_time(tm_year=2008, tm_mon=11, tm_mday=12, tm_hour=21, tm_min=59, tm_sec=27, tm_wday=2, tm_yday=317, tm_isdst=0)

# timestamp to time tuple in local time
timestamp = 1226527167.595983
time_tuple = time.localtime(timestamp)
print(time_tuple) # 輸出 time.struct_time(tm_year=2008, tm_mon=11, tm_mday=12, tm_hour=13, tm_min=59, tm_sec=27, tm_wday=2, tm_yday=317, tm_isdst=0)
print(repr(time_tuple)) # 輸出 time.struct_time(tm_year=2008, tm_mon=11, tm_mday=12, tm_hour=13, tm_min=59, tm_sec=27, tm_wday=2, tm_yday=317, tm_isdst=0)

#------------------------------------------------
# Conversion to timestamps
#------------------------------------------------

# time tuple in local time to timestamp
time_tuple = (2008, 11, 12, 13, 51, 18, 2, 317, 0)
timestamp = time.mktime(time_tuple)
print(timestamp) # 輸出 1226526678.0
print(repr(timestamp)) # 輸出 1226526678.0

# time tuple in UTC time to timestamp
time_tuple_utc = (2008, 11, 12, 13, 51, 18, 2, 317, 0)
timestamp_utc = calendar.timegm(time_tuple_utc)
print(timestamp_utc) # 輸出 1226497878
print(repr(timestamp_utc)) # 輸出 1226497878

