# Exercício 847 - Shortest Path Visiting All Nodes

## Descrição do Problema

Dado um grafo não-direcionado e conectado de `n` nós, rotulados de `0` a `n-1`. Você recebe um array `graph` onde `graph[i]` é uma lista de todos os nós conectados ao nó `i` por uma aresta.

Seu objetivo é retornar o comprimento do caminho mais curto que visita todos os nós. Você pode começar e parar em qualquer nó, pode revisitar nós várias vezes e pode reutilizar as arestas.

### Exemplos

#### Exemplo 1

-   **Entrada:** `graph = [[1,2,3],[0],[0],[0]]`
-   **Saída:** `4`
-   **Explicação:** Um possível caminho é `[1,0,2,0,3]`.

#### Exemplo 2

-   **Entrada:** `graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]`
-   **Saída:** `4`
-   **Explicação:** Um possível caminho é `[0,1,4,2,3]`.

### Restrições

-   `n == graph.length`
-   `1 <= n <= 12`
-   `0 <= graph[i].length < n`
-   `graph[i]` não contém `i`.
-   Se `graph[a]` contém `b`, então `graph[b]` contém `a`.
-   O grafo de entrada é sempre conectado.

## Solução

A solução para este problema utiliza a técnica de **Busca em Largura (BFS)** com o uso de um **bitmask** para representar os estados dos nós visitados.

### Estratégia

-   Cada estado é definido como `(nó_atual, máscara, passos)`:
-   **nó_atual**: o nó em que estamos atualmente.
-   **máscara**: um inteiro onde cada bit indica se um nó foi visitado (1) ou não (0).
-   **passos**: o número de passos realizados até este ponto.
-   A BFS garante que encontraremos o caminho mais curto para visitar todos os nós.
-   Utilizamos um conjunto (`visitados`) para armazenar os estados visitados e evitar ciclos desnecessários.

### Complexidade

-   **Tempo:** `O(2^n * n^2)`, onde `n` é o número de nós. Esta complexidade é aceitável para `n <= 12`.
-   **Espaço:** `O(2^n * n)`, pois armazenamos o estado de cada nó e sua máscara.

### Como Executar

Para executar a solução, utilize o comando:

```bash
python index.py
```
