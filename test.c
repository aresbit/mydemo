#include <stdio.h>

int main(void) {
    int arr[] = {10, 20, 30, 40, 50}; 
    int size = *(&arr + 1) - arr;
    for(int i = 0; i < size; i++) {
        printf("%d ", *(arr + i));
    }

    return 0;
}
