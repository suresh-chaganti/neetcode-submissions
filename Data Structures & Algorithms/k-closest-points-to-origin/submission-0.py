class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
    
        from collections import defaultdict
        elements_distance = defaultdict(list)
        final_list = []
        base = [0,0]
        for point in points:
            # x = point[0] - base[0]
            # y = point[1] - base[1]
            distance = point[0] ** 2 + point[1] ** 2
            # Logic from user's snippet
            elements_distance[distance].append(point)
            
        # 2. Sort the unique distances
        sorted_distances_keys = sorted(elements_distance.keys())   
          
        
        for key in sorted_distances_keys:
            for element in elements_distance[key]:
                final_list.append(element)
                if len(final_list) == k:
                    return final_list

        

    
        