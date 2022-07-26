# React

- 프로젝트 생성

  `yarn create react-app [프로젝트 이름]`

- 서버 실행

  `yarn start`

- JSX 코드

```js
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
```

## 2. JSX

: jSX는 자바스크립트의 확장 문법

### 1. JSX의 장점

- 보기 쉽고 익숙하다.
- 더욱 높은 활용도
  - div, span같은 HTML 태그를 사용할 수 있다.



### 2. JSX의 문법

- 감싸인 요소 

  : 컴포넌트에 여러 요소가 있다면 반드시 부모 요소 하나로 감싸야 한다.

  ```js
  // h1, h2 태그를 div 태그로 감싸야 오류가 발생하지 않는다.
  function App() {
      return (
     <div>
      <h1>리액트 안녕!</h1>
      <h2>잘 작동하니?</h2>
     </div>
      
      )
  }
  export default App;
  ```


  여기서 div 요소를 사용하고 싶지 않을 때 Fragment 기능 사용

  ```js
  import { Fragment } from 'react';
  
  function App() {
    return (
      <Fragment>
        <h1> 리액트야 </h1>
        <h1>잘 작동하니</h1>
      </Fragment>
    );
  }
  
  export default App;
  
  // Fragment를 다음과 같이 사용 가능
      <>
        <h1>잘 작동하니
        </h1>
      </>
  ```

  

- if문 대신 조건부 연산자

  : JSX 내부의 자바스크립트 표현식에서 if 문을 사용할 수 없다.
  하지만 조건부 연산자 (삼항 연산자)를 사용하면 된다.

  ```js
  import { Fragment } from 'react';
  function App() {
    const name = '리액트';
  
    return (
      <div>
        {name === '리액트' ? (
          <h1>리액트입니다.
          </h1> ) : (
          <h2>리액트가 아닙니다</h2>
        )}
      </div>
    );
  }
  export default App;
  ```



- AND 연산자(&&)를 사용한 조건부 렌더링 (특정조건을 만족하는 경우 보여주고 싶다 라고 할 때)

  ```js
  function App() {
    const name = '리액트';
    return <div>{name === '리액트' && <h1>리액트입니다</h1>}</div>
  }
  
  export default App;
  ```
  
  
  
- undefined를 랜더링 하지 않기 

  ```js
  // 오류 발생, undefined만 return 불가능
  import './App.css';
  
  function App() {
      const name = undefined;
      return name;
  }
  
  // 옳게된 방식, ||(OR)을 이용하여 어떤 값이 undefined 일 때 사용할 값을 지정할 수 있다.
  function App() {
      const name = undefined;
      return name || '값이 undefiend입니다.';
  }
  
  // JSX 내부에서 undefiend를 렌더링하는 것은 괜찮다.
  return <div>{name || '리액트'}</div>;
  ```

  

- 인라인 스타일링

  : 리액트에서 DOM 요소에 **스타일을 적용**할 때는 문자열 형태로 넣는 것이 아니라 객체 형태로 넣어 주어야 한다. 

  `background-color` 가 아니라  카멜케이스 인 `backgroundColor`로 작성해야 한다.

  ```js
  function App() {
    const name = '리액트';
    const style = {
      backgroundColor: 'black',
      color: 'aqua'
    };
    
    return <div style={style}>{name}</div>;
  }
  
  export default App;
  
  // 바로 style값을 지정하고 싶다면 이렇게도 작성 가능
  function App() {
    const name = '리액트';
  
    return (
      <div style={{
        backgroundColor: 'black',
        color: 'aqua'
      }}>
        {name}
      </div>
    )
  }
  
  export default App;
  ```

  

- class 대신 className

  : JS와는 다르게 `class="myclass"` 가 아니라 `className`으로 작성해야 한다. 

  ```js
  import './App.css';
  
  function App() {
  	const name = "리액트";
  	return <div className="react">{name}</div>
  }
  export default App;
  ```

- 꼭 닫아야 하는 태그 
  : HTML의 경우 `<input>` 은 닫지 않아도 되지만 JSX 에서는 닫아야 한다 .
   태그 사이에 아무 내용도 들어가지 않는다면 `<input />` 로 작성한다.

   

- 주석

  `{/* */}` 으로 작성해야 한다.



[변수와 타입](react/00_변수와타입.md)



## 3. 컴포넌트

### 3.1. 클래스형 컴포넌트

- 함수 컴포넌트
  장점 : 선언하기가 훨씬 편하다. 메모리 자원도 클래스형보다 덜 사용
  단점 : state와 라이프사이클 API 사용이 불가능 하다.  

  ``` js
  import './App.css';
  
  fucntion App() {
      const name = '리액트';
      return <div className="react">{name}</div>
  }
  export default App;
  ```

