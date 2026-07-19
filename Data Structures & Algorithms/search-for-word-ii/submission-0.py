class TrieNode:
    def __init__(self):
        self.children= {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)
        rows = len(board)
        cols = len(board[0])
        ans = set()
        visited = set()

        def dfs(r,c, node,  word):
            if (r<0 or c<0 or r==rows or c==cols or 
            (r,c) in visited or board[r][c] not in node.children):
                return 
            visited.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.endOfWord:
                ans.add(word)
            dfs(r+1,c, node, word)
            dfs(r-1,c, node, word)
            dfs(r,c+1, node, word)
            dfs(r,c-1, node, word)
            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c, trie.root, "")
        return list(ans)