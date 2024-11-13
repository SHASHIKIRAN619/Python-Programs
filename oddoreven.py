#Write a program to find a number is even or odd:-
class Demo:
    def evnodd(self):
        print("Enter the number to find even or odd: ");
        num=int(input());
        if(num%2==0):
            print(num,"is a even number")
        else:
            print(num,"its a odd number");
c1=Demo();
c1.evnodd();

