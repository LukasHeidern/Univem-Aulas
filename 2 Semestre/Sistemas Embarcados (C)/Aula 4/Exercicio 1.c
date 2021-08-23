#include <stdio.h>

int main(){
    int d,h,m,s,s_final;

    printf("Dias: ");
    scanf("%i",&d);

    printf("Horas: ");
    scanf("%i",&h);

    printf("Minutos: ");
    scanf("%i",&m);

     printf("Segundos: ");
    scanf("%i",&s);

    s_final = (d * 24 * 3600) + (h * 3600) + (m * 60) + s;

}