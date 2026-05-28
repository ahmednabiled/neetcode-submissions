class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = dict()
        hasht = dict()
        if(len(s) != len(t)): return False


        for i in range(len(s)):
            if(s[i] in hashs):
                hashs[s[i]] += 1
            else:
                hashs[s[i]] = 1

            if(t[i] in hasht):
                hasht[t[i]] += 1
            else:
                hasht[t[i]] = 1

        for i in s:
            if i not in hasht or hashs[i] != hasht[i]:
                return False

        return True
