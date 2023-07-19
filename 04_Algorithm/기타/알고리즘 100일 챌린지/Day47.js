/*
 문제 링크 : https://codingdojang.com/scode/496
*/

function solution(n) {
  let plusList = [];
  let plusNum = n;
  let sqList = [];

  while (plusNum != "1") {
    for (num of plusNum) {
      let sq = parseInt(num) ** 2;
      plusList.push(sq);
    }

    plusNum = String(plusList.reduce((a, b) => a + b, 0));
    plusList = [];

    // 더 할 숫자가 입력 숫자가 된다면 무한 반복 된다.
    if (plusNum == n) {
      return false;
    }

    // 똑같은 숫자가 하나 더 나왔다면 무한 반복.
    for (i of sqList) {
      if (i === plusNum) {
        return false;
      }
    }

    sqList.push(plusNum);
  }

  return true;
}

console.log(solution(String(13)));

// 49

// 16 81
// 49 97
