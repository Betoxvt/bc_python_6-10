from typing import List

from pydantic import BaseModel

# Exercícios

# Vamos revisar funções adicionando type hints e Pydantic

#     1. Calcular Média de Valores em uma Lista


class Valores(BaseModel):
    valores: List[float]


def calcular_media(valores: List[float]) -> float:
    """
    Calcula a média aritmética de uma lista de valores.
    """
    return sum(valores) / len(valores)


# if __name__ == "__main__":
#     lista = [5.0, 6.4, 7.0, 'a', 17.34, 15.3, 12.0, 9.12]

#     try:
#         valores_validados = Valores(valores=lista)
#         media = calcular_media(valores_validados.valores)
#         print(f'A média é: {media}')
#     except ValueError as e:
#         print(f'Erro na validação: {e}')

#     2. Filtrar Dados Acima de um Limite


class Valor(BaseModel):
    valor: float


def filtrar_dados(valores: List[float], limite: float) -> List[float]:
    """
    Cria uma lista com os valores acima do limite.
    """
    return [valor for valor in valores if valor > limite]


# if __name__ == "__main__":
#     lista = [5.0, 6.4, 7.0, '10.1', 17.34, 15.3, 12.0, 9.12]
#     limite = '10.0'

#     try:
#         valores_validados = Valores(valores=lista)
#         limite_validado = Valor(valor=limite)
#         filtrados = filtrar_dados(valores_validados.valores, limite_validado.valor)
#         print(f'A lista de valores filtrados é: {filtrados}')
#         print(valores_validados)
#         print(limite_validado)
#     except ValueError as e:
#         print(f'Erro na validação: {e}')


#     3. Contar Valores Únicos em uma Lista


def contar_valores_unicos(lista: List[float]) -> int:
    """
    Conta os valores únicos em uma lista
    """
    return len(set(lista))


# if __name__ == "__main__":
#     lista = [1.1, 2.2, 1.1, 2.2, 3.3, 1.2, 2.1]

#     try:
#         lista_valida = Valores(valores=lista)
#         contagem = contar_valores_unicos(lista_valida.valores)
#         print(f'Quantiade de valores únicos: {contagem}')
#     except ValueError as e:
#         print(f'Erro na validação: {e}')

#     4. Converter Celsius para Fahrenheit em uma Lista


def converter_celsius_fahrenheint(temperaturas_celsius: List[float]) -> List[float]:
    """
    Converte os valores de temperatura em graus Celsius para Fahrenheit.
    """
    return [(9 / 5) * temp + 32 for temp in temperaturas_celsius]


# if __name__ == "__main__":
#     temperaturas_celsius = [12.7, 15.3, 15.8, 16.1, 15.8]

#     try:
#         temperaturas_celsius_validadas = Valores(valores=temperaturas_celsius)
#         temperaturas_fahrenheit =
#         converter_celsius_fahrenheint(temperaturas_celsius_validadas.valores)
#         print(f'Temperaturas em Fahrenheit: {temperaturas_fahrenheit}')
#     except ValueError as e:
#         print(f'Erro de validação: {e}')

#     5. Calcular Desvio Padrão de uma Lista


def calcular_desvio_padrao(dados: List[float]) -> float:
    """
    Calcula o desvio padrão dos dados em uma lista
    """
    variancia = sum((x - calcular_media(dados)) ** 2 for x in dados) / len(dados)
    return variancia**0.5


# if __name__ == "__main__":
#     dados = [4, 3, 5, 6, 3, 5]

#     try:
#         dados_validados = Valores(valores=dados)
#         desvio_padrao = calcular_desvio_padrao(dados_validados.valores)
#         print(f'O desvio padrão desse conjunto de dados é {desvio_padrao}')
#     except ValueError as e:
#         print(f'Erro de validação: {e}')

#     6. Encontrar Valores Ausentes em uma Sequência


class Inteiros(BaseModel):
    inteiros: List[int]


def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    """
    Cria uma lista com os valores ausentes em uma sequencia.
    """
    completa = set(range(min(sequencia), max(sequencia) + 1))
    return list(completa - set(sequencia))


# if __name__ == "__main__":
#     lista = [5, 3, 8, 6, 10, 1 ]

#     try:
#         lista_validada = Inteiros(inteiros=lista)
#         ausentes = encontrar_valores_ausentes(lista_validada.inteiros)
#         print(f'Os números ausentes são: {ausentes}')
#     except ValueError as e:
#         print(f'Erro de validação: {e}')
