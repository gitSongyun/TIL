function solution(number, k) {
    
  var answer = '';
  let stack = [];

  for (let num of number) {
      while (stack.length && stack[stack.length-1] < num && k > 0){
          k -= 1
          stack.pop()
      }
      stack.push(num)
      
  }
  if (k != 0) {
      stack = stack.slice(0,-k)
  }
  answer = stack.join('')
  return answer;
}