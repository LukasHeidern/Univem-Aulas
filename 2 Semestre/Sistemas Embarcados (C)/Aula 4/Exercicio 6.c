#include <stdio.h>

int main(){
    int a,b;

    printf("Digite o valor A:");
    scanf("%i",&a);

    printf("Digite o valor B:");
    scanf("%i",&b);

    printf("A = %i --- B = %i\n",a,b);
    
    if(a > b){ printf("A e maior que B >>> %i > %i\n",a,b); }
    else { printf("A e menor que B >>> %i < %i\n",a,b); }
}