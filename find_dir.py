def find_dir(X):
    res = check_rows(X) + check_cols(X) + check_diags(X)
    if '0' in res:
        pos = res[res.index('0') + 1]
        X[pos//3][pos%3] = '0'
        return True , '0' , 'Computer' , X 
    
    elif 'X' in res:
        pos = res[res.index('X') + 1]
        X[pos//3][pos%3] = '0'
    
    else:
        print('1')
        if '-' not in np.array(X):
            print('2')
            if check_for_3(X):
                return True , 'X' , 'Opponent' , X
            else:
                return True , 'Null' , 'Draw' , X
        
        else:
#             print('4')
            pos = r(9)
            flag = False
            while X[pos//3][pos%3] != '-':
                pos = r(9)
            if X[pos//3][pos%3] == '-':
                flag = True
                X[pos//3][pos%3] = '0' 
    return False , 'o' ,   'nul' , X