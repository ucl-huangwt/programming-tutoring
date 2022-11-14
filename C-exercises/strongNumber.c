#include <stdio.h>
#include <stdlib.h>

// A strong number is defined as an integer where the sum of the factorials of the digits forming 
// the number is equal to the original number. For example: 1! + 4! + 5! = 1 + 24 + 120 = 145. 
//  Write a program to find all the strong numbers within a specified range.

long factorial(int num) {
    if (num == 1 || num == 0) {
        return 1;
    }
    return num * factorial(num - 1);
}

int* factorialfrom0to9() {
    int digitsSize = 10; // from 0 to 9
    int *digitsFactorial = malloc(sizeof(int) * digitsSize);
    int i = 0;
    for (i = 0; i < digitsSize; i++) {
        *(digitsFactorial + i) = factorial(i);
    }
    return digitsFactorial;
}

int main(void) {
    int upperBound = 0;
    scanf("%d", &upperBound);

    int *digitsFactorial = factorialfrom0to9();

    long sum = 0;
    int num = 0;
    int i = 0;
    for (i = 1; i <= upperBound; i++) {
        sum = 0;
        num = i;
        while (num > 0) {
            int digit = num % 10;
            sum += digitsFactorial[digit];
            num /= 10;
        }
        if (i == sum) {
            printf("%d\n", i);
        }
    }

    free(digitsFactorial);
}