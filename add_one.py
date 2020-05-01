#!/usr/bin/env python3
import ctypes as ct

if __name__ == '__main__':
    libc = ct.CDLL("./libmyCLib.so")

    x = 19
    # uint8_t add_one(uint8_t value);
    print(f"sent:{x}, returned:{libc.add_one(x)}")
    input("Press Return for next result")
    print()

    x = 1999
    print(f"sent:{x}, returned:{libc.add_one(x)}")
    input("Press Return for next result")
    print()

    x = 9999999999999999999
    print(f"sent:{x}, returned:{libc.add_one(x)}")
    print(f"sent:{x}, PYTHON returned:{x+1}")
    print()
