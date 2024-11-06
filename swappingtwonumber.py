#Write python program to swap two numbers using third variable:-
print("Enter the first number:");
num1=int(input());
print("Enter the second number");
num2=int(input());
num3=0;
print("Before swapping",num1,"numbers",num2);
num3=num1;
num1=num2;
num2=num3;
print("After swapping",num1,"numbers",num2);

print("=====================================================================")
#Write a python program to swap two numbers without third variable:-
print("Enter the first number:");
x=int(input());
print("Enter the second number");
y=int(input());
print("Before swapping",x,"numbers",y);
x=x+y;
y=x-y;
x=x-y;
print("After swapping",x,"numbers",y);

print("==========================================================================")
print("Enter the first number:");
a=int(input());
print("Enter the second number");
b=int(input());
print("Before swapping",a,"numbers",b);
a,b= b,a;
print("After swapping",a,"numbers",b);
