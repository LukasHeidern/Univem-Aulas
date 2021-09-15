#include <stdio.h>

int main(){
    int matrix[7][3];

    for(int i = 0; i < 7; i++){
        for(int j = 0; j < 3; j++){
            printf("matriz[%i][%i]: ",i,j);
            scanf("%i",&matrix[i][j]);}
        }
    for(int i = 0; i < 7; i++){
        for(int j = 0; j < 3; j++){
            printf("%i ",matrix[i][j]);}
        printf("\n");}
    
}