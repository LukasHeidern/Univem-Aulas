#include <stdio.h>

void main(){
    float f, c;

    printf("Digite a temperatura em graus Fahrenheit: ");
    scanf("%f",&f);

    c = ((f-32)/9)*5;
    printf("%0.2f graus Fahrenheit sao %0.2f graus Celcius",f,c);}