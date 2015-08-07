#!/usr/bin/env python
# HW03_ex06
# (1) Please comment your code.
# (2) Please be thoughtful when naming your variables.
# (3) Please remove development code before submitting.
################################################################################
# Exercise 1
# When you submit only include your final function: compare
def compare(x,y):
    if x>y:
        print 1
    elif x==y:
        print 0
    else:
        print -1




################################################################################
# Exercise 2
# When you submit only include your final function: hypotenuse
# Do develop incrementally. Do not share here.
def hypotenuse(x,y):
    import math
    dsquared=x**2 + y**2
    result = math.sqrt(dsquared)
    print result



################################################################################
# Exercise 3
# When you submit only include your final function: is_between
def is_between(x,y,z):
    if (x<=y and y<=z):
        print True
    else:
        print False





################################################################################
# Exercise 6
# When you submit only include your final function: is_palindrome
def is_palindrome(s):
    def inverse(s):
        return s[::-1]
    if (s==inverse(s)):
        print('Pal')
    else:
        print('No')
    




################################################################################
# Exercise 7
# When you submit only include your final function: is_power
def is_power(a,b):
    if(float(float(a)/float(b))%1==0 and float(float(a)/float(b))%b== 0):
        print('Yes')
    else:
        print('no')
    




################################################################################
def main():
    """Your functions will be called within this function."""
    ############################################################################
    # Use this space temporarily to call functions in development:
    print("Hello World!")







    ############################################################################
    # Uncomment the below to test and before commiting:
    # # Exercise 1
    compare(1,1)
    compare(1,2)
    compare(2,1)
    # Exercise 2
    hypotenuse(1,1)
    hypotenuse(3,4)
    hypotenuse(1.2,12)
    # # Exercise 3
    is_between(1,2,3)
    is_between(2,1,3)
    is_between(3,1,2)
    is_between(1,1,2)
    # # Exercise 6
    is_palindrome("Python")
    is_palindrome("evitative")
    is_palindrome("sememes")
    is_palindrome("oooooooooooo")
    # # Exercise 7
    is_power(28,3)
    is_power(27,3)
    is_power(248832,12)
    is_power(248844,12)


if __name__ == "__main__":
    main()
