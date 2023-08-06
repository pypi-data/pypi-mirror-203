#include "math.h"

int addition(int a, int b)
{
    return a + b;
}

int subtraction(int a, int b)
{
    return a - b;
}

int multiplication(int a, int b)
{
    return a * b;
}

int division(int a, int b)
{
    return a / b;
}

int exponentiation(int a, int b)
{
    int index = 0;
    int result = 1;
    for (; index < b; index++)
        result *= a;
    return result;
}