class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        startvalues = []
        endvalues = []
        results = []
        for subarray in sorted(intervals):
            startvalues.append(subarray[0])
            endvalues.append(subarray[1])
        i= 1
        results.append([startvalues[0], endvalues[0]])
        while i < len(startvalues):
            if endvalues[i] < results[-1][1]:
                i+=1
                continue
            elif results[-1][1] >= startvalues[i]:
                results[-1][1] = endvalues[i]
            else:
                results.append([startvalues[i], endvalues[i]])
            i += 1
        return results

print(Solution.merge(None, [[1,3],[2,5]]))
print(Solution.merge(None, [[4,7],[1,4]]))
print(Solution.merge(None, [[1,4],[2,3]]))
print(Solution.merge(None, [[1,4],[0,2],[3,5]]))