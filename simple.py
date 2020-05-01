#!/usr/bin/env python3
import ctypes as ct

if __name__ == '__main__':

    libc = ct.CDLL("./libmyCLib.so")

    print(libc.simple_function());
    print(libc.simple_function());
    print(libc.simple_function());
    print(libc.simple_function());
    print()


