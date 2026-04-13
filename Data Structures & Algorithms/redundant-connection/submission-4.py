class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(node, parent):
            if visited[node]:
                return True
            
            visited[node] = True
            for nei in graph[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    return True
            return False

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

            visited = [False] * (len(edges) + 1)
            if dfs(u,-1):
                return [u,v]

        return [] 

        
        

        