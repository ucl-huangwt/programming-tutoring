#include<stdio.h>
#include<stdlib.h>

// Write a function with the signature int* sort(int* n, int size) that takes a 
// pointer to an array of integers, and returns a pointer to a new array containing 
// the integers in sorted order.

int* copyArray(int *array, int size) {
    int *arrayCopied = malloc(sizeof(int) * size);
    int i = 0;
    for(i = 0 ; i < size ; i++){
        *(arrayCopied + i) = *(array + i);
    }
    return arrayCopied; 
}

void swap(int* array, int j) {
    int num1 = *(array + j);
    int num2 = *(array + j + 1);
    if(num1 > num2){
        int temp = num1;
        *(array + j) = num2;
        *(array + j + 1) = temp;
    }
}

int* sort(int* array, int size) {
    int *arrayCopied = copyArray(array, size);
    int i = 0;
    for(i = 0; i < size - 1; i++){
        int j = 0;
        for(j = 0 ; j < size - i - 1 ; j++){
            swap(arrayCopied, j);
        }
    }

    return arrayCopied;
}

int main(void){
    int array[] = {3, 5, 12, 1, 9, 7, 11};
    int *arraySorted = sort(array, 7);

    int i = 0;
    for(i = 0 ; i < 7 ; i++){
        printf("%d\t", *(arraySorted + i));
    }
    printf("\n");

    free(arraySorted);

    return 0;
}