- 클래스형 컴포넌트 

  ```js
  import { Component } from 'react';
  
  class App extends Component {
      render() {
          const name = 'react';
          return <div className="react">{name}</div>;
      }
  }
  
  export default App;
  ```

  : 클래스형 컴포넌트는 state 기능 및 라이프 사이클 기능을 사용할 수 있다.
   **render 함수는 필수**

### 3.2 첫 컴포넌트 생성 

- 컴포넌트 생성 순서

   `파일 만들기 → 코드 작성하기 → 모듈 내보내기 및 불러오기`  



// 싸트북으로 작성

### 3.3 props

- jsx 내부에서 props 랜더링

  ```react
  // App (부모 컴포넌트)
  import MyComponent from './MyComponent'
  
  const App = () => {
    return <MyComponent/>;
  };
  
  export default App;
  
  // Mycomponent
  const MyComponent = props => {
      return <div>안녕하세요, 제 이름은 {props.name} 입니다.</div>
  };
  
  MyComponent.defaultProps = {
      name : '기본 이름'
  };
  
  export default MyComponent;
  ```

  

- 태그 사이의 내용을 보여 주는 children

  ```react
  // App
  import MyComponent from './MyComponent'
  
  const App = () => {
    return <MyComponent>리액트</MyComponent>;
  };
  
  export default App;
  
  // Mycomponent
  const MyComponent = props => {
      return ( <div>
          안녕하세요, 제 이름은 {props.name} 입니다.<br/>
          children 값은 {props.children}.
          </div>
  )};
  
  MyComponent.defaultProps = {
      name : '기본 이름'
  };
  
  export default MyComponent;
  ```

  `props.children` 을 사용하면 App 컴포넌트의 내용을 MyComponent에서 보여 줄 수 있다.



- 비구조화 할당 문법을 통해 props 내부 값 추출
  비구조화 할당 문법: 객체에서 값을 추출하는 문법, 함수의 파라미터 부분에서도 사용할 수 잇다.

  ```react
  const MyComponent = props => {
      const {name, children} = props;
  
      return ( 
      <div>
          안녕하세요, 제 이름은 {name} 입니다.<br/>
          children 값은 {children}
          입니다.
      </div>
      );
  };
  
  MyComponent.defaultProps = {
      name : '기본 이름'
  };
  
  export default MyComponent;
  
  
  // 더 간단한 방법
  const MyComponent = ({name, children}) => {
  ...
  ```

  name 과 children을 할당해서 값을 추출한다.

​	

- propTypes를 통한 props 검증
  name 값은 무조건 string 형태로 전달하게 한다.

  ```react
  MyComponent.defaultProps = {
      name : '기본 이름'
  };
  
  MyComponent.propTypes = {
      name: PropTypes.string
  };
  ```



### 3.4  state

:  컴포넌트 내부에서 바뀔 수 있는 값
   props는 컴포넌트가 사용되는 과정에서 부모 컴포넌트가 설정하는 값이며, 읽기 전용 으로만 사용할 수 있다.

- 클래스형 컴포넌트의  state

```react
import { Component } from 'react';


class Counter extends Coponent {
    // state를 설정하기 위한 constructor 메서드를 작성
    constructor(props) {
        super(props); // 클래스형 컴포넌트에서 constructor를 작성할 때는 반드시 spuer 호출해야 함
        // state의 초깃값 설정하기
        this.state = { 	// 컴포넌트의 state는 객체 형식
            number = 0
        };
    }
    render() {
        const { number } = this.state; // state를 조회할 때는 this.state로 조회합니다.
        return (
        	<div>
            	<h1>{number}</h1>
            	<button
                    // onClick을 통해 버튼이 클릭되었을 때 호출할 함수를 지정합니다.
                    onClick={( =>
                             this.setState({ number: number + 1 });
                             )}
                 > 
                	+1 
                </button>
            </div>
        );
    }
}

export default Counter;
```



- this.setState에 객체 대신 함수 인자 전달하기 

  ```react
  onClick => {
      this.setState({ number : number + 1 });
      this.setState({ number : this.state.number + 1 });
  }
  ```

  이와 같이 작성하면 `this.setState`를 두 번 사용하는 것이지만 number는 +1 만 된다.
  `this.setState`를 사용한다고 해서 state 값이 바로 바뀌지는 않기 때문.
  이를 해결하기 위해 객체 대신 함수를 넣어준다.

  

  ```react
  onClick => {
  	this.setState(PrevState => {
          return {
              number: prevState.number + 1
          };
      )};
      // 위와 똑같은 코드, 함수에서 바로 객체를 반환한다는 의미              
      this.setState(prevState => ({
         number: prevState.number + 1
       }));
                    
  }
  ```

  ​    

