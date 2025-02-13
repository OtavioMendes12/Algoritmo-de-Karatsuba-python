# Projeto Karatsuba

## Descrição do Projeto
Este projeto implementa o algoritmo de Karatsuba em Python para realizar multiplicação eficiente de números inteiros grandes. O algoritmo reduz a complexidade da multiplicação tradicional, tornando o cálculo mais rápido e eficiente.

## Como executar o projeto

### Requisitos
- Python 3.x instalado

### Passo a passo
1. Clone este repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd nome_do_projeto
   ```
3. Execute o script principal:
   ```bash
   python main.py
   ```
4. Digite dois números inteiros quando solicitado e visualize o resultado da multiplicação.

## Implementação do Algoritmo de Karatsuba

```python
import math

def karatsuba(x: int, y: int) -> int:
    """
    Implementação do algoritmo de Karatsuba para multiplicação eficiente de dois números inteiros.
    
    :param x: Primeiro número inteiro
    :param y: Segundo número inteiro
    :return: Resultado da multiplicação de x por y
    """
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = math.ceil(n / 2)
    
    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)
    
    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba((low_x + high_x), (low_y + high_y))
    z2 = karatsuba(high_x, high_y)
    
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

if __name__ == "__main__":
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = karatsuba(num1, num2)
    print(f"O resultado da multiplicação é: {resultado}")
```

## Análise da Complexidade do Algoritmo

### Complexidade Assintótica
- Melhor Caso: O(n^log_2(3)) ≈ O(n^1.58)
- Caso Médio: O(n^log_2(3)) ≈ O(n^1.58)
- Pior Caso: O(n^log_2(3)) ≈ O(n^1.58)

### Complexidade Ciclomática
A complexidade ciclomática pode ser calculada através do grafo de fluxo de controle do algoritmo:

- Número de arestas (E): 6
- Número de nós (N): 5
- Número de componentes conexos (P): 1

**Complexidade Ciclomática (M) = E - N + 2P = 6 - 5 + 2(1) = 3**

## Licença
Este projeto está licenciado sob a Licença MIT.
