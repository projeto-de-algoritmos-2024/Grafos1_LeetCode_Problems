# Código submetido ao LeetCode
# Autores: Gabriela Tiago


class Solution:
    """
    O problema consiste em organizar os casais de forma que fiquem lado a lado, utilizando o mínimo de trocas possíveis.

    - Cada casal é numerado como (0, 1), (2, 3), (4, 5), etc.
    - Dado o array `row`, o elemento `row[i]` representa o ID da pessoa na posição `i`.
    - O objetivo é fazer com que pessoas do mesmo casal (IDs consecutivos) estejam em assentos consecutivos.

    Utilizaremos um algoritmo de ciclo para minimizar as trocas.
    """

    def minSwapsCouples(self, row):
        # Mapeamento de cada pessoa para sua posição atual
        pos = {person: i for i, person in enumerate(row)}
        swaps = 0

        # Função auxiliar para realizar a troca de duas pessoas e atualizar o mapeamento
        def swap(i, j):
            pos[row[i]], pos[row[j]] = j, i
            row[i], row[j] = row[j], row[i]

        # Percorremos o array tentando alinhar os casais
        for i in range(0, len(row), 2):
            # Identificamos o par que deve estar sentado ao lado
            x = row[i]
            y = x ^ 1  # Encontramos o par da pessoa atual (ex: 0 -> 1, 2 -> 3)

            # Se o par correto não estiver ao lado, fazemos a troca
            if row[i + 1] != y:
                swap(i + 1, pos[y])
                swaps += 1

        return swaps
