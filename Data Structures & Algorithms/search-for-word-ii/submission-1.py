class Node:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self) -> None:
        self.root = Node()
    
    def insert(self, word:str):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.endOfWord = True
    
    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.insert(w)

        ROWS, COLS = len(board), len(board[0])
        res = set()

        def dfs(r, c, node, word):
            nonlocal res
            if 0<= r < ROWS and 0 <= c < COLS and board[r][c] != "#" and board[r][c] in node.children:
                node = node.children[board[r][c]]
                word += board[r][c]

                if node.endOfWord:
                    res.add(word)
                    # return

                
                
                temp = board[r][c]
                board[r][c] = "#"
                
                dfs(r-1, c, node, word)
                dfs(r+1, c, node, word)
                dfs(r, c-1, node, word)
                dfs(r, c+1, node, word)

                board[r][c] = word[-1]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")

        return list(res)

        