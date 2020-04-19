def check_for_3(X):
    X_np = np.array(X)
    posiblts = []
    for i in range(3):
        r = X[i]
        counts = collections.Counter(r)
        if counts['X'] == 3:
            return True 
    for i in range(3):
        c = (X_np[:,i]).tolist()
        counts = collections.Counter(c)
        if counts['X'] == 3:
            return True 
    d0 = np.diag(X_np).tolist()
    d1 = np.diag(np.flip(X_np , 1)).tolist()
    D = [d0,d1]
    
    for d in D:
        counts = collections.Counter(d)
        if counts['X'] == 3:
            return True
    
    return False