#include <stdio.h>

int main(){
    int n = 0;
    int count = 0;

    printf("Digite um numero: ");
    scanf("%i",&n);

    while(count <= 10){
        printf("%i x %i = %i\n", n, count, n*count);
        count += 1;}
}