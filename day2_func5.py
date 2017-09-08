#!/usr/bin/env python


def check_len(str):
    str_len = len(str)
    if (str_len > 2):
        print (str[0:2])
    else:
        print ("Too short")

def main():
    a = ['a','b','c','d']
    check_len(a)

    #print ("string")

if __name__ == "__main__":
    main()
