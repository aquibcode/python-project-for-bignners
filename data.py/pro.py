class solution(object):
    def kthterm(self, arr, k):
        frequency = {}
        for string in arr:
            if string in frequency:
                frequency[string] +=1
            else:
                frequency[string] = 1

        #now count the kth term of string in arr:
        distinct_count = 0
        for string in arr:
            if frequency[string] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return string
        return ""
sol = solution()
k = 1
arr = ["d", "b", "c", "b", "c", "a"]
result = sol.kthterm(arr,k )
print(result)            

        
