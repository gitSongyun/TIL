 // 조합 코드
 const getCombinations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]); 
    // n개중에서 1개 선택할 때(nC1), 바로 모든 배열의 원소 return

    arr.forEach((fixed, index, origin) => {
      const rest = origin.slice(index + 1); 
      // 해당하는 fixed를 제외한 나머지 뒤
      const combinations = getCombinations(rest, selectNumber - 1); 
      // 나머지에 대해서 조합을 구한다.
      const attached = combinations.map((el) => [fixed, ...el]); 
      //  돌아온 조합에 떼 놓은(fixed) 값 붙이기
      results.push(...attached); 
      // 배열 spread syntax 로 모두다 push
    });

    return results; // 결과 담긴 results return
}

let a = getCombinations([0,1,2,3], 2)


// 코드 
function solution(dots) {
  const getInclination = ([[x1, y1], [x2, y2]]) => (x2 !== x1 ? (y2 - y1) / (x2 - x1) : Infinity);
  const isParallel = (line1, line2) => getInclination(line1) === getInclination(line2);

  return dots.some(dot => {
    const line1 = [dots[0], dot];
    const line2 = dots.filter(dot => !line1.includes(dot));
    return isParallel(line1, line2);
  })
    ? 1
    : 0;
}



