# 0205 TIL (HTML,CSS)

## HTML 기본 구조 

- html: 문서의 최상위 요소
- head: 문서 메타데이터 요소 
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- body: 문서 본문 요소
  - 실제 화면 구성과 관련된 내용



## head 예시

- `<title>`:브라우저 상단 타이틀
- `<meta>`: 문서 레벨 메타데이터 요소 
- `<link>`: 외부 리소스 연결 요소(CSS 파일, favicon 등)
- `<script>`: 스크립트 요소 (JavaScript)



## 요소(element)

- HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
  - 태그(Element, 요소)는 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
- 내용이 없는 태그들
  - br, hr, img, input, link, meta 
- 요소는 중첩(nested)될 수 있음



## 시맨틱 태그 

- Non semantic 요소는 div, span 등이 있으며 h1, table 태그들도 시맨틱 태그 
- 의미 있는 정보의 그룹을 태그로 표현 



## form

- `<form>`은 정보(데이터)를 서버에 제출하기 위한 영역
- `<form>`기본 속성
  - action : form을 처리할 서버의 URL
  - method : form을 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)
  - enctype : method가 post인 경우 데이터의 유형



## input

- 다양한 타입을 가지는 입력 데이터 유형과 위젯 제공
- `<input>` 대표적인 속성
  - name : form control에 적용되는 이름 
  - value : form control에 적용되는 값
  - required, readonly, autofocus, autocomplete, disabled



clearfix :: after 다시 보기 

class에 속성을 부여할 때 부모에게 한번에 부여할지, 각 자식에게 속성을 각각 똑같이 부여할지 고민될때는 어떻게 해야하나요? 결과가 가끔 다르게 나올때가 있어서요 ㅠㅠ

___



# 0207

## 강의중

CSS Flexible Box Layout

1차원 레이아웃 모델 

축과 구성요소 별표 



flex-direction : row

Flex container (부모요소)를 쓸 때는 display: flex를 써야 함. 



# Bootstrap

스크립트 파일은 일반적으로body 닫는 태그 위에



### **CDN**

### 

## spacing

- mt-1 (margin top), (0.25rem = 4px)

```html
.mt{
margin-top: 0.25rem !important;
}
 # improtant는 덮어씌워지는걸 방지하기 위해
```

- mx-0 (margin x축)

```html
.mx-0 {
margin-right:0
margin-left:0
}
```

- py-0 () (padding)

```

```





