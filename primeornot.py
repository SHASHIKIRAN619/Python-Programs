#Write a program to find the number is prime or not:-
class prime:
    def primeornot(self):
        print("Enter the number: ");
        num=int(input());
        if(num==1):
            print("{num} is not a prime number");
        if(num>1):
            for i in range(2,num):
                if(num%i==0):
                    print(f"{num} is not a prime number");
                    break;
                else:
                    print(f"{num}is a prime number");
p1=prime();
p1.primeornot();
                    
