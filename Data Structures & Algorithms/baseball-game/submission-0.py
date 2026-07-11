class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for i in range(len(operations)):
            if operations[i]=="+":
                arr.append(arr[-2]+arr[-1])
            elif operations[i]=="C":
                arr.pop()
            elif operations[i]=="D":
                arr.append(arr[-1]*2)
            else:
                arr.append(int(operations[i]))
        inte = 0
        for i in range(len(arr)):
            inte = inte+arr[i]
        return inte
