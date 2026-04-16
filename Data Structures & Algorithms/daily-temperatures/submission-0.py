class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmer_than_today_after_days = []
        for i in range(len(temperatures)):
            
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    warmer_than_today_after_days.append(j-i)
                    break
                if j == len(temperatures)-1:
                    warmer_than_today_after_days.append(0)

        return   warmer_than_today_after_days


                
            
            
        
        return   warmer_than_today_after_days
         




        