# Makefile to build and run ctypes test

all: clean build simple add_one bad_string good_string

clean:
	rm -f *.o *.so

build:
	gcc -shared -o libmyCLib.so -Wall -Werror -fpic myCLib.c -I /usr/include/python3.7

simple:
	./simple.py

add_one:
	./add_one.py

bad_string:
	./bad_string.py

good_string:
	./good_string.py

