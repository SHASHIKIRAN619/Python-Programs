#Write a program to find the factorial of a number:-
class Factorial:
    def fact(self):
        print("Enter a number: ");
        num=int(input());
        fact=1;
        if(num<0):
            print("Enter a positive number");
        else:
            for i in range(1,num+1):
                fact=fact*i;
        print("The factorial is: ",fact);
f1=Factorial();
f1.fact();
        
    


