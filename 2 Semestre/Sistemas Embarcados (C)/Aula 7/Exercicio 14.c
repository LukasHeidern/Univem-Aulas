#include <stdio.h>

int main(){

    int a[10], b[10], n;
    
    for (int i = 0; i <= 9; i++){
        printf("Digite o valor da celula a[%i]",i);
        scanf("%i",&a[i]);}
    
    printf("Digite o valor para soma: ");
    scanf("%i",&n);
    
    for (int i = 0; i <= 9; i++){ 
        b[i] = n + a[i];}
    printf("\nvetor A = ");
    for (int i = 0; i <= 9; i++){
        printf("%i ",a[i]);}
    
    printf("\nvetor B = "); 
    for (int i = 0; i <= 9; i++){
        printf("%i ",b[i]);}

}