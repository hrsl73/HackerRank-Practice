# python program to check if number(year) is leap year or not according to Gregorian calendar

def is_leap(year):
    leap = False
    
    leap = (year%400==0) or (year%4==0 and year%100!= 0)
    return leap

year = int(input())
print(is_leap(year))