class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        #https://www.youtube.com/watch?v=4ndmX1FvZks
        visit_count={}
        for main_domain in cpdomains:
            count,parent_domains=main_domain.split(' ')
            count=int(count)
            subdomains=parent_domains.split('.')
            #print(count)
            #print(subdomains)
            for i in range(len(subdomains)):
                domain='.'.join(subdomains[i:])
                #print(domain)
                if domain not in visit_count:
                    visit_count[domain]=count
                else:
                    visit_count[domain]+=count
        #print(visit_count)
        result=[]
        for domain, count in visit_count.items():
            result.append("{0} {1}".format(count,domain))
        #print(result)
        return result

