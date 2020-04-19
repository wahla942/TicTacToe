import numpy as np
import secrets
import collections
from IPython.display import clear_output

from check_for_3 import check_for_3
from display import display
from find_dir import find_dir
from next_move import next_move
from row_col_diag import check_rows , check_cols , check_diags



r = secrets.randbelow

score = 0
p_a = 'y'
while p_a == 'y':
    c = input('Wanna go first ? (y/n) : ')
    M = np.array([ '-' for i in range(9)]).reshape(3,3).tolist()
    over = False
    if c == 'y':
        while over == False:
            clear_output()
            display(M)
            i = np.array(input('Enter pos : ').split()).astype('int').tolist()
            while M[i[0]-1][i[1]-1] != '-':
                i = np.array(input('Error !! .Position already occupied .  Enter unoccupied position u autist !!! : ').split()).astype('int').tolist()
            M[i[0] - 1][i[1] - 1] = 'X'

            over , w  , result , M = next_move(M)
            if over == False and '-' not in np.array(M):
                over = True
                result = 'Draw'
            if over:
                display(M)
                if result == 'Draw':
                    print("Result : " , result)
                elif w == '0':
                    print('Computer wins !!')
                else:
                    score += 1
                    print('Player wins !! ')
            else:
                continue
    else:
        M[1][1] = '0'
        while over == False:
            clear_output()
            display(M)
            i = np.array(input('Enter pos : ').split()).astype('int').tolist()
            while M[i[0]-1][i[1]-1] != '-':
                i = np.array(input('Error !! .Position already occupied .  Enter unoccupied position u autist !!! : ').split()).astype('int').tolist()
            M[i[0] - 1][i[1] - 1] = 'X'

            over , w  , result , M = next_move(M)
            if over == False and '-' not in np.array(M):
                over = True
                result = 'Draw'
            if over:
                display(M)
                if result == 'Draw':
                    print("Result : " , result)
                elif w == '0':
                    print('Computer wins !!')
                    score += 1
                else:
                    print('Player wins !! ')
            else:
                continue
    
    p_a = input('Play again (y/n) ? :')

clear_output()
print('Score : ',score)

