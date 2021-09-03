#include <stdio.h>

int main(){
    int C_odigo,Q_uantidade;
    float P_total;

    printf("Cardapio\n");
    
    printf("Especificacao      Codigo      Preco\n");
    
    printf("Cachorro Quente    100         1,20\n");
    printf("Bauru Simples      101         1,30\n");
    printf("Bauru com Ovo      102         1,50\n");
    printf("Hamburguer         103         1,20\n");
    printf("Cheeseburger       104         1,70\n");
    printf("Suco               105         2,20\n");
    printf("Refrigerante       106         1,00\n");

    while(C_odigo != 0){
        
        printf("\nDigite o codigo do item que deseja comprar ou digite 0 para encerrar: ");
        scanf("%i",&C_odigo);

        printf("Digite a quantidaede: ");
        scanf("%i",&Q_uantidade);
        
        printf("Voce adicionou:");
        printf("Especificacao      Codigo      Preco\n");
        
        if (C_odigo == 100){
            P_total += Q_uantidade * 1.20; 
            printf("Cachorro Quente    100         1,20 x %i\nTotal - %f",Q_uantidade, 1.20 * Q_uantidade);}

        else if (C_odigo == 101){
            P_total += Q_uantidade * 1.30;
            printf("Bauru Simples      101         1,30 x %i\nTotal - %f",Q_uantidade, 1.30 * Q_uantidade);}

        else if (C_odigo == 102){
            P_total += Q_uantidade * 1.50;
            printf("Bauru com Ovo      102         1,50 x %i\nTotal - %f",Q_uantidade, 1.50 * Q_uantidade);}

        else if (C_odigo == 103){
            P_total += Q_uantidade * 1.20;
            printf("Hamburguer         103         1,20 x %i\nTotal - %f",Q_uantidade, 1.20 * Q_uantidade);}

        else if (C_odigo == 104){
            P_total += Q_uantidade * 1.70;
            printf("Cheeseburger       104         1,70 x %i\nTotal - %f",Q_uantidade, 1.70 * Q_uantidade);}

        else if (C_odigo == 105){
            P_total += Q_uantidade * 1.20;
            printf("Suco               105         2,20 x %i\nTotal - %f",Q_uantidade, 2.20 * Q_uantidade);}

        else if (C_odigo == 106){
            P_total += Q_uantidade * 1.00;
            printf("Refrigerante       106         1,00 x %i\nTotal - %f",Q_uantidade, 1.00 * Q_uantidade);}
        
        else {printf("Codigo Invalido");}
    
    printf("O valor total da compra e %f",P_total);
}