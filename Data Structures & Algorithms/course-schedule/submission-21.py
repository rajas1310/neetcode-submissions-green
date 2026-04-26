class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for c, pre in prerequisites:
            graph[c].append(pre)

        def dfs(cnum):
            if cnum in path:
                return False
            
            path.add(cnum)
            for pre in graph[cnum]:
                if not dfs(pre):
                    return False
            path.remove(cnum)
            return True
        
        for i in range(numCourses):
            path = set()
            if not dfs(i):
                return False
        return True