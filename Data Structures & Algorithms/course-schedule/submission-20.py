class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for i in range(numCourses):
            graph[i] = []
        for c, pre in prerequisites:
            graph[c].append(pre)

        path = set()

        def dfs(cnum):
            if cnum in path:
                return False
            
            if graph[cnum] == []:
                return True
            
            path.add(cnum)
            for pre in graph[cnum]:
                if not dfs(pre):
                    return False
            path.remove(cnum)
            graph[cnum] = []
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True 