#include <stdio.h>
int main(){
    int n;
    printf("Digite o numero: ");
    scanf("%i",&n);
    for(int x = 0; x <= 10; x++){printf("%i x %i = %i",n,x,n*x);}}