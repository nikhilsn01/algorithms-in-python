
def bestSum(targetSum,numbers,memo={}):
    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum<0:
        return None
    myShortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        reamainderCombination = bestSum(remainder,numbers,memo)
        if reamainderCombination != None:
            reamainderCombination.append(num)
            combination = reamainderCombination
            if (myShortestCombination == None) or (len(combination) < len(myShortestCombination)):
                myShortestCombination = combination
    memo[targetSum] = myShortestCombination
    return myShortestCombination


print(bestSum(7,[5,3,4,7],memo={}))
print(bestSum(8,[2,3,5],memo={}))
print(bestSum(8,[1,4,5],memo={}))
print(bestSum(100,[1,2,5,25],memo={}))
