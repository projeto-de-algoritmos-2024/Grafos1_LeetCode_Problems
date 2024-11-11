# Exercício 765 - Couples Holding Hands

## Descrição do Problema

Há `n` casais sentados em `2n` assentos dispostos em uma linha, e eles desejam segurar as mãos.

As pessoas e os assentos são representados por um array de inteiros `row`, onde `row[i]` é o ID da pessoa sentada no assento `i`.

Os casais são numerados sequencialmente:

-   O primeiro casal é `(0, 1)`, o segundo é `(2, 3)`, e assim por diante.

O objetivo é retornar o **número mínimo de trocas** para que cada casal esteja sentado lado a lado. Uma troca consiste em escolher duas pessoas, e elas trocam de lugar.

### Exemplos

#### Exemplo 1

-   **Entrada:** `row = [0, 2, 1, 3]`
-   **Saída:** `1`
-   **Explicação:** Basta trocar a segunda pessoa (posição 1) com a terceira (posição 2).

#### Exemplo 2

-   **Entrada:** `row = [3, 2, 0, 1]`
-   **Saída:** `0`
-   **Explicação:** Todos os casais já estão sentados lado a lado.

### Restrições

-   `2n == row.length`
-   `2 <= n <= 30`
-   `n` é par.
-   `0 <= row[i] < 2n`
-   Todos os elementos de `row` são únicos.

## Solução

A solução usa o **algoritmo de ciclos** para minimizar o número de trocas.

1. Utilização um dicionário para rastrear a posição de cada pessoa no array `row`.
2. Interação pelos assentos, verificando se as pessoas sentadas lado a lado são um casal.
3. Se não forem, faz uma troca para alinhar o casal, e atualizar o mapeamento de posições.
4. O número total de trocas é retornado ao final.
