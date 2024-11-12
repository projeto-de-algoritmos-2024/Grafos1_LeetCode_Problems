# Código submetido ao LeetCode
# Autores: Gabriela Tiago


class Solution:
    """
    O problema consiste em organizar os casais de forma que fiquem lado a lado, utilizando o mínimo de trocas possíveis.

    - Cada casal é numerado como (0, 1), (2, 3), (4, 5), etc.
    - Dado o array `row`, o elemento `row[i]` representa o ID da pessoa na posição `i`.
    - O objetivo é fazer com que pessoas do mesmo casal (IDs consecutivos) estejam em assentos consecutivos.
    """

    def minSwapsCouples(self, row):
        n = len(row) // 2  # Número de casais
        graph = {i: [] for i in range(n)}  # Criando um grafo com n vértices para os casais

        # Mapeamento de posições para pessoas
        _ = {person: i for i, person in enumerate(row)}

        # Construindo as arestas do grafo para casais
        for i in range(0, len(row), 2):
            a, b = row[i], row[i + 1]
            couple1 = a // 2
            couple2 = b // 2

            # Adicionando uma aresta entre os casais atuais
            if couple1 != couple2:
                graph[couple1].append(couple2)
                graph[couple2].append(couple1)

        # Função de DFS para encontrar componentes conectados
        def dfs(node, visited):
            stack = [node]
            visited.add(node)
            size = 0
            while stack:
                u = stack.pop()
                size += 1
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        stack.append(v)
            return size

        visited = set()
        swaps = 0

        # Percorrendo todos os casais e contando os ciclos
        for i in range(n):
            if i not in visited:
                cycle_size = dfs(i, visited)
                # Para um ciclo de tamanho k, precisamos de (k - 1) trocas para alinhá-lo
                if cycle_size > 1:
                    swaps += cycle_size - 1

        return swaps