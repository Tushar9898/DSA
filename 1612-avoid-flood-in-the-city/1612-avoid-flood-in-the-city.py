import bisect

class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        n = len(rains)
        ans = [-1] * n
        full = set()  
        last_rain = {}  
        dry_days = []  
        
        for i, lake in enumerate(rains):
            if lake == 0:
                bisect.insort(dry_days, i)
                ans[i] = 1  
            else:
                if lake in full:
                    prev_day = last_rain[lake]
                    idx = bisect.bisect_right(dry_days, prev_day)
                    if idx == len(dry_days):
                        return []  
                    dry_day = dry_days.pop(idx)
                    ans[dry_day] = lake  
                full.add(lake)
                last_rain[lake] = i
                ans[i] = -1  
        
        return ans
