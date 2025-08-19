#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int countPrimesInRange(int low, int high) {
    if (high < 2) return 0;

    bool sieve[high + 1];
    for (int i = 0; i <= high; i++)
        sieve[i] = true;

    sieve[0] = sieve[1] = false;

    for (int p = 2; p * p <= high; p++) {
        if (sieve[p]) {
            for (int i = p * p; i <= high; i += p) {
                sieve[i] = false;
            }
        }
    }

    int count = 0;
    for (int i = (low < 2 ? 2 : low); i <= high; i++) {
        if (sieve[i]) {
            count++;
        }
    }

    return count;
}

int main() {
    int low, high;
    scanf("%d %d", &low, &high);

    printf("%d\n", countPrimesInRange(low, high));

    return 0;
}
