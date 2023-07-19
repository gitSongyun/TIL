/**
 * 문제 링크 : https://codingdojang.com/scode/445
 * s1의 문자 하나를 삭제, 추가, 변환 했을 때 s2와 같아지는지 확인
 */

function OneEditpart(s1, s2) {
  while (s1.length != 0 && s2.length != 0) {
    if (s1[0] === s2[0]) {
      s1 = s1.slice(1);
      s2 = s2.slice(1);
    } else if (s1.slice(-1) === s2.slice(-1)) {
      s1 = s1.slice(0, -1);
      s2 = s2.slice(0, -1);
    } else {
      break;
    }
  }
  // 두 문자가 한개 이하로 남는다면, 하나만 '삭제 추가 변환' 으로 같게 만들 수 있다는 의미
  return s1.length <= 1 && s2.length <= 1;
}

console.log(OneEditpart("cat", "aat"));
