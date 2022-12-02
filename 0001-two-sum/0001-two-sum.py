class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          # Create a hash table to store the numbers in the array
        table = {}

    # Iterate over the numbers in the array
        for i, num in enumerate(nums):
        # Check if the difference between the target and the current number exists in the hash table
            if target - num in table:
            # If it does, we have found the two numbers that add up to the target,
            # so we can return their indices
                return [table[target - num], i]

        # If the difference does not exist in the hash table, add the current number to the table
            table[num] = i

    # If we reach this point, we have not found the two numbers that add up to the target,
    # so we return an empty list
        return []