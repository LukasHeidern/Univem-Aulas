#include <stdio.h>

int main(){
    int a,b,r;

    printf("Digite o valor A: ");
    scanf("%i",&a);

    printf("Digite o valor B: ");
    scanf("%i",&b);

    r = (a*a) + (b*b);

    printf("O resultado de %i^2 + %i^2 e %i",a,b,r);}