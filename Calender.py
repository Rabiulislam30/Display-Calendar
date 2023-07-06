#Python program to display calender of the givien month and year

#importing calender module
import calendar

yy = 2023 #year

mm = 1 #month

#To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter year: "))

#display the calender
print(calendar.month(yy, mm))
