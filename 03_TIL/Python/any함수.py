def my_any(elements):
    
    for element in elements:
        if element == []:
            continue
        elif bool(element) == True:
                return True
        else:
            return False
    return False # 공백은 for 안에 들어가지 못하므로 for문 밖에 return 값을 설정 해준다. 

    
print(my_any([1, 2, 5, '6']))
print(my_any([[], 2, 5, '6']))
print(my_any([]))
print(any([1, 2, 5, '6']), any([[], 2, 5, '6']), any([0]))