- 함수 컴포넌트에서 useState 사용하기 
  : 구 버전에서는 함수 컴포넌트에서 state를 사용할 수 없었다. 
  함수 컴포넌트에서도 state를 사용하기 위해  useState를 사용한다.

  - 배열 비구조화 할당 
    : 배열 안에 들어 있는 값을 쉽게 추출할 수 있도록 해주는 문법.

    ```react
    const array = [1, 2];
    const one = array[0];
    const two = array[1];
    
    // 비구조화 할당
    const array = [1, 2];
    const [one, two] = array;
    ```

  - useState 사용하기 

    ```react
    import { useState } from 'react';
    
    const Say = () => {
    	const [message, setMessage] = useState('');
        const onClickEnter = () => setMessage('안녕하세요!');
        const onClickLeave = () => setMessage('안녕히 가세요!');
        
        return (
        	<div>
            	<button onClick={onClickEnter}>입장</button>
                <button onClick={onClickLeave}>퇴장</button>
                <h1>{message}</h1>
            </div>
        );
    };
    
    export default Say;
    ```

    useState 함수의 인자에는 상태의 초기값을 넣어 주며, 반드시 객체가 아니어도 된다.

    함수를 호출하면 배열이 되는데 
    첫번째 원소는 현재 상태 : ` message`
    두번째 원소는 상태를 바꾸어 주는 함수(Setter 함수) :  `setMessage`



## 4. 이벤트 핸들링

- 사용자가 웹 브라우저에서 DOM 요소들과 상호 작용하는 것을 이벤트 라고 한다.

### 4.1 리액트의 이벤트 시스템

event: 사용자가 웹에서 DOM 요소들과 상호 작용 하는 것

##### 4.1.1 주의 사항

1. 카멜 표기법
2. 이벤트 실행 시 함수 형태의 값 전달
3. DOM 요소에만 이벤트를 설정 가능



이벤트 연습

```react
import React, {Component} from 'react';

class EventPractice extends Component{
    render(){
        return (
            <div>
                <h1>이벤트 연습</h1>
                <input type='text' name='message' placeholder='아무거나 입력'
                    onChange={(e) => {console.log(e)}}/>
            </div>
        );
    }
}

export default EventPractice;
```

콘솔에 기록되는 e 객체는 SyntheticEvent로 웹브라우저의 네이티브 이벤트를 감싸는 객체이다.

비동기적으로 이벤트 객체를 참조할 일이 있다면 e.persist() 함수를 호출해야 한다.



render 안에 임의 메서드 만들기

```react
import React, {Component} from 'react';

class EventPractice extends Component{

    state = {
        message:""
    }
    render(){
        return (
            <div>
                <h1>이벤트 연습</h1>
                <input type='text' name='message' placeholder='아무거나 입력'
                       value={this.state.message}
                       onChange={(e) =>{this.setState({message: e.target.value})}}/>
                
                <button onClick={() => {alert(this.state.message);
                                        this.setState({message:''}); // message 공백으로 변환
                                       } 
                                }>확인</button>
            </div>
        );
    }
}

export default EventPractice;
```





4.2.3.2 Property Initializer Syntax를 사용한 메서드 작성

```react
import React, {Component} from 'react';

class EventPractice extends Component{

    state = {
        message:""
    }

    handleChange = (e) => {
        this.setState({
            message: e.target.value
        });
    }      
    
    handleClick = () => {
        alert(this.state.message);
        this.setState({
            message: ""
        });
    }

    render(){
        return (
            <div>
                <h1>이벤트 연습</h1>
                <input type='text' name='message' placeholder='아무거나 입력'
                       value={this.state.message}
                       onChange={this.handleChange}
                        />
                        
                {/*e.tartgetl.value : 입력 시 변하는 하나하나의 값 
                   this.state.message : 완전히 변한 값?
                */}
                <button onClick={this.handleClick}>확인</button>
            </div>
        );
    }
}

export default EventPractice;
```



##### 4.2.4 input 여러 개 다루기

input이 여러 개일 때는 event 객체를 활용하는 것이다.

```react
import React, {Component} from 'react';

class EventPractice extends Component{
	
    //state 설정
    state = {
        username: '',
        message:''
    }
	// input에 일어난 일을 알아야 하므로 event를 매개변수로 보낸다. state를 input에 쓴 name과 value로 set한다.
    handleChange = (e) => {
        this.setState({
           [e.target.name]: e.target.value
        });
    }      
    // 클릭이 일어나면 alert로 state에 저장된 username과 message를 출력 후 빈 문자로 초기화 한다.
    handleClick = () => {
        alert(this.state.username + ':' + this.state.message);
        this.setState({
            username:"",
            message: ""
        });
    }


    render(){
        return (
            <div>
                <h1>이벤트 연습</h1>
                <input type='text' name='username' placeholder='사용자 명'
                       value={this.state.username}
                       onChange={this.handleChange}
                        />

                <input type="text" name="message" placeholder='아무거나 입력' value={this.state.message} onChange={this.handleChange}></input>
                <button onClick={this.handleClick}>확인</button>
            </div>
        );
    }
}

export default EventPractice;
```

