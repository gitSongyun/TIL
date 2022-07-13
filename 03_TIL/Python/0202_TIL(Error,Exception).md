# 0202 TIL (에러와 예외)

### Syntax Error (문법 에러)

- EOL (End of Line)
- EOF (End of File)

### Error 종류

1. ZeroDivisionError : 0으로 나누고자 할 때 발생
2. NameError : namespace 상에 이름이 없는 경우

3. TypeError 

```python
# Type 불일치
1+'1'
round('3.5')

#argument 누락 및 개수 초과
divmod() , divmod(1,2,3)
import random
random.sample()
```

4. ValueError

```python
#타입은 올바르나 값이 적절하지 않거나 없는 경우
int('3,5')
range(3).index(6)
```

5. IndexError : 인덱스가 존재하지 않거나 범위를 벗어나는 경우

```python
empty_list = []
empty_list[2]
```

6. KeyError : 해당 키가 존재하지 않는 경우
7. ModuleNotFoundError : 존재하지 않는 모듈을 import 하는 경우 
8. ImprotError - Module은 있으나 존재하지 않는 클래스/함수를 가져오는 경우 

```python
# 오류
from random import sampl

# 정상
from random import sample
sample(range(3), 1) # [1,2,3] 3개의 sample 중 1개 뽑기
```

9. IndentationalError - 들여쓰기 에러



### Exception (예외)

- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤

- 예외는 여러 type으로 나타나고, type이 메시지의 일부로 출력됨
- 모든 내장 예외는 Exception Class를 상속받아 이뤄짐



#### - 예외처리

try 문 / except 절을 이용하여 예외 처리 가능

-  try문
  - 오류가 발생할 가능성이 있는 코드를 실행
  - 예외가 발생되지 않으면, except 없이 실행 종료 

- except 문
  - 예외가 발생하면 except 절이 실행
  - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함.

```python
try:
    numbers = [1,2,3]
    number = numbers[4] # 없는 index이므로 IndexError 발생
except IndexError:
    print('오류 발생')
else: # Error가 발생하지 않은 경우 수행되는 문장
    print(number*100)
```



- finally 
  - 반드시 수행해야 하는 문장은 `finally`를 활용
  - 즉, 모든 상황에 실행되어야만 하는 코드를 정의하는데 활용
  - 예외의 발생 여부와 관계없이 `try`문을 떠날 때 항상 실행

```python
try:
    print('성적 파일을 읽어옵니다.')
    data = {'python': 'A+'}
    data['java']
except KeyError as err:
    print(f'{err}는 딕셔너리에 없는 키입니다.')
finally:
    print('성적 파일을 종료합니다.')
```



#### - 에러 메시지 처리

```python
try:
    empty_list = []
    print(empty_list[-1])
except IndexError as IdxErr:
    print(f'{IdxErr} 발생') # => list index out of range 발생
```



#### - 예외 발생 시키기(`raise`)

```python
raise ValueError('hi')
```

