class Solution:
    def removeDuplicates(self, nums):

        # i points to the last unique element
        i = 0

        # j scans the array from the second element
        for j in range(1, len(nums)):

            # If we found a new unique number
            if nums[j] != nums[i]:

                # Move i to the next position
                i += 1

                # Put the new unique number there
                nums[i] = nums[j]

        # i is an index, so number of elements = i + 1
        return i + 1