: 객체 안에서 key를 []로 감싸면 그 안에 넣은 래퍼런스가 가리키는 실제 값이 key 값으로 사용된다.
따라서 `e.target.name`이 key가 된다.



##### 4.2.5 onKeyPress 이벤트 핸들링

```react
import React, {Component} from 'react';

class EventPractice extends Component{

    state = {
        username: '',
        message:''
    }

    handleChange = (e) => {
        this.setState({
           [e.target.name]: e.target.value
        });
    }      
    
    handleClick = () => {
        alert(this.state.username + ':' + this.state.message);
        this.setState({
            username:"",
            message: ""
        });
    }
	// 추가사항, enter라는 event가 일어나면 handleClick을 실행한다.
    handleKeyPress = (e) => {
        if(e.key === 'Enter') {
            this.handleClick();
        }
    }

    render(){
        return (
            <div>
                <h1>이벤트 연습</h1>
                <input type='text' name='username' placeholder='사용자 명'
                       value={this.state.username}
                       onChange={this.handleChange}
                       
                        />

                <input type="text" name="message" placeholder='아무거나 입력' 
                       value={this.state.message} onChange={this.handleChange} 
                       onKeyPress={this.handleKeyPress} ></input>
                       
                <button onClick={this.handleClick} >확인</button>
            </div>
        );
    }
}

export default EventPractice;
```



함수 컴포넌트로 구성

```react
import React, {useState} from 'react';

const EventPractice = () => {
    const [username, setUsername] = useState('');
    const [message, setMessage] = useState('');
    const onChangeUsername = e => setUsername(e.target.value);
    const onChangeMessage = e => setMessage(e.target.value);
    
    const onClick = () => {
        alert(username + ':' + message);
        setUsername('');
        setMessage('');

    };
    
    const onKeyPress = e => {
        if(e.key === 'Enter'){
            onClick();
        }
    };

    return (
        <div>
            <h1>이벤트 연습</h1>
            <input type="text" name="username" placeholder={"사용자명"} value={username} onChange={onChangeUsername}></input>
            <input type="text" name="usermessage" placeholder={"아무말이나 하셈"} value={message} onChange={onChangeMessage} onKeyPress={onKeyPress}></input>
            <button onClick={onClick}>확인</button>
        </div>
    );
};

export default EventPractice 
```





```react
import React, {useState} from 'react';

const EventPractice = () => {
    const [form, setForm] = useState({
        username:'',
        message: ''
    });

    const {username, message} = form;
    
    const onChange = e => {
        const nextForm = {
            ...form, // 이전 form 복사
            [e.target.name] : e.target.value
        };
        setForm(nextForm);
    };
    
    const onClick = () => {
        alert(username + ':' + message);
        setForm({
            username:'',
            message:''
        });    
    }
   
    const onKeyPress = e => {
        if(e.key === 'Enter'){
            onClick();
        }
    };

    return (
        <div>
            <h1>이벤트 연습</h1>
            <input type="text" name="username" placeholder="사용자명" value={username} onChange={onChange}></input>
            <input type="text" name="message" placeholder="아무말이나 적으세여" value={message} onChange={onChange} onKeyPress={onKeyPress}></input>
            <button onClick={onClick}>확인</button>
            
        </div>
    );
};

export default EventPractice 
```



## 5. ref:DOM에 이름달기

### 5.1 ref를 어떤 상황에서 사용해야 할까?

: DOM을 꼭 직접적으로 건드려야 할 때
id 같은 존재...



##### 5.1.1 예제 생성

```react
import {Component} from 'react';
import './ValidationSample.css'

class ValidationSample extends Component {
    state = {
        password:'',
        clicked: false,
        validated: false
    }
	
    // input에 변화가 일어나면 변화에 따라 password를 업데이트 한다.
    handleChange = (e) => {
        this.setState({
            password: e.target.value
        });
    }
	
    // 버튼 클릭이 일어나면, clicked를 true로 바꾸고, ㄱ머증 비밀번호
    handleButtonClick = () => {
        this.setState({
            clicked: true,
            validated: this.state.password === '0000'
        })
    }
    
    render(){
        return(
            <div>
                <input type="password" value={this.state.password} onChange={this.handleChange}
                       className={this.state.clicked ? (this.state.validated ? 'success' : 'failure') : ''} ></input>
                <button onClick={this.handleButtonClick}>검증하기</button>
            </div>
        );
    }
}

export default ValidationSample
```



