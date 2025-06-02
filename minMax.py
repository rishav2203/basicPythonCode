class Solution:
    def get_min_max(self, arr):
        min = arr[0]
        max = arr[0]

        for i in range(1, len(arr)):
            if min > arr[i]:
                min = arr[i]
            if max < arr[i]:
                max = arr[i]

        return (min, max)

if __name__ == "__main__":
    sol = Solution()
    arr = [3, 1, 4, 1, 5, 9, 2]
    print(sol.get_min_max(arr))
