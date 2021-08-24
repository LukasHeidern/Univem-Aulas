#include <stdio.h>

int main(){
    float salario,salario_final,p_reajuste;
    
    printf("Digite o valor do salario: ");
    scanf("%f",&salario);

    printf("Digite a porcentagem de reajuste: ");
    scanf("%f",&p_reajuste);

    salario_final = salario + (salario / 100) * p_reajuste;
    printf("O valor final do salario e %0.2f\n",salario_final);
}