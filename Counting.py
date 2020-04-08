class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for i in range(0, len(arr)):
            sum1 = arr[i] + 1
            if sum1 in arr:
                count += 1
        return count