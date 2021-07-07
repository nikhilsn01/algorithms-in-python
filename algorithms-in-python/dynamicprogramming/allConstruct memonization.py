def allConstruct(target,wordBank,memo={}):
    if target in memo.keys():
        return memo[target]
    if target == '':
        return [[]]
    result = []
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix,wordBank,memo)
            for i in suffixWays:
                i.insert(0,word)
                result.append(i)
    return result





print( allConstruct('abcdef',['ab','abc','cd','def','abcd'],memo={}))
print( allConstruct('purple',['purp','p','ur','le','purpl'],memo={}))
print( allConstruct('skateboard',['bo','rd','ate','t','ska','sk','boar'],memo={}))
print( allConstruct('enterapotentpot',['a','p','ent','enter','ot','o','t'],memo={}))
print( allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eeee','eee','eeeee'],memo={}))


