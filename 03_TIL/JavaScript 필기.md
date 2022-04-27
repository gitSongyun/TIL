# JavaScript

## 1. 데이터 타입		

### - 원시 타입 

-  객체가 아닌 기본 타입 
- 변수에 해당 타입의 값이 담김
- 다른 변수에 복사할 때 실제 값이 복사됨 

### - 참조 타입 

- 객체 타입의 자료형 
- 변수에 해당 객체의 참조 값이 담김 
- 다른 변수에 복사할 때 참조 값이 복사됨

```javascript
# 1. let
let message = '안녕하세요'

let greeting = message
console.log(greeting)
>>> 안녕하세요 

message = 'Hello World'
console.log(greeting)
>>> 안녕하세요 


# 2. const
const message = ['안녕하세요']

const greeting = message
console.log(gretting)
>>> ['안녕하세요']

message[0] = 'Hello world'
console.log(greeting)
>>> ['Heelo world']
```



- undefined
  - 변수의 값이 없음을 나타내는 데이터 타입 
  - 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined가 할당됨

- null

  - 변수의 값이 없음을 의도적으로 표현할 때 
  - `typeof null` 의 결과는 `object` 이다. 

  

## 2. 삼항 연산자

- 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자 
- 가장 왼쪽의 조건식이 <span style='color:blue'>참</span>이면 <span style='color:blue'>콜론 앞의 값</span> 을 사용하고 <span style='color:red'>거짓</span> 이면 <span style='color:red'>콜론 뒤의 값</span>을 사용

```javascript
console.log(true ? 1 : 2)  // 1
console.log(false ? 1 : 2) // 2
```





## 3. 조건문의 종류와 특징

- ### 'if' statement

​		조건 표현식의 결과 값을 Boolean 타입으로 변환 후 참/거짓을 판단   

```javascript
const nation = 'Korea'

if (nation === 'Korea') {
  cosole.log('안녕하세요')
} else if (nation === 'France') {
  console.log('Bongour')
} else {
  console.log('Hello')
}
```



- ### 'switch' statement

  조건 표현식의 결과값이 어느 값(case)에 해당하는지 판별 

  break 안쓰면 사고남 (True 인 케이스 밑으로 다 출력됨)

```javascript
const nation = 'Korea'

switch(nation) {
    case 'Korea': {
        console.log('안녕하세요')
    	break
    }
    case 'France': {
        console.log('Bonjour')
        break
    }
    default: {
        console.log('Hello')
    }
}
```



## 4. 반복문

### 종류 

- while

```javascript
let i = 0
while (i < 6) {
    console.log(i) // 0, 1, 2, 3, 4, 5 
    i += 1
}
```

- for

```javascript
for (let i = 0; i < 6; i++) {
    console.log(i) // 0, 1, ~
}
```

- for ... in (객체 순회)

  : 주로 객체의 속성들을 순회 할 때 사용 

    배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장 X

```javascript
const capitals = {
    korea: 'seoul',
    france: 'paris',
    USA: 'washington D.C.'
}

for (let capital in capitas) {
    console.log(capital) // korea, france, USA
}
```

- for ... of (배열 순회)

  : 반복 가능한 객체를 순회하며 값을 꺼낼 때 사용 (Array, Map, Set, String)

```javascript
const fruits = ['딸기', '바나나', '메론']

for (let friut of fruits) {
    fruit = fruit + '!'
    console.log(fruit)
}

for (const fruit of fruits) {
    console.log(fruit)
}
```

![image-20220425230451051](JavaScript 필기.assets/image-20220425230451051.png)



## 5. 함수 

:  JavaScript에서 함수를 정의하는 방법 2가지 

- 함수 선언식 
  - hoisting 발생
- 함수 표현식
  - hoisting 발생 하지 않는다. 

```javascript
// 함수 선언식
function sub(args) { }

// hoisting이 발생한다. 
add(2, 7) // 9
function add (num1, num2) {
    return num1 + num2
}

// 함수 표현식
const add = function (args) { }
```



### 참고

- JS의 함수는 일급객체에 해당
  - 일급객체: 다음의 조건들을 만족하는 객체를 의미 
    - 변수에 할당 가능
    - 함수의 매개변수로 전달 가능
    - 함수의 반환 값으로 사용 가능

```javascript
function add(num1, num2) {
	return num1 + num2
}

add(1, 2)
```



> 매개변수와 인자의 개수 불일치 허용

```javascript
// 매개변수보다 인자의 개수가 많을 경우 
const noArgs = function() {
    return 0
}

noArgs(1, 2, 3) // 0

const twoArgs = function (arg1, arg2) {
    return [arg1, arg2]
}

twoArgs(1, 2, 3) // [1, 2]


// 매개변수보다 인자의 개수가 적을 경우 
const threeArgs = funciton (arg1, arg2, arg3) {
    return [arg1, arg2, arg3]
}

threeArgs(1) // [1, undefined, undefined]
```





