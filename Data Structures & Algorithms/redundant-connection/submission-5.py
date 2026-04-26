class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                elif not dfs(nei, node):
                    return False
            return True
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

            visited = set()
            if not dfs(u, -1):
                return [u,v]
        
        return []
            
