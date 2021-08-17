//Exercicio 7 //
#include <stdio.h>

void main(){
    int a,b,aux;

    printf("Digite o valor de A: ");
    scanf("%i",&a);

    printf("Digite o valor de B: ");
    scanf("%i",&b);

    printf("\nA = %i\nB = %i",a,b);

    aux = a;
    a = b;
    b = aux;

    printf("\nA = %i\nB = %i",a,b);}
