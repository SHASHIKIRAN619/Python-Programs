#Write a program to find the Fibonacci series:-
print("Enter the number: ");
fib1=0;
fib2=1;
num=int(input());
if(num == 0):
    print(fib1);
elif(num == 1):
    print(fib1,fib2);
else:
    print(fib1);
    print(fib2);
    for i in range(1,num+1):
        res = fib1 + fib2;
        fib1=fib2;
        fib2=res;
        print(res);
        

        
