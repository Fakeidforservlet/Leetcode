class Solution(object):
    def char_freq_count(self,s):
        dic={}
        for ch in s:
            if ch in dic:
                dic[ch]+=1
            else:
                dic[ch]=1
        char_count_str=''
        for char in sorted(dic.keys()):
            char_count_str+=char+str(dic[char])
        return char_count_str
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # hashmap={}
        # for st in strs:
        #     sorted_str=''.join(sorted(st))
        #     if sorted_str in hashmap:
        #         hashmap[sorted_str].append(st)
        #     else:
        #         hashmap[sorted_str]=[st]
        # return list(hashmap.values())

        #https://www.youtube.com/watch?v=C9V66KyZCP8
        hashmap={}
        for s in strs:
            char_count_str=self.char_freq_count(s)
            if char_count_str in hashmap:
                hashmap[char_count_str].append(s)
            else :
                hashmap[char_count_str]=[s]
        return list(hashmap.values())