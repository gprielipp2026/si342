
def f1(wts, W):
    return [f'(~a{n1} => w{n1} = 0)' for n1 in range(len(wts))]

def f2(wts, W):
    return [f'(a{n1} => w{n1} = {wts[n1]})' for n1 in range(len(wts))]

def f3(wts, W):
    if len(wts) > 1:
        return 'plus('*(len(wts)-1) + 'w0,' + '),'.join([f'w{x}' for x in range(1,len(wts))]) + ')'
    return 'w0'

def f4(wts, W):
    return ' & '.join(f1(wts,W)) + ' & ' + ' & '.join(f2(wts, W)) + ' & sum = ' + f3(wts, W) + ' & sum = ' + str(W)


