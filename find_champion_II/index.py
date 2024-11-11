# Código submetido ao LeetCode
# Autores: Ester Lino e Gabriela Tiago

'''
Em um torneio com `n` times, representados como nós em um DAG (grafo acíclico direcionado), encontrar o
"campeão". O campeão é definido como o único nó que não possui outros times (nós) mais fortes que ele,
ou seja, um nó com zero arestas de entrada que pode alcançar todos os outros nós. Se existir apenas um
campeão possível, identificar. Caso contrário, retornar -1.
'''
class Solution(object):
    def findChampion(self, n, edges):
        
        from collections import defaultdict, deque
        
        '''
        Construir o grafo e calcular os graus de entrada. O grafo será representado como 
        uma lista de adjacências e o grau de entrada como um array.
        '''
        grafo = defaultdict(list) 
        grau_entrada = [0] * n 
        
        '''
        Preenche o grafo e os graus de entrada com base nas arestas. Adiciona uma aresta de `u` para `v` no grafo
        e incrementa o grau de entrada de `v`.
        '''
        for u, v in edges:
            grafo[u].append(v)
            grau_entrada[v] += 1 
        
        '''
        Encontrar todos os nós com grau de entrada zero (candidatos a campeão), já que eles não têm nenhum time mais forte.
        Se não houver exatamente um candidato, retorna -1. O candidato único com grau de entrada zero é o potencial campeão.
        '''
        candidatos = []
        for node in range(n):
            if grau_entrada[node] == 0:
                candidatos.append(node)
        if len(candidatos) != 1:
            return -1
        campeao = candidatos[0]
        
        '''
        Verificar se o candidato pode alcançar todos os outros nós. Para isso foi usada a Busca em Largura (BFS). 
        Armazena os nós visitados e faz uma fila para a BFS.
        '''
        nos_visitados = set()
        fila = deque([campeao]) 
        
        '''
        Realizando a BFS. Para cada vizinho do nó atual, se ainda não foi visitado, adiciona na fila.
        '''
        while fila:
            node = fila.popleft()
            nos_visitados.add(node)  
            for vizinho in grafo[node]:
                if vizinho not in nos_visitados:
                    fila.append(vizinho)
        
        '''
        Se o número de nós visitados é igual a `n`, então o candidato alcança todos os nós
        e é o campeão. Caso contrário, retorna -1, pois ele não é o único campeão.
        '''
        if len(nos_visitados) == n:
            return campeao
        else: -1
