class Solution:
    def segregateElements(self, arr):
        
        result = []
        for i in range(0,len(arr)) :
            if arr[i] >= 0 :
                result.append(arr[i])
                
        for i in range(0,len(arr)) :
            if arr[i] < 0 : 
                result.append(arr[i])
        
        for i in range(0,len(arr)) : 
            arr[i] = result[i]
        #arr = result
        
        return arr

if __name__ == "__main__":
    arr = [1, -1, 3, 2, -7, -5, 11, 6]
    sol = Solution()
    result = sol.segregateElements(arr)
    print("Segregated Elements:", result)
