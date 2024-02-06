class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap={}
        for st in strs:
            sorted_str=''.join(sorted(st))
            if sorted_str in hashmap:
                hashmap[sorted_str].append(st)
            else:
                hashmap[sorted_str]=[st]
        return list(hashmap.values())