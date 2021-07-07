
memo = {}
def howSum(targetSum,numbers,memo):
    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum<0:
        return None
    for num in numbers:
        remainder = targetSum-num
        reamainderResult = howSum(remainder,numbers,memo)
        if reamainderResult != None:
            reamainderResult.append(num)
            memo[targetSum] = reamainderResult
            return memo[targetSum]
    memo[targetSum] = None
    return None
memo = {}
print(howSum(7,[2,3],memo))
memo = {}
print(howSum(8,[2,3,5],memo))
memo = {}
print(howSum(7,[5,3,4,7],memo))
memo = {}
print(howSum(7,[2,4],memo))
memo = {}
print(howSum(210,[7,21],memo))