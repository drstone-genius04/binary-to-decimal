'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

def decToBin(dec_value):
    # logic to convert decimal to binary 
    # using recursion
    bin_value =''
    if dec_value > 1:
        decToBin(dec_value//2)
    print(dec_value % 2,end = '')

# main code
if __name__ == '__main__':
    # taking input as decimal 
    # and, printing its binary 
    decimal = int(input("Input a decimal number: "))
    print("Binary of the decimal ", decimal, "is: ", end ='')
    decToBin(decimal)
