class largest:
    def largestnumber(self):
        print("Enter the first number");
        num1=int(input());
        print("Enter the second number: ");
        num2=int(input());
        print("Enter the third number: ");
        num3=int(input());
        if(num1>num2) and (num1>num3):
            print(f"{num1} is largest");
        elif(num2>num1) and (num2>num3):
            print(f"{num2} is largest");
        else:
            print(f"{num3} is largest");
l1=largest();
l1.largestnumber();
