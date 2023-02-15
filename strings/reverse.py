#!/usr/bin/python3

def reverse_string(s):
    return s[::-1]

if __name__ == '__main__':
    a = str(input("Enter string to reverse\n"))
    result = reverse_string(a)
    print(result)