### 5.2 ref 사용

##### 5.2.1 콜백 함수를 통한 ref 설정

ref를 만드는 가장 기본적인 방법은 콜백 함수를 사용하는 것이다.
ref를 달고자 하는 요소에 ref라는 콜백 함수를 props로 전달해 주면 된다.
이 콜백함수는 ref 값을 파라미터로 전달 받는다. 

```react
<input ref={ref} => {this.input=ref}/>
```

##### 5.2.2 createRef를 통한 ref 설정

```react
import React, {Component } from 'react';

class RefSample extends Component {
    input = React.createRef();

    handleFocus = () => {
        this.input.current.focus(); // ref를 설정해 준 DOM에 접근하려면 												   this.input.current를 조회 하면 된다.
    }

    render() {
        return (
            <div>
                <input ref={this.input}></input>
            </div>
        );
    }
}

export default RefSample;
```



### 5.3 컴포넌트에 ref 달기

: 컴포넌트 내부에 있는 DOM을 컴포넌트 외부에서 사용할 때 쓴다. 

##### 5.3.1 사용법

```react
<MyComponent ref={(ref) => {this.MyComponent=ref}}
```

이렇게 하면 MyComponent 내부의 메서드 및 멤버 변수에도 접근 가능 
(ex. myComponent.handleClick, myComponent.input)



##### 5.3.4 컴포넌트에 ref 달고 내부 메서드 사용

```react
// ScrollBox
import { Component } from "react";

class ScrollBox extends Component {

    scrollToBottom = () => {
        const { scrollHeight, clientHeight } = this.box;
        this.box.scrollTop = scrollHeight - clientHeight;
    }

    render() {
        const style = {
            border: '1px solid black',
            height: '300px',
            width: '300px',
            overflow: 'auto',
            position: 'relative',
        };
        
        const innerStyle = {
            width: '100%',
            height: '650px',
            background: 'linear-gradient(white, black)'
        }

       
        return (
            <div style={style} ref={(ref) => {this.box=ref}}>
                <div style={innerStyle}></div>

            </div>
        );
    }
    
}

export default ScrollBox;

// App.js
import ScrollBox from './ScrollBox';
import { Component } from 'react';

class App extends Component {
  render() {
    
    return (
      <div>
        <ScrollBox ref={(ref) => this.scrollBox=ref}/>
        <button onClick={() => this.scrollBox.scrollToBottom()}>맨밑으로</button>
        
      </div>
    );
  }
}

export default App;
```



### 5.4

컴포넌트 내부에서 DOM에 직접 접근해야 할 때는 ref를 사용해야 한다.
ref를 사용하기 전에 원하는 기능을 구현할 수 있는지 고려한 후 사용해야 한다.



## 6. 컴포넌트 반복

### 6.1 자바스크립트 배열의 map() 함수 

: 반복되는 컴포넌트를 랜더링 할 수 있다. 

```react
const numbers = [1,2,3,4,5];
const result = numbers.map(num => num * num);

console.log(result) // 1 4 9 16 25
```

이처럼 기존 배열로 새로운 배열을 만드는 역할을 한다.



##### 6.1.1 문법

`arr.map(callback, [thisArg])`

- callback : 새로운 배열의 요소를 생성하는 함수로 파라미터는 다음 세가지
  - currentValue: 현재 처리하고 있는요소
  - index: 현재 처리하고 있는 요소의 index 값
  - array: 현재 처리하고 있는 원본 배열
- thisArg(선택) : callback 함수 내부에서 사용할 this 래퍼런스



### 6.2 데이터 배열을 컴포넌트 배열로 변환

##### 6.2.1 컴포넌트 생성

```react
const IterationSample = () => {
    const names = ['눈사람', '얼음', '눈', '바람'];
    const nameList = names.map(name => <li>{name}</li>);
    return <ul>{nameList}</ul>;

};

export default IterationSample;
```

이 코드는 key prop이 없기 때문에 불안정하다.



### 6.3 key (** 중요**)

: 컴포넌트 배열을 랜더링 했을 때 어떤 원소에 변동이 있었는지 알아내기위해 사용한다.

key 값은 언제나 유일 해야 한다. (반복되는 데이터를 랜더링 할 때는) 

```react
const articleList = articles.map(article => (
	<Article title={article.title} writer={article.writer} key={article.id}/> 
));
```

고유 번호가 없다면 index 번호를 사용한다.

