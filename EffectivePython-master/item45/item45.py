from time import time, localtime, strftime, mktime, strptime


now = 1407984510
local_tuple = localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
print(strftime(time_format, local_tuple))

time_str = '2017-05-06 12:33:44'
utc_now = mktime(strptime(time_str, time_format))
print(utc_now)
print(time())