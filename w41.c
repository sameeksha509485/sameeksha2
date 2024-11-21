#include <stdio.h>

int isPrime(int n) {
    if (n <= 1) return 0;  // Numbers less than or equal to 1 are not prime.
    
    for (int i = 2; i < n; i++) {
        if (n % i == 0) return 0;  // If divisible by any number other than 1 and itself, not prime.
    }
    
    return 1;  // Number is prime.
}

int main() {
