print("Enter the number: ");
num=int(input())
if num<0:
    print("Please enter positive numbers")
else:
    sum=0;
    while(num>0):
        sum +=num;
        num -= 1;
    print(sum);

print("============================================================")

print("Enter a number: ");
num=int(input());
sum=0;
if(num<0):
    print("Please enter the positive number: ");
else:
    for i in range(1,num+1):
        sum=sum+i;
print(sum);
        

