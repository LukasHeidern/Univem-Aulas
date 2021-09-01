#include <stdio.h>

int main() {

	int idade;
	
    printf("Digite a idade do nadador: ");
	scanf("%d",&idade);
	
    if(idade>=5 && idade<=7){
		printf("Nadador Infantil A");}

	if(idade>=8 && idade<=11){
		printf("Nadador Infantil B");}

	if(idade>=12 && idade<=13){
		printf("Nadador Juvenil A");}

	if(idade>=14 && idade<=17){
		printf("Nadador Juvenil B");}

	if(idade>=18){
		printf("Nadador Adulto");}
}



