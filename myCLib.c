#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include "myCLib.h"

uint8_t simple_function(void) {
    static int counter = 0;
    counter++;
    return counter;
}

uint8_t add_one(uint8_t value) {
    return value + 1;
}

void add_one_to_string(char *input) {
    printf("Input  string: %s\n", input);
    for (int ii = 0; ii < strlen(input); ii++) {
        input[ii]++;
    }
    printf("Output string: %s\n", input);
}

