# Código submetido ao LeetCode
# Autores: Ester Lino e Gabriela Tiago

'''
O problema exige encontrar o caminho mais curto que visita todos os nós em um grafo não direcionado, 
podendo iniciar e terminar em qualquer nó. O grafo é representado por uma lista de adjacência onde 
cada nó está conectado a outros por uma aresta. Para encontrar a soluçaõ foi usada a BFS (Busca em Largura).
'''

class Solution(object):
    def shortestPathLength(self, grafo):
        from collections import deque

        '''
        Número de nós no grafo e máscara de bits que indica que todos os nós foram visitados.
        '''
        n = len(grafo)
        todos_visitados = (1 << n) - 1
        
        '''
        Inicializa a fila para a BFS com tuplas (nó i, máscara de visitados (1<<i), 0 passos).
        '''
        fila = deque()
        for i in range(n):
            fila.append((i, 1 << i, 0))
        
        '''
        Conjunto para acompanhar os estados visitados (nó, máscara de visitados).
        '''
        visitados = set()
        for i in range(n):
            visitados.add((i, 1 << i))
        
        '''
        Desempilha um estado da fila. Se todos os nós foram visitados, retorna o 
        número de passos
        '''
        while fila:
            no, mascara_visitados, passos = fila.popleft()
            if mascara_visitados == todos_visitados:
                return passos
            
            '''
            Explora os vizinhos do nó atual. Calcula a nova máscara de visitados após 
            visitar o vizinho.
            '''
            for vizinho in grafo[no]:
                nova_mascara_visitados = mascara_visitados | (1 << vizinho)
                
                ''' 
                Se o novo estado (nó, nova máscara de visitados) ainda não foi visitado, 
                marca o novo estado como visitado.
                '''
                if (vizinho, nova_mascara_visitados) not in visitados:
                    visitados.add((vizinho, nova_mascara_visitados))
                    
                    '''
                    Adiciona o novo estado à fila com um incremento no número de passos.
                    '''
                    fila.append((vizinho, nova_mascara_visitados, passos + 1))