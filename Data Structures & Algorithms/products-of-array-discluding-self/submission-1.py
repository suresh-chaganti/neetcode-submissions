class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 0 if nums.count(0)>1 else 1
        products_array = []
        
        for num in nums:
                if num != 0:
                    total_product = total_product * num
            
        if 0 in nums:
            for num in nums:
                if num == 0:
                    products_array.append(total_product)
                else:
                    products_array.append(0)
        else:
            for num in nums:
                products_array.append((int(total_product/num)))
            
        return products_array

    

        

        