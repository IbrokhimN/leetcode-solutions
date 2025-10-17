class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        store = []
        nums.append(-1005)
        count, n = 1, len(nums)
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                count += 1class Solution:
    def hasIncreasingSubarrays(self, a: List[int], k: int) -> bool:
        s = []
        a.append(-1005)
        c, n = 1, len(a)

        for i in range(1, n):
            if a[i - 1] < a[i]:
                c += 1
            else:
                s.append(c)
                c = 1

        kk = k * 2
        n = len(s)

        for i in range(1, n):
            if s[i - 1] >= k and s[i] >= k:
                return True

        for x in s:
            if x >= kk:
                return True

        return False

            else:
                store.append(count)
                count = 1
        
        _2x = k + k
        n = len(store)
        for i in range(1, n):
            if store[i - 1] >= k and store[i] >= k:
                return True

        for x in store:
            if x >= _2x:
                return True
        return False
