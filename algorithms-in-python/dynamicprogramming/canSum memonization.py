
memo = dict()
def canSum(targetSum,numbers,memo):
    if targetSum in memo.keys():
        return True
    if targetSum==0:
        return True
    if targetSum<0:
        return False
    for num in numbers:
        remainder = targetSum-num;
        if canSum(remainder,numbers,memo) == True:
            memo[targetSum] = True
            return True
        memo[targetSum] = False
    return False

print(canSum(7,[2,3],memo))
memo = {}
print(canSum(8,[2,3,5],memo))
memo = {}
print(canSum(7,[5,3,4,7],memo))
memo = {}
print(canSum(7,[2,4],memo))
memo = {}
print(canSum(1801,[7,14],memo))
print(memo)
