class Solution:
    def chocolates(self, n : int, arr : List[int]) -> int:
        # code here
        min=arr[0]
        for i in range(0,len(arr)):
            if(arr[i]<min):
                 min=arr[i]
           
        return min
