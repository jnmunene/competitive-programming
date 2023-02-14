#!/usr/bin/python3

def is_palindrome(s):
    """
    :type: s str
    :rtype: bool
    """
    return s ==s[::-1]

if __name__ =='__main__':
    a = str(input("Enter string to check palindrome\n"))
    result = is_palindrome(a)
    print(result)
