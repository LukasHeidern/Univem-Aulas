#include <stdio.h>

void main(){
    float a,b,c,media;
    
    printf("Digite o primeiro valor: ");
    scanf("%f",&a);

    printf("Digite o segundo valor: ");
    scanf("%f",&b);

    printf("Digite o terceiro valor: ");
    scanf("%f",&c);

    media = (a + b + c) / 3;

    printf("O valor da media e %0.2f ",media);}