class Solution(object):
    def count_character(self,string):
            hashmap={}
            for i in string:
                if i not in hashmap:
                    hashmap[i]=0
                else:
                    hashmap[i]+=1
            return hashmap
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_hashmap=self.count_character(s)
        t_hashmap=self.count_character(t)

        return s_hashmap==t_hashmap

        