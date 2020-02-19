import time

tim = time.time()
print(tim)

print(time.localtime(tim))

print(time.localtime())
#格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S  %a %A %b %B",time.localtime()))
#时间字符串转化为时间戳
t = "2020-02-14 15:24:14"
print(time.mktime(time.strptime(t,"%Y-%m-%d %H:%M:%S")))


import calendar

print(calendar.month(2020,2))


cal = calendar.calendar(2018,w=2,l=1,c=6)
print(cal)
