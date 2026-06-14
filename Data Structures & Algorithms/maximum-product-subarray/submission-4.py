class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        since we are multiplying, we will keep default value of
        curr_max and curr_min as 1
        both these variable are used to keep track of max and min product subarray.
        """
        curr_max = 1
        curr_min = 1
        
        """
        res will be default as negative infinity
        """
        res = float('-inf')

        """
        we need to keep track of curr_max and curr_min till point till point.
        curr_min can become curr_max if a negative number is encountered
        curr_max can become curr_min if a negative number is encountered
        """

        for num in nums:
            curr = curr_max * num
            """
            curr can be negative as well as positive, depending upon the num
            curr_max can be
            1. curr element
            2. curr_min * curr element
            3. curr element * curr_max
            """
            curr_max = max(
                curr,
                curr_min * num,
                num
            )
            """
            curr_min can be
            1. curr element itself
            2. curr_max * curr element
            3. curr_min * curr_element
            """
            curr_min = min(curr, num, curr_min * num)
            print(curr_min, curr_max, res)
            res = max(curr_max, res)
        return res
