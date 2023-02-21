const price = [100, 60, 30];

function solution(price) {
  let minDay = parseInt(1e9);
  console.log(minDay);
  let maxDay = 0;
  let cnt = 0;
  // 가장 싼 날을 골라

  // 가장 비싼날에 팔아야한다.

  // 투포인터로 풀어보자
  for (let i = 0; i < Math.floor(price.length / 2); i++) {
    if (price[i] < minDay) {
      minDay = price[i];
    }

    if (price[price.length - 1 - i] > maxDay) {
      maxDay = price[price.length - 1 - i];
    }

    // 갯수가 홀수라면 왼쪽에서 하루 더해서 minPirce만 갱신
    if (price.length % 2) {
      if (price[i + 1] < minDay) {
        minDay = price[i + 1];
      }
    }
  }
  console.log(minDay, maxDay);
}
solution(price);
