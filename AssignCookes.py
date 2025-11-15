class Solution:
    def findContentChildren(self, g, s):
       
        g.sort()

        
        s.sort()

        children = 0 
        cookies = 0  
        count = 0  

        # Try to match children and cookies from smallest to largest
        while children < len(g) and cookies < len(s):
            if s[cookies] >= g[children]:
                
                count += 1
                children += 1  
                cookies += 1  
            else:
                
                cookies += 1

        return count
