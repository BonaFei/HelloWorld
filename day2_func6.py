#!/usr/bin/env python

def get_odd(str):
    str_len = len(str)
    #print(type(str_len))
    #print(str_len)
    i = 0
    #print (type(i))

    while (str_len != 0 and i < str_len):
        if (i < str_len):
           print (str[i])
           i += 2
        else:
           break


def main():

# For list
    a = [1,2,3,4]
    get_odd(a)

# For tuple
    b = ('a','b','c','d','e')
    get_odd(b)


if __name__ == "__main__":
    main()
