#time and date modules in py
import time  # This is required to include time module.
import datetime 
import calendar #name error if not import
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)
localtime = time.asctime(time.localtime(time.time())) #module object is not callable
localtime1 = time.localtime(time.time())
print("local time is ",localtime)
print("local weird time is ",localtime1)
      
def Datetime():
    print("datetime module")
    x = datetime.datetime.now() #module datetime has no attribute
    print("current date & time : ",x)
    print("H-Hour 00-23 : ",x.strftime("%H"))
    print("I-Hour 00-12 : ",x.strftime("%I"))
    print("M - minutes : ",x.strftime("%M"))
    print("p - second : ",x.strftime("%S"))
    print("p- am/pm : ",x.strftime("%p"))
def strftime():
    year = int(input("enter a year : "))
    month = int(input("enter a month : "))
    day = int(input("enter a day : "))
    print("calendar ")
    cal = calendar.month(year,month)
    print("calennder of a mont is :  \n")
    print("calendar of a year is : ",year)
    print (calendar.calendar(year,5,3,6)) #to print whole year calendar
    print(cal)
    x = datetime.datetime(year, month, day)
    print("B-month name-full version : ",x.strftime("%B"))
    print("a-weekday- short version : ",x.strftime("%a"))
    print("A-weekday- full version : ",x.strftime("%A"))
    print("w-week day as a  number : ",x.strftime("%w"))
    print("d-day of month : ",x.strftime("%d"))
    print("b-month name short version : ",x.strftime("%b"))
    print("m-month as number : ",x.strftime("%m"))
    print("y-year short version without century : ",x.strftime("%y"))
    print("Y-year full version : ",x.strftime("%Y"))
    print("this is leap year? : ",calendar.isleap(year))    #4==0 
Datetime()
strftime()

