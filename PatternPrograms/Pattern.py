'''
*****
*****
*****
*****
*****
'''
class Pattern1:
    def pat1(self):
        print("Enter how many rows: ")
        n=int(input());
        print("Enter how many colimns: ");
        m=int(input());
        for i in range(n):
            for j in range(m):
                print("*",end='');
            print();
p1=Pattern1();
p1.pat1();
        
