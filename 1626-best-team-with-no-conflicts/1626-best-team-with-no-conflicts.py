class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
                                                
        dp = [0]*(1+max(ages))                  
        score_age = sorted(zip(scores, ages))
                                                
        for score, age in score_age:            
            #   –––––  –––––   ––––––––––––––––––                                    
            dp[age] = score +   max(dp[:age+1])   
            #   4       1      [0, 4, 0, 0, 0, 0]
            #   4       2      [0, 4, 8, 0, 0, 0]                                    
            #   5       1      [0, 9, 8, 0, 0, 0]
        
        return max(dp)