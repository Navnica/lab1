def foo(n):
    ret = n.split(' ')
    for x in ret:
        if x == '':
            ret.remove(x)
            
    return ret[0]