```react
const IterationSample = () => {
    const names = ['눈사람', '얼음', '눈', '바람'];
    const nameList = names.map((name, index) => <li key={index}>{name}</li>);
    return <ul>{nameList}</ul>;

};

export default IterationSample;
```



### 6.4 응용, 유동적인 데이터 렌더링

```react
const IterationSample = () => {
    
    const [names, setNames] = useState([
        {id:1 , text: '눈사람'},
        {id:2 , text; '얼음'},
        {id:3 , text; '눈'},
        {id:4 , text; '바람'},
    ]);
    
    const [InputText, setInputText] = useState('');
    const [nextId, setNextId] = useState(5); // 새로운 항목을 추가할 때 사용할 id
    
    const nameList = names.map(name => <li key={name.id}>{name.text}</li>);
    return <ul>{nameList}</ul>;

};

export default IterationSample;
```



배열에 새 항목을 추가할 때 concat을 사용한다. 
push는 기존 배열 자체를 변경, concat은 새로운 배열을 만들어 준다.

```react
const IterationSample = () => {
    
    const [names, setNames] = useState([
        {id:1 , text: '눈사람'},
        {id:2 , text; '얼음'},
        {id:3 , text; '눈'},
        {id:4 , text; '바람'},
    ]);
    
    const [InputText, setInputText] = useState('');
    const [nextId, setNextId] = useState(5); // 새로운 항목을 추가할 때 사용할 id
    
    // 새로운 항목이 추가되었을 때
    const onChange = e => setInputText(e.tartget.value);
    cosnt onClick = () => {
        const nextNames = names.concat({
            id: nextId,
            text: inputText
        });
        setNextId(nextId + 1); // id+1 해주고
        setNames(nextNames); // 내용 업데이트 해주고
        setInputText(''); // 초기화 시킨다.
    }
    const nameList = names.map(name => <li key={name.id}>{name.text}</li>);
    return(
        <>
        <input value={InputText} onChange={onChange}></input>
        <button>추가</button>
        <ul>{nameList}</ul>
        </>
    )

};

export default IterationSample;
```





### 6.4.3 데이터 제거 기능 구현

불변성을 유지하면서 배열의 특정 항목을 지울 때는 배열의 내장 함수 filter를 사용한다.

```react
//예시
const numbers = [1, 2, 3, 4, 5, 6];
const biggerThanThree = numbers.filter(number => number > 3);
```



- IterationSample.js

```react
const IterationSample = () => {
    
    const [names, setNames] = useState([
        {id:1 , text: '눈사람'},
        {id:2 , text; '얼음'},
        {id:3 , text; '눈'},
        {id:4 , text; '바람'},
    ]);
    
    const [InputText, setInputText] = useState('');
    const [nextId, setNextId] = useState(5); // 새로운 항목을 추가할 때 사용할 id
    
    // 새로운 항목이 추가되었을 때
    const onChange = e => setInputText(e.tartget.value);
    cosnt onClick = () => {
        const nextNames = names.concat({
            id: nextId,
            text: inputText
        });
        setNextId(nextId + 1); // id+1 해주고
        setNames(nextNames); // 내용 업데이트 해주고
        setInputText(''); // 초기화 시킨다.
    };
    
    const onRemove = id => {
        const nextNames = names.filter(name => name.id !== id );
        setNames(nextNames);
  }
    const nameList = names.map(name => <li key={name.id} onDoubleClick={() => onRemove(name.id)}>{name.text}</li>);
    return <ul>{nameList}</ul>;

};

export default IterationSample;
```



## 7 컴포넌트의 라이프사이클 메서드

: 모든 리액트 컴포넌.트의 라이프 사이클은 **[페이지 랜더링 되기 전 준비과정 ~ 페이지에서 사라질 때]** 
  **클래스형 컴포넌트**에서 사용이 가능하며 함수 컴포넌트는 Hooks로 비슷한 작업 처리 가능

### 7.1 라이프사이클 메서드의 이해

- 메서드의 종류는 9가지

   WILL- :어떤 작업을 작동하기 전에 실행되는 메서드 

   Did- : 작동 후에 실행 되는 메서드

- 3가지 카테고리로 나뉨
  - 마운트 
  - 업데이트
  - 언마운트



- 마운트

  DOM이 생성되고 웹 브라우저상에 나타나는 것을 마운트라고 한다.

  - 마운트 할 때 호출되는 메서드

    ```
    컴포넌트 만들기 -> constructor -> getDerivedStateFromProps -> render -> componentDidMount
    ```

    - constructor

      : 컴포넌트를 새로 만들 때마다 호출되는 클래스 생성자 메서드

    - getDerivedStateFromProps

      : props에 있는 값을 state에 넣을 때 사용하는 메서드

    - render

      : 우리가 준비한 UI를 랜더링하는 메서드

    - componentDidMount

      : 컴포넌트가 웹 브라우저상에 나타난 후 호출하는 메서드

      

