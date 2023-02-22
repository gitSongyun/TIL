function solution(cookie) {
    var answer = 0;
    let n = cookie.length

    for(let i=0; i < n-1; i++) {
        let fir = i;
        let sec = i+1;
        let firCookie = cookie[fir];
        let secCookie = cookie[sec];
        while (true) {
            if (firCookie === secCookie && answer < firCookie) {
                answer = firCookie;
            } else if (firCookie <= secCookie && fir !== 0) {
                firCookie += cookie[--fir];
            } else if (secCookie <= firCookie && sec !== n-1){
                secCookie += cookie[++sec];
            } else {
                break;
            }
        }
    }
    return answer;
}