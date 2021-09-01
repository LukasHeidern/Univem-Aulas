#include <stdio.h>
int main(){

	float nota1, nota2, media;
	int totalaulas, totalfaltas;
	
	printf("Digite a sua nota de trabalho:");
	scanf("%f", &nota1);
	
    printf("\nDigite a sua nota de prova:");
	scanf("%f", &nota2);
	
    media = (nota1+nota2)/2;

	printf("\nNota1=%.2f - Nota2=%.2f - Media=%.2f",nota1,nota2,media);
	
	printf("\nDigite o total de aulas da disciplina:");
	scanf("%i", &totalaulas);
	
    printf("\nDigite o total de faltas:");
	scanf("%i", &totalfaltas);


	if((media>=7) && ((((totalaulas-totalfaltas)*100)/totalaulas)>=75)) 
        printf("\nAprovado!\n");	              
	
    else printf("\nReprovado!\n"); 
	
    return 0;
}