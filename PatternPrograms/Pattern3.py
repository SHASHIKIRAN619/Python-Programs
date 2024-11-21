'''
Write a python program to print:-
*
**
***
****
*****
'''

class Pattern3:
    def patt3(self):
        print("Enter number of rows:");
        n=int(input());
        for i in range(n):
            for j in range(i+1):
                print("*",end='');
            print();
p3=Pattern3();
p3.patt3();
