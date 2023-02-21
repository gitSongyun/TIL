function solution(participant, completion) {
    let answer = '';
    let dict = {}
    
    for (comp of completion) {
        if (dict[comp]) {
            dict[comp] += 1         
        } else {
            dict[comp] = 1
        }
    }
   

    for (part of participant) {
        if (!dict[part]) {
            answer = part
        } else {
            dict[part]--
        }

    }
    console.log(answer)
    return answer;
}