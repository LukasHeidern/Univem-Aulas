#include <stdio.h>

int main(){
    float p_combustivel, desempenho, d_cidades, litros, valor;
    
    printf("Digite a distancia entre a cidade de origem e a cidade de destino: ");
    scanf("%f",&d_cidades);

    printf("Digite o preco do combustivel: ");
    scanf("%f",&p_combustivel);

    printf("Digite o desempenho do carro por litro de combustivel (km/l): ");
    scanf("%f",&desempenho);

    litros = d_cidades / desempenho;
    valor =  litros * p_combustivel;

    printf("Voce precisara de %0.2f litros que custaram R$ %0.2f",litros,valor); }