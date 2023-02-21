const input = "{}{}[(())";

function solution(input) {
  const newInput = [...input];
  const stack = [];

  for (i of newInput) {
    if (i === "{" || i === "(" || i === "[") {
      stack.push(i);
    } else {
      switch (i) {
        case "}":
          if ("{" === stack[stack.length - 1]) {
            stack.pop();
            break
          }
        case ")":
          if ("(" === stack[stack.length - 1]) {
            stack.pop();
            break
          }
        case "]":
          if ("[" === stack[stack.length - 1]) {
            stack.pop();
            break
          } 
      }
    }
  }
  return stack
}
const res = solution(input);
console.log(res);
