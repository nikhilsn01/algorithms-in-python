memo = dict()
def gridTraveler(m,n,memo):
    key = str(m)+','+str(n)
    if key in memo.keys():
        return memo[key]
    if (m==1) and (n==1):
        return 1
    if m==0 or n==0:
        return 0
    memo[key] = gridTraveler(m-1,n,memo) + gridTraveler(m,n-1,memo)
    return memo[key]



print(gridTraveler(1,1,memo))
print(gridTraveler(2,3,memo))
print(gridTraveler(3,3,memo))
print(gridTraveler(18,18,memo))
