//  const getCombinations = function (arr, selectNumber) {
//     const results = [];
//     if (selectNumber === 1) return arr.map((el) => [el]);
//     // n개중에서 1개 선택할 때(nC1), 바로 모든 배열의 원소 return

//     arr.forEach((fixed, index, origin) => {
//       const rest = origin.slice(index + 1);
//       // 해당하는 fixed를 제외한 나머지 뒤
//       const combinations = getCombinations(rest, selectNumber - 1);
//       console.log('comb', combinations)
//       // 나머지에 대해서 조합을 구한다.
//       const attached = combinations.map((el) => [fixed, ...el]);
//       //  돌아온 조합에 떼 놓은(fixed) 값 붙이기
//       results.push(...attached);

//     });

//     return results; // 결과 담긴 results return
// }

// let array = [1,2,3,4]
// const res = getCombinations(array,3)

const getCombinations = (arr, selectNumber) => {
  const results = [];
  console.log("현재 arr", arr);
  if (selectNumber === 1) return arr.map((el) => [el]);

  arr.forEach((fixed, idx, origin) => {
    console.log(fixed);
    const rest = arr.slice(idx + 1);
    const combinations = getCombinations(rest, selectNumber - 1);
    console.log("그 어레이에 따른 콤비네이션", combinations);
    const attached = combinations.map((el) => [fixed, ...el]);
    console.log("콤비를 하나씩 뿌려서 fixed와 결합", attached);
    results.push(...attached);
  });

  return results;
};

console.log(getCombinations([1, 2, 3, 4], 3));
