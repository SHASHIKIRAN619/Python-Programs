'''
Write a python program to print:-
* * *  *
* * *  *
* * *  *
* * *  *
* * *  *
'''
class Pattern2:
    def patt2(self):
        print("Enter no of rows: ");
        n=int(input());
        print("Enter no of columns: ");
        m=int(input());
        for i in range(n):
            for j in range(m):
                print("*",end=' ');
            print();
p2=Pattern2();
p2.patt2();
