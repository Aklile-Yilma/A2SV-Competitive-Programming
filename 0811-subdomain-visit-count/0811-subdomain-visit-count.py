class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        # sub domain count
        count = {}
        
        for item in cpdomains:
            #item description contains "9001 discuss.leetcode.com"
            item_des = item.split(' ')
                        
            # number of visits
            rep = int(item_des[0])
            domain = item_des[1]
            
            
            self.visitCount(count, domain, rep)
            
            splitted_domains = domain.split('.')
            
            if(len(splitted_domains) == 3):
                
                first_domain = splitted_domains[1] + '.' + splitted_domains[2]
                last_domain = splitted_domains[2]
                
                self.visitCount(count, first_domain, rep)
                self.visitCount(count, last_domain, rep)
            else:
                
                last_domain = splitted_domains[1]
                self.visitCount(count, last_domain, rep)
                
        
        return self.constructAnswer(count)
            
            
        
    def visitCount(self, count, domain, rep):
        
        if(domain in count.keys()):
            count[domain] += rep
            
        else:
            count[domain] = rep
            
            
    def constructAnswer(self, count):
        
        answer = []
        
        for key in count.keys():
            answer.append(f'{count[key]} {key}')
            
        return answer
            
        
                
            
            
            
            
            