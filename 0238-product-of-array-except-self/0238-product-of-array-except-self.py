class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # 1. Set prefix array to length of input array multiplied by 1
        # 2. set postix array to length of input array muplited by 1
        resPreFix = [1] * len(nums)
        resPostFix = [1] * len(nums)
        result = []
        
        #3. Loop through the nums and compute the prefix products
        prefix = 1
        for i in range (len(nums)):
            prefix *= nums[i]
            resPreFix[i] = prefix
        
        print(resPreFix)
        #4. Loop through nums and compute postfix
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix *= nums[i]
            resPostFix[i] = postfix
            
        print(resPostFix)
        
        #5. Now we can compute the values 
        for i in range (len(nums)):
            if i == len(nums) - 1:
                product = resPreFix[i - 1] * 1
                result.append(product)
                return result
            if i > 0:
                product = resPreFix[i - 1] * resPostFix[i + 1]
                result.append(product)
            else:
                product = 1 * resPostFix[i + 1]
                result.append(product)