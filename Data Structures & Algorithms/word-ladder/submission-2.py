class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        graph = defaultdict(list) # pattern : [words,..]
        
        # create adj List
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                graph[pattern].append(word)
        
        q = deque()
        q.append(beginWord)
        visited = set([beginWord])
        level = 1
        while q:
            for i in range(len(q)):
                cur_word = q.popleft()

                if cur_word == endWord:
                    return level
                
                for j in range(len(cur_word)):
                    pattern = cur_word[:j] + "*" + cur_word[j+1:]
                    for child in graph[pattern]:
                        if child not in visited:
                            q.append(child)
                            visited.add(child)
            level += 1

        return 0