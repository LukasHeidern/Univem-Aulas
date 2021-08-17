#include <stdio.h>

//Exercicio 4 // 
//Solucao 1

void main(){
    char nome[30];
    int idade;

    printf("Digite o seu nome: ");
    fgets(nome,sizeof(nome),stdin);
        // a funcao [fgets(vetor_de _char, tamanho_da_string, entrada_de_dados)] 
        // implementa uma condicao de parada para o caso de
        // o tamanho da string exceder o tamanho do vetor, assim nao
        // ocorrera um erro de buffer overflow
    
    printf("Digite sua idade: ");
    scanf("%i",&idade);
    
    printf("\n\a%s tem %i anos\n",nome ,idade);}

/* Solucao 2

void main(){
    char nome[30];
    int idade;

    printf("Digite o seu nome: ");
    gets(nome);
        // a funcao gets() funciona de forma semelhante a
        // fgets() porem como nao ha condicao de parada
        // se o tamanho da string exceder o tamanho do vetor
        // ocorrera um erro de buffer overflow
    
    printf("Digite sua idade: ");
    scanf("%i",&idade);
    
    printf("\n\a%s tem %i anos\n",nome ,idade);}
*/