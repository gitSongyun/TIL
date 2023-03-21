import pandas as pd
from itertools import combinations

def solution(l):

    colname = range(len(l[0]))

    data = pd.DataFrame(l)
    data_ = pd.DataFrame()

    유일성만족리스트 = []
    모든이름의조합 = []

    for 조합수 in range(1, len(colname)+1):
        컬럼이름의조합 = combinations(colname, 조합수)
        모든이름의조합.append(list(컬럼이름의조합))

    for 이름조합 in 모든이름의조합:
        for 컬럼명 in 이름조합:
            #print(컬럼명)
            if len(컬럼명) == 1:
                data_[f'data[{컬럼명[0]}]'] = data[컬럼명[0]]
            elif len(컬럼명) == 2:
                data_[f'data[{컬럼명[0]}] + data[{컬럼명[1]}]'] = data[컬럼명[0]] + data[컬럼명[1]]
            elif len(컬럼명) == 3:
                data_[f'data[{컬럼명[0]}] + data[{컬럼명[1]}] + data[{컬럼명[2]}]'] = data[컬럼명[0]] + data[컬럼명[1]] + data[컬럼명[2]]
            elif len(컬럼명) == 4:
                data_[f'data[{컬럼명[0]}] + data[{컬럼명[1]}] + data[{컬럼명[2]}] + data[{컬럼명[3]}]'] = data[컬럼명[0]] + data[컬럼명[1]] + data[컬럼명[2]] + data[컬럼명[3]]
            elif len(컬럼명) == 5:
                data_[f'data[{컬럼명[0]}] + data[{컬럼명[1]}] + data[{컬럼명[2]}] + data[{컬럼명[3]}] + data[{컬럼명[4]}]'] = data[컬럼명[0]] + data[컬럼명[1]] + data[컬럼명[2]] + data[컬럼명[3]] + data[컬럼명[4]]
            elif len(컬럼명) == 6:
                data_[f'data[{컬럼명[0]}] + data[{컬럼명[1]}] + data[{컬럼명[2]}] + data[{컬럼명[3]}] + data[{컬럼명[4]}] + data[{컬럼명[5]}]'] = data[컬럼명[0]] + data[컬럼명[1]] + data[컬럼명[2]] + data[컬럼명[3]] + data[컬럼명[4]]  + data[컬럼명[5]]
            elif len(컬럼명) == 7:
                data_[f'data[{컬럼명[0]}] + data[{컬럼명[1]}] + data[{컬럼명[2]}] + data[{컬럼명[3]}] + data[{컬럼명[4]}] + data[{컬럼명[5]}] + data[{컬럼명[6]}]'] = data[컬럼명[0]] + data[컬럼명[1]] + data[컬럼명[2]] + data[컬럼명[3]] + data[컬럼명[4]] + data[컬럼명[5]] + data[컬럼명[6]]
            elif len(컬럼명) == 8:
                data_[f'data[{컬럼명[0]}] + data[{컬럼명[1]}] + data[{컬럼명[2]}] + data[{컬럼명[3]}] + data[{컬럼명[4]}] + data[{컬럼명[5]}] + data[{컬럼명[6]}] + data[{컬럼명[7]}]'] = data[컬럼명[0]] + data[컬럼명[1]] + data[컬럼명[2]] + data[컬럼명[3]] + data[컬럼명[4]] + data[컬럼명[5]] + data[컬럼명[6]] + data[컬럼명[7]]

    인덱스 = data_.columns

    for i in 인덱스:
        if len(data_[i]) == len(data_[i].value_counts()):
            유일성만족리스트.append(i)

    ## 수정된 코드
    for i in range(len(유일성만족리스트)):
        for j in range(i+1, len(유일성만족리스트)):
            if all(요소 in 유일성만족리스트[j].split(' + ') for 요소 in 유일성만족리스트[i].split(' + ')):
                유일성만족리스트[j] = '!'

    return len(유일성만족리스트) - 유일성만족리스트.count('!')