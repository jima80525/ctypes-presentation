#!/usr/bin/env python3
import ctypes as ct

''' python strings are immutable.  The function adds 1 to each value in the
    array. The python string will remain unchanged afterwards.

    The ctypes string buffer IS mutable, however.
'''
if __name__ == '__main__':
    libc = ct.CDLL("./libmyCLib.so")
    print("Calling C function with mutable buffer this time")
    original_string = "starting string"
    # need to encode the original to get bytes for string_buffer
    mutable_string = ct.create_string_buffer(str.encode(original_string))
    print("Python Before:", mutable_string.value.decode('utf-8'))
    libc.add_one_to_string(mutable_string)  # works!
    print("Python After :", mutable_string.value.decode('utf-8'))
    print()


