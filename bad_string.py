#!/usr/bin/env python3
import ctypes as ct

''' python strings are immutable.  The function adds 1 to each value in the
    array. The python string will remain unchanged afterwards.
'''
if __name__ == '__main__':
    libc = ct.CDLL("./libmyCLib.so")

    print("Calling C function which tries to modify Python string")
    original_string = "starting string"
    print("Python Before:", original_string)
    # this call does not change value, even though it tries!
    libc.add_one_to_string(original_string)
    print("Python After :", original_string)

