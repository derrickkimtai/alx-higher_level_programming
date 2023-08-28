#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0;
        for intgers in my_list:
            if count < x:
                print(intgers, end='')
                count += 1
        print()
    except:
        pass
    return count
