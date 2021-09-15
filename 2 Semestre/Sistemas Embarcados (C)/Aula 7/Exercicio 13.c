#include <stdio.h>


int main(){
    int c = 0;

    printf("\nWhile\n");
    while(c <= 100){
        printf("%i ",c);
        c++;}
    printf("\nFor\n");
    for(int i = 0;i <= 100; i += 2){ printf("%i ",i);}
    
    c = 1;
    printf("\nDo While\n");
    do{ printf("%i ",c);
        c += 2;}
    while (c <= 100);
}
