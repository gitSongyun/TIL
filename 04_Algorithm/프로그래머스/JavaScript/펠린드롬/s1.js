function solution(plain) {
    const n = plain.length;
    var answer = n;

    let reverse = plain.split('').reverse().join('');

    for (let i=0; i<n; i++){
        let tf = true;
        for (let j=0; j<n-i; j++){
            if (plain[i+j] !== reverse[j]) {
                tf = false;
                break;
            }
        }
        if (tf) {
            answer += i;
            break;
        }

    }

    return answer;
}