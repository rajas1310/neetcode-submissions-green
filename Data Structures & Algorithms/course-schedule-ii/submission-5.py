class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for c, pre in prerequisites:
            graph[c].append(pre)

        visited = set()
        cycle = set()
        res = []
        
        def dfs(cnum):
            if cnum in cycle:
                return False
            
            if cnum in visited:
                return True # dfs after this leads to true

            
            cycle.add(cnum)
            for pre in graph[cnum]:
                if not dfs(pre):
                    return False
            cycle.remove(cnum)
            visited.add(cnum)
            res.append(cnum)
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return res



