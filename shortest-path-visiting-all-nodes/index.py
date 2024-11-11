# Código submetido ao LeetCode
# Autores: Gabriela Tiago

from collections import deque


class Solution:
    """
    Este problema é resolvido utilizando busca em largura (BFS) com um bitmask para representar
    os estados dos nós visitados. A ideia é visitar todos os nós com o menor número de movimentos.

    - n é o número de nós no grafo.
    - Utilizamos a BFS pois ela garante encontrar o caminho mais curto para visitar todos os nós.
    - Cada estado na fila é representado por (nó_atual, máscara, passos), onde:
        - nó_atual: o nó onde estamos atualmente.
        - máscara: um inteiro onde cada bit indica se um nó foi visitado (1) ou não (0).
        - passos: o número de passos tomados até este ponto.
    """

    def shortestPathLength(self, graph):
        n = len(graph)
        # Estado inicial para cada nó no grafo
        queue = deque([(i, 1 << i, 0) for i in range(n)])
        visitados = set((i, 1 << i) for i in range(n))

        # BFS para encontrar o caminho mais curto
        while queue:
            no_atual, mascara, passos = queue.popleft()

            # Se todos os nós foram visitados, a máscara terá todos os bits iguais a 1
            if mascara == (1 << n) - 1:
                return passos

            # Percorrendo os vizinhos do nó atual
            for vizinho in graph[no_atual]:
                nova_mascara = mascara | (1 << vizinho)
                if (vizinho, nova_mascara) not in visitados:
                    visitados.add((vizinho, nova_mascara))
                    queue.append((vizinho, nova_mascara, passos + 1))

        return -1  # Caso não encontre um caminho
