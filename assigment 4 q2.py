Year=int(input("Enter the year"))
if Year%400==0:
    print(Year,"is a leap year")
elif Year%100==0:
    print(Year,"is not a leap year")
elif Year%4==0:
    print(Year,"is a leap year")
else:
    print(Year,"is not a leap year")