# Exercício 841 - Keys and Rooms

## Descrição

Dado um número `n` de salas numeradas de `0` a `n-1`, todas as salas estão trancadas, exceto a sala `0`.
O objetivo é visitar todas as salas. No entanto, não é possível entrar em uma sala trancada sem ter a chave correspondente.

Quando você visita uma sala, você pode encontrar um conjunto de chaves distintas que desbloqueiam outras salas.
O problema consiste em determinar se é possível visitar todas as salas a partir da sala `0`.

-   **Input**: `rooms = [[1],[2],[3],[]]`
-   **Output**: `true`

**Explicação**:

-   Visitamos a sala `0` e pegamos a chave `1`.
-   Em seguida, visitamos a sala `1` e pegamos a chave `2`.
-   Visitamos a sala `2` e pegamos a chave `3`.
-   Finalmente, visitamos a sala `3`.
-   Todas as salas foram visitadas, então retornamos `true`.

-   **Input**: `rooms = [[1,3],[3,0,1],[2],[0]]`
-   **Output**: `false`

**Explicação**:

-   Não conseguimos acessar a sala `2`, pois a chave para abri-la está dentro dela mesma.

## Restrições

-   `n == rooms.length`
-   `2 <= n <= 1000`
-   `0 <= rooms[i].length <= 1000`
-   `1 <= sum(rooms[i].length) <= 3000`
-   `0 <= rooms[i][j] < n`
-   Todos os valores em `rooms[i]` são únicos.

## Solução

A solução foi implementada utilizando o algoritmo de busca em profundidade (DFS) com o uso de uma pilha para armazenar as chaves que permitem visitar os quartos.
