def check_rows(X):
    i = 0
    for j in range(3):
        row = X[j]
        counts = collections.Counter(row)
        if counts['-'] == 1 and ( counts['X'] == 2 or counts['0'] == 2 ):
            if counts['X'] == 2:
                ele = 'X'
            else:
                ele = '0'
            i = 3*j + row.index('-')
            return [ele , i]
    return [None , None]

def check_cols(X):
    X_np = np.array(X)
    for j in range(3):
        l = X_np[:,j].tolist()
        counts = collections.Counter(l)
        if counts['-'] == 1 and ( counts['X'] == 2 or counts['0'] == 2 ):
            if counts['X'] == 2:
                ele = 'X'
            else:
                ele = '0'
            i = 3*l.index('-') + j
            return [ele , i]
    return [None , None]

def check_diags(X):
    X_np = np.array(X)
    d0 = np.diag(X_np).tolist()
    d1 = np.diag(np.flip(X_np , 1)).tolist()
    D = [d0,d1]
    for j in range(2):
        diag = D[j]
        counts = collections.Counter(diag)
        if counts['-'] == 1 and ( counts['X'] == 2 or counts['0'] == 2 ):
            if counts['X'] == 2:
                ele = 'X'
            else:
                ele = '0'
            i = diag.index('-') 
            if j == 0:
                i = 3*i + i
            else:
                i = 2*(i+1)
            return [ele , i]
    return [None , None]