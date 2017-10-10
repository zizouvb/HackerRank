import calendar
month, day ,year = map(int,input().split())
# wday = {0:'MONDAY', 1:'TUESDAY', 2:'WEDNESDAY', 3:'THURSDAY', 4:'FRIDAY', 5:'SATURDAY', 6:'SUNDAY'}
wday = calendar.day_name
print(wday[calendar.weekday(year, month, day)].upper())