- 업데이트

  : 컴포넌트는 다음과 같은 총 네가지 경우에 업데이트 한다.

  1. (컴포넌트에 전달하는) props가 바뀔 때 
  2. (컴포넌트 자신이 들고있는) state가 바뀔 때
  3. 부모 컴포넌트가 리젠더링 될 때
  4. this.forceUpdate로 강제로 랜더링을 트리거 할 때

  - 업데이트할 때 호출하는 메서드

  ```
  업데이트를 발생시키는 요인 -> getDerivedStateFromProps -> shouldCoponentUpdate -> render -> getSnapshotBeforeUpdate -> coponentDidUpdate
  ```

  - getDerivedStateFromProps

    : 이 메서드는 마운트 과정에서 호출된다. props의 변화에 따라 state 값에도 변화를 주고 싶을 때 사용한다.

  - shouldCoponentUpdate

    : 리젠더링을 할지 말지 결정하는 메서드, true면 리 젠더링, false면 작업 중지. forceUpdate() 함수를 호출하면 바로 render 함수 호출

  - render

    : 컴포넌트를 리젠더링

  - getSnapshotBeforeUpdate

    : 컴포넌트 변화를 DOM에 반영하기 바로 직전에 호출하는 메서드

  - componentDidupdate

    : 컴포넌트의 업데이트 작업이 끝난 후 호출하는 메서드

- 언마운트

  : `componentWillUnmount` , 컴포넌트를 DOM에서 제거하는 것



### 7.2 라이프사이클 메서드 살펴보기

___

- render

  - 유일한 필수 메서드
  - 이 메서드 안에서 `this.props` ,`this.state`에 접근할 수 있으며 리액트 요소를 반환

  :warning:주의

  ```
  이벤트 설정이 아닌 곳에서 setState 사용 금지
  브라우저의 DOM에 접근 금지 
  
  DOM에서 정보를 가져오거나 state에 변화를 줄 땐 componentDidMount에서 처리
  ```

- constructor 메서드

  `constructor(prpos) {...}`

  - 컴포넌트의 생성자 메서드로 컴포넌트를 만들 때 처음 사용.
    이곳에서 초기 state 정할 수 있음

- getDerivedStateFromPorps 메서드

  - props로 받아 온 값을 state에 동기화 시키는 용도
    컴포넌트가 마운트, 업데이트될 때 호출

  ```react
  static getDerivedStateFromProps(nextProps, prevState) {
      if(nextProps.value !== prevState.value) { // 조건에 따라 특정 값 동기화
          return {value: nextProps.value}; 
      }
  	return null; // state를 변경할 필요 없다면 null 반환
  }
  ```

- componentDidMount 메서드

  - 컴포넌트를 만들고 첫 렌더링을 다 마친 후 실행
  - 이 안에서 JS 라이브러리, 프레임워크 함수 호출, 이벤트등록, setTimeout, setInterval, 네트워크 요청 같은 비동기 작업 처리 

- shouldComponentUpdate 메서드

  `shouldComponentUpdate(nextProps, nextState) {...}`

  - props, state를 변경했을 때, 리젠더링을 시작할지 여부를 지정하는 메서드.
  - 따로 생성하지 않으며 언제나 true 값을 반환.
  - 이 안에서 현재 props와 state는 this. 으로 접근, 새로 설정될 때 next. 로 접근 가능

- getSnapshotBeforeUpdate 메서드

  - render에서 만들어진 결과물이 브라우저에 실제로 반영되기 직전에 호출

  - componentDidMount 에서 세 번째 파라미터인 snapshot 값으로 전달 받을 수 있다.

  - 업데이트 하기 직전 값을 참고할 일이 있을 때 활용 (예: 스크롤바 위치 유지)

    ```react
    getSnapshotBeforeUpdate (prevProps, prevState) {
        if(prevState.array !== this.state.array) {
            const {scrollTop, scrollHeight} = this.list
            return { scrollTop, scrollHeight };
        }
    }
    ```

- componentDidUpdate 메서드 

  `componentdidUpdate(prevProps, prevState, snapshot) {...}`

  - 리랜더링 완료 후 실행
  - 업데이트가 끝난 직후라 DOM관련 처리 가능
  - prevProps, prevState를 사용하여 컴포넌트가 이전에 가졌던 데이터에 접근 가능

  

-  componentWillUnmout 메서드

  - 컴포넌트를 DOM에서 제거할 때 실행
  - componentDidMount에서 등록한 이벤트, 타이머, 직접 생성한 DOM이 있다면 여기서 제거 해야 함

