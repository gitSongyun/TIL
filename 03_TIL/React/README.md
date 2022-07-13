# React

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

## JSX

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

  

[변수와 타입](react/00_변수와타입.md)