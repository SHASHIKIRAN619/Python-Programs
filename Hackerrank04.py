#Task
'''
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to 2 to 5, print Not Weird
If n is even and in the inclusive range of  to 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
'''
class Demo:
    def check(self):
        print("Enter the number: ");
        n=int(input());
        if(n%2!=0):
            print("Weird");
        elif(n%2==0) and (2<= n <=5):
            print("Not Weird");
        elif(n%2==0) and (6<= n <=20):
            print("Weird");
        elif(n%2==0) and (n > 20):
            print("Not Weird");
d1=Demo();
d1.check();
