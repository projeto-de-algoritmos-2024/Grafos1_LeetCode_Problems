# Exercício 847 - Shortest Path Visiting All Nodes

## Descrição

Você tem um grafo não direcionado e conectado de `n` nós rotulados de `0` a `n - 1`. Você recebe um array `graph` onde `graph[i]` é uma lista de todos os nós conectados com o nó `i` por uma aresta.

Retorna o comprimento do caminho mais curto que visita cada nó . Você pode começar e parar em qualquer nó, pode revisitar nós várias vezes e pode reutilizar arestas.

## Exemplo 1

![Exemplo 1](./imagens/shortest1-graph.jpg)

Entrada: `grafo = [[1,2,3],[0],[0],[0]]`</br>
Saída: `4`</br>
Explicação: `Um caminho possível é [1,0,2,0,3]`

## Exemplo 2

![Exemplo 2](./imagens/shortest2-graph.jpg)

Entrada: `grafo = [[1],[0,2,4],[1,3,4],[2],[1,2]]`
Saída: `4`
Explicação: `Um caminho possível é [0,1,4,2,3]`

## Restrições

- `n == graph.length`
- `1 <= n <= 12`
- `0 <= graph[i].length < n`
- `graph[i]` não contém `i`
- Se `graph[a]` contém `b`, então `graph[b]` contém `a`
- `edges[i][0] != edges[i][1]`
- O grafo de entrada está sempre conectado.