- componentDidCatch 메서드

  - 렌더링 도중 에러 발생했을 때, 애플리케이션 먹통 없이 오류 UI를 보여줄 수 있다. 

    ```react
    componentDidCatch(error, info){
        this.setState({
            error: true
        });
    	console.log({error, info});
    }
    // error: 에러 종류, info: 코도의 위치
    ```

  - 컴포넌트 자신에게 발생하는 에러는 못잡음.
    자신의 this.props.children으로 전달되는 컴포넌트에서 발생하는 에러만 가능





## 8.  Hooks

: useState는 함수 컴포넌트에서도 가변적인 상태를 지닐 수 있게 해준다.

 `const [value, setValue] = useState(0)`
: useState 함수의 파라미터에는 상태의 기본값을 넣어준다.
  이 함수가 호출되면 배열을 반환하는데, 그 배열의 첫 번째 원소는 상태 값, 두 번째 원소는 상태를 설정하는 함수.



#### 8.1.1 useState를 여러번 사용하기 

: 하나의 useState함수는 하나의 상태 값만 관리할 수 있다.
 여러번 사용 하면 된다. 

```react
const [name, setName] = useState('');
const [nickname, setNickname] = useState('');
```



### 8.2 useEffect

: 컴포넌트가 랜더링될 때 마다 특정 작업을 수행하도록 설정할 수 있는 Hook

````react
useEffect(() => {
        console.log('랜더링이 완료되었다.');
        console.log({
            name,
            nickname
        });
    });
````

 

#### 8.2.2 특정 값이 업데이트 될 때만 실행하고 싶을 때 

useEffect를 사용할 때, 

```react
componentDidupdate(prevProps, prevState) {
    if (prevProps.value !== this.props.value ){
        doSomething();
    }
}
```

이 코드는 props 안에 들어 있는 value 값이 바뀔 때만 특정 작업을 수행한다.
이러한 작업을 useEffect에서 하려면 배열안에 검사하고 싶은 값을 넣어주면 된다.

```react
useEffect(() => {
	console.log(name);
}, [name]);

// 이러면 console창에서 name만 뽑아서 확인할 수 있다.
```

배열 안에는 useState를 통해 관리하고 있는 상태, props로 전달받은 값을 넣어 줘도 된다.



#### 8.2.3 뒷정리하기 

useEffect는 렌더링되고 난 직후마다 실행되며, 두 번째 파라미터 배열에 무엇을 넣는지에 따라 실행 조건이 달라진다. 

```react
useEffect (()=> {
    console.log('effect');
    console.log(name);
    return() => {
        console.log('cleanup');
        console.log(name);
    };
}, [name]);
```



### 8.3 useReducer

: useState보다 더 다양한 컴포넌트 상황에 따라 다양한 상태를 다른 값으로 업데이트 해 주고 싶을 때 사용

```react
import { useReducer} from 'react';

function reducer(state, action) {
    // action.type에 따라 다른 작업 수행
    switch (action.type) {
        case 'INCREMENT':
            return { value: state.value + 1};
        case 'DECREMENT':
            return { value: state.value - 1};
        default:
            // 아무것도 해당되지 않을 대 기존 상태 변환
            return state;
    }
}

const Counter = () => {
    const [state, dispatch] = useReducer(reducer, {value: 0});

    return (
        <div>
            <p>
                현재 카운터 값은 <b>{state.value}</b>
            </p>
            <button onClick={() => dispatch({type: 'INCREMENT'})}>+1</button>
            <button onClick={() => dispatch({type: 'DECREMENT'})}>-1</button>
        </div>
    )
}

export default Counter;
```



- useReducer의 
  첫번째 파라미터 (reducer 함수)
  두번째 파라미터 (해당 리듀서의 기본 값)

- 이 Hook을 사용하면 state(현재 가리키고 있는 상태)값과 dispatch(액션을 발생시키는 ) 함수를 받아온다. 



#### 8.3.2 인풋 상태 관리





### 8.4 useMemo

: 함수 컴포넌트 내부에서 발생하는 연산을 최적화할 수 있다.
  

### 8.5 useCallback





## 9. 컴포넌트 스타일링

### 9,1 CSS

: CSS작성 시 중요한 점은 클래스를 중복되지 않게 만드는 것.
 특별한 규칙을 만들거나, CSS Selector를 사용한다.

#### 9.1.1 이름 짓는 규칙

: 컴포넌트 이름-클래스 형태로 짓는다.  (App-header).



#### 9.1.2 CSS Selector

```react
.App .logo {...} // .App 안에 있는 logo를 선택할 때
```



### 9.2 Sass 사용하기



