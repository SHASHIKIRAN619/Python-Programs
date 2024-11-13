#Write a program to find the leap year:-

print("Enter tye Year: ");
year=int(input());
if(year%400==0) and (year%100==0):
    print(year, "is a leap year")
elif(year%4==0) and (year%100!=0):
    print(year,"is a leap year");
else:
    print(year,"its not a leap year");
