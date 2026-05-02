-- ==========================================================
    Variables + Data Types + Type Casting
-- ==========================================================
-- Task 1: User Info Formatter
Take name, age, and city as input and print:
"My name is X, I am Y years old, and I live in Z."
-- ================================================================================================================
name = str(input('Enter your name: '));
age = int(input('Enter your age: '));
city = str(input('Enter your city: '))'
print(f"My name is {name}, I am {age} years old, and I live in {city}");
-- ===============================================================================================================
-- Task 2: Take input from user and print its data type using type()
-- ==============================================================================================================
   value = input('Enter a vakue');
   print(type(value));
-- ==============================================================================================================
-- Task 3: Take two numbers and:
           Print sum
           Difference
           Product
           Division
-- ===============================================================================================================
    num1 = 4
    num2 = 2
    print(num1 + num2);
    print(num1 - num2);
    print(num1 * num2);
    print(num1 / num2);
-- ===============================================================================================================
-- Task 4: Swap two numbers without using a third variable
-- ===============================================================================================================
   a = 5 
   b = 2
 a = a + b;
 b = a - b;
 a = a - b;
print("a", a);
print("b", b);

Method 2:- 
     a,b = b,a
     print('a',a);
     print('b',b);
-- =================================================================================================================
-- Task 5: Convert Celsius to Fahrenheit
   Formula:
   F = (C * 9/5) + 32
-- =================================================================================================================
   celsius = float(input('Enter temperature in celsius'))
   Fahrenheit = (celsius * 9/5) + 32;
   print("Temperature in Fahrenheit:", Fahrenheit);
-- ================================================================================================================
