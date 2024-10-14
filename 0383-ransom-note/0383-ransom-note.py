class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # instead of counting every char
        st1, st2 = Counter(ransomNote), Counter(magazine)
        # check intersection
        if st1 & st2 >= st1:
            return True
        return False
        