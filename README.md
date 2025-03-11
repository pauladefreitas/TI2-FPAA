# Implementação do Algoritmo de Seleção Simultânea do Maior e do Menor Elementos (MaxMin Select) em Python

O algoritmo de seleção simultânea (MaxMin Select) pode ser implementado de forma recursiva, utilizando a técnica de divisão e conquista. O problema é dividido em subproblemas menores que são resolvidos recursivamente, e seus resultados são combinados para encontrar o maior e o menor elementos com eficiência. Esse método reduz o número de comparações necessárias em comparação com uma abordagem ingênua.

## Implementação do Algoritmo

A implementação inicia-se com a declaração da função recursiva principal do algoritmo MaxMin Select.

```python
   def maxmin(lista):
```

A partir disso, há uma verificação de tamanho da lista. Caso o tamanho da lista for 1, significa que há apenas um valor presente, portanto este é o maior e o menor número.

```python
    if len(lista) == 1:
        result = [lista[0], lista[0]]
        return result
```

Logo após,karatsuba há outra verificação de tamanho da lista. Dessa vez, se o tamanho for 2, os valores são diretamente comparados para identificar um mínimo e um máximo.

```python
    if len(lista) == 2:
        if lista[0] > lista[1]: #comparação
            max_d = lista[0]    #atribuição de valor
            min_d = lista[1]
        else:
            max_d = lista[1]
            min_d = lista[0]
```

A próxima etapa divide a lista em duas sublistas para realizar a estratégia de divisão e conquista.

```python
    meio = len(lista)//2
    esquerda = lista[:meio]
    direita = lista[meio:]
```

Assim, há uma recursão para que a lista continue diminuindo até que encaixe em alguma das condições dos _ifs_ mencionados anteriormente.

```python
    min_esq, max_esq = maxmin(esquerda)
    min_dir, max_dir = maxmin(direita)
```

Então, há uma comparação entre os mínimos encontrados (os mínimos de cada sublista) e os máximos encontrados (os máximos de cada sublista).

```python
    min_total = min(min_esq, min_dir)
    max_total = max(max_esq, max_dir)
```

Finalmente, como boa prática, é criada a variável _result_ que contém um _array_ de apenas dois objetos: o mínimo e o máximo. O retorno da função é essa variável.

```python
    result = [min_total, max_total]
    return result
```

## Como rodar em ambiente local?

### Passo 1: Clonar o repositório

1. Clone o repositório git em uma pasta no seu ambiente local com o seguinte comando:

   ```bash
   git clone https://github.com/pauladefreitas/TI2-FPAA.git
   cd TI2-FPAA
   ```

### Passo 2: Executar o script

1. Execute o script principal:

   ```bash
   python main.py
   ```

2. O programa solicitará que você insira números e quando quiser terminar a lista, digite FIM, como:

   ```bash
   Digite os números da sua lista. Para parar, digite FIM.
   ```

3. O resultado será exibido logo depois.

## Relatório técnico

### Análise da Complexidade Assintótica
