# Código submetido ao LeetCode
# Autores: Gabriela Tiago e Ester Lino

class Solution:
    """
    O objetivo é visitar todas os quartos usando as chaves disponíveis em cada quarto.
    Vamos entrar em todas os quartos enquanto tivermos as chaves para destrancá-los.
    Este código utiliza o algoritmo de Busca em Profundidade (DFS) utilizando uma pilha
    para armazenar as chaves que abrem os quartos.
    """

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        quartos_visitados = set()  # Conjunto para armazenar os quartos já visitados
        pilha = [0]  # Começamos pelo quarto 0, que está destrancado

        # Executa enquanto houver quartos na pilha
        while pilha:
            quarto = pilha.pop()  # Remove uma quarto da pilha
            quartos_visitados.add(quarto)  # Marca o quarto como visitado
            # Percorre todos os chaves encontrados no quarto atual
            for chave in rooms[quarto]:
                # Se a chave leva a um quarto ainda não visitado, adiciona na pilha
                if chave not in quartos_visitados:
                    pilha.append(chave)

        # Verifica se o número de quartos visitados é igual ao total de quartos
        return len(quartos_visitados) == len(rooms)
