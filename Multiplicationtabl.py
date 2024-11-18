#Write a program to print a multiplication table:-
class Table:
    def multiply(self):
        print("Enter the number: ");
        num=int(input());
        for i in range(1,11):
            print(num,"x",i,"=",(num*i));
T1=Table();
T1.multiply();

print("========================OR=============================");

class Table1:
    def multiply1(self):
        print("Enter the Number: ");
        num=int(input());
        i=1;
        while(i<=10):
            print(num,"x",i,"=",(num*i));
            i +=1;
T2=Table1();
T2.multiply1();

        
