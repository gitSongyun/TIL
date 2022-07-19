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
        <h1>잘 작동하니
        </h1>
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



- AND 연산자(&&)를 사용한 조건부 렌더링

  ```js
  function App() {
    const name = '리액트';
    
    return <div>{name === '리액트' && <h1>리액트입니다</h1>}</div>
  }
  
  export default App;
  ```

  

- undefined를 랜더링 하지 않기 

  ```js
  // 오류 발생
  import './App.css';
  
  function App() {
      const name = undefined;
      return name;
  }
  
  // 옳게된 방식
  function App() {
      const name = undefined;
      return name || '값이 undefiend입니다.';
  }
  
  // JSX 내부에서 undefiend를 렌더링하는 것은 괜찮다.
  return <div>{name || '리액트'}</div>;
  ```

  

- 인라인 스타일링

  : 리액트에서 DOM 요소에 스타일을 적용할 때는 문자열 형태로 넣는 것이 아니라 객체 형태로 넣어 주어야 한다. 

  `background-color` 이 아니라  카멜케이스 인 `backgroundColor`로 작성해야 한다.

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

  :JS와는 다르게 `class="myclass"` 가 아니라 `className`으로 작성해야 한다. 

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
   props는 컴포넌트가 사용되는 과정에서 부모 컴포넌트가 설정하는 값이며, 읽기 전용으     	로만 사용할 수 있다.

- 클래스형 컴포넌트의  state
