class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

        

    def search(self, word: str) -> bool:
        curr = self.root

        def dfsSearch(i, curr):
            
            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    for child in curr.children.values():
                        if dfsSearch(j+1, child):
                            return True
                    return False
                elif c not in curr.children:
                    return False
                else:
                    curr = curr.children[c]
            return curr.endOfWord
                

        return dfsSearch(0, curr)

    
    


                

        
