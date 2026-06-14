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
            1. current element
            2. curr_min * current element
            3. current element * curr_max
            """
            curr_max = max(
                curr,
                curr_min * num,
                num
            )
            """
            curr_min can be negative and positive also
            1. current element itself (if curr_min is negative, then curr_min * curr_element will be positive)
            2. curr_max * current element (if curr_max is positive, then curr_max * current element will be negative given current element is negative)
            3. curr_min * curr_element (if curr_min is positive, curr_min will be negative given current element is negative)
            """
            curr_min = min(curr, num, curr_min * num)
            res = max(curr_max, res)
        return res