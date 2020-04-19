def next_move(X):
    X_np = np.array(X)
    if '0' not in X_np:
        if X[1][1] != 'X':
            X[1][1] = '0'
        else:
            r_c = r(9)
            if r_c == 4:
                r_c = r(9)
            X[r_c//3][r_c%3] = '0'
            over = False
            res = 'dsad'
        Arr = X
    elif check_for_3(X):
        return True , 'X' , 'Opponent' , X
    else : 
        over,X,res,Arr = find_dir(X)
        
    return over , X , res , Arr