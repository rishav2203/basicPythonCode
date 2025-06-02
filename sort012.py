class Solution:
    def sort012(self, arr):
        a0 = 0
        a1 = 0
        a2 = len(arr) - 1

        while a1 <= a2:
            if arr[a1] == 0:
                arr[a0], arr[a1] = arr[a1], arr[a0]
                a0 += 1
                a1 += 1
            elif arr[a1] == 1:
                a1 += 1
            else:
                arr[a1], arr[a2] = arr[a2], arr[a1]
                a2 -= 1
        return arr

if __name__ == "__main__":
    arr = [0, 1, 2, 0, 1, 2, 1, 0]
    sol = Solution()
    result = sol.sort012(arr)
    print("Sorted array:", result)