def countConstruct(target,wordBank,memo={}):
    if target in memo.keys():
        return memo[target]
    if target == '':
        return 1
    totalCount = 0
    for word in wordBank:
        if target.find(word) == 0:
            numWaysForRest = countConstruct(target[len(word):],wordBank,memo)
            totalCount+=numWaysForRest
    memo[target] = totalCount
    return totalCount


print( countConstruct('abcdef',['ab','abc','cd','def','abcd'],memo={}))
print( countConstruct('purple',['purp','p','ur','le','purpl'],memo={}))
print( countConstruct('skateboard',['bo','rd','ate','t','ska','sk','boar'],memo={}))
print( countConstruct('enterapotentpot',['a','p','ent','enter','ot','o','t'],memo={}))
print( countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eeee','eee','eeeee'],memo={}))
