#include <stdio.h>

int main(){
    int a, b;

    printf("Digite o primeiro valor: ");
    scanf("%i",&a);

    printf("Digite o segundo valor: ");
    scanf("%i",&b);

    a = a*2;
    b = b*2;

    printf("Primeiro valor - %i\nSegundo valor - %i",a,b);}