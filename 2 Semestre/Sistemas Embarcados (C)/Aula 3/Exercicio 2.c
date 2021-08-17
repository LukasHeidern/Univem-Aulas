//Exercicio 2//
#include <stdio.h>

char nome[30];

int main(){
    printf("Ola Pessoa!");
    printf("Digite seu nome por favor: ");
        // para receber o vetor onde sera armazenado o nome
        // nao necessita de '&'
    scanf("%s",nome);
    printf("Ola %s =)",nome);}
