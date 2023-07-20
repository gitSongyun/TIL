/**
 * 문제 링크 : https://codingdojang.com/scode/393
 * 1~N 까지 8이 몇갠가
 */

const input = Array(10000).fill(0).map((v, i)=> i).toString().split('').filter(v=>v === '8').length
console.log(input)