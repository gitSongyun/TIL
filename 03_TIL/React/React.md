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

ref를 만드는 가장 기본적인 방법은 콜백 함수를 사용하는 것
