class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        currLine = []
        currLen = 0

        for i in range(len(words)):
            # curr line already longer than maxwidth
            if currLen + len(currLine)+ len(words[i]) > maxWidth:
                spaces = (maxWidth - currLen)//max(1,len(currLine)-1)
                extra = (maxWidth - currLen)%max(1,len(currLine)-1)

                for j in range(max(1,len(currLine)-1)):
                    currLine[j]+=" "*spaces
                    if extra:
                        currLine[j] += " "
                        extra -= 1
                ans.append("".join(currLine))
                currLine = []
                currLen = 0

            # curr line can add the word
            currLine.append(words[i])
            currLen += len(words[i])

            if i==len(words)-1:
                for j in range(max(1,len(currLine)-1)):
                    currLine[j]+=" "
                    currLen+=1
                extra = maxWidth - currLen
                currLine.append(" "*extra)
                ans.append("".join(currLine))
        return ans
